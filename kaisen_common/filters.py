#!C:/KaizokuEncoderV2/python

from typing import Any, List, Dict, Tuple, Optional
from vardautomation import FileInfo
from vapoursynth import VideoNode

from vsaa import Nnedi3
from vsaa.antialiasers.eedi3 import Eedi3SR
from vskernels import Bicubic, BicubicDidee
from vsscale import SSIM, descale_detail_mask
from vsdenoise import MVTools, SADMode, Prefilter
from vstools import core, replace_ranges, join, set_output
from havsfunc import FineDehalo, EdgeCleaner
from vsutil import get_w, get_y, depth
from vsrgtools import contrasharpening
from jvsfunc import retinex_edgemask
from adptvgrnMod import adptvgrnMod
from debandshit import dumb3kdb
from adjust import Tweak

from kaisen_common.utils import letterbox_fix


class Filter:

    native_res = 844


    def __init__(
        self,
        SRC: FileInfo,
        NO_AA_RANGES: List[Tuple[int, int]] = [],
        NO_RESCALE_RANGES: List[Tuple[int, int]] = [],
        NO_DENOISE_RANGES: List[Tuple[int, int]] = [],
        STRONG_DEBAND_RANGES: List[Tuple[int, int]] = [],
        DIMMED_SCENES: Dict[Tuple[int, int], float] = {},
        NUKE_FRAMES: List[int] = [],
        LETTERBOX_RANGES: Dict[Tuple[int, int], Dict[str, Any]] = {}
    ):

        self.SRC = SRC
        self.NO_AA_RANGES = NO_AA_RANGES
        self.NO_RESCALE_RANGES = NO_RESCALE_RANGES
        self.NO_DENOISE_RANGES = NO_DENOISE_RANGES
        self.STRONG_DEBAND_RANGES = STRONG_DEBAND_RANGES
        self.DIMMED_SCENES = DIMMED_SCENES
        self.NUKE_FRAMES = NUKE_FRAMES
        self.LETTERBOX_RANGES = LETTERBOX_RANGES


    def process(self, ED3: Optional[int] = None) -> VideoNode:
        clip = depth(self.SRC.clip_cut, 16)

        unghosted = clip
        for frame in self.NUKE_FRAMES:
            unghosted = unghosted.std.DeleteFrames(abs(frame))
            unghosted = unghosted.std.DuplicateFrames(frame if frame > 0 else abs(frame) - 1)

        undimmed = unghosted
        for ranges, strength in self.DIMMED_SCENES.items():
            tweak = Tweak(undimmed, sat=strength, cont=strength)
            undimmed = replace_ranges(undimmed, tweak, ranges)

        src = undimmed
        src_y = get_y(src)

        descaled = Bicubic().descale(src_y, get_w(self.native_res), self.native_res)
        upscaled = Nnedi3(pscrn=1).scale(descaled, descaled.width*2, descaled.height*2)

        eedi3 = Eedi3SR(alpha=0.125, beta=0.25, gamma=80, vthresh0=12, vthresh1=24, vthresh2=4, sclip_aa=True)
        aa = eedi3.aa(upscaled.std.Transpose())
        aa = eedi3.aa(aa.std.Transpose())
        aa = replace_ranges(aa, upscaled, self.NO_AA_RANGES)

        if ED3:
            descaled_ED3 = Bicubic().descale(src_y, get_w(842), 842)
            upscaled_ED3 = Nnedi3(pscrn=1).scale(descaled_ED3, descaled.width*2, descaled.height*2)
            aa = replace_ranges(aa, upscaled_ED3, [(ED3, ED3+2157)])

        fine_dehalo = FineDehalo(aa, darkstr=0, thlimi=16, thmi=64)
        edge_clean = EdgeCleaner(fine_dehalo, strength=8, smode=1, hot=True)
        dehalo = core.std.Expr([fine_dehalo, edge_clean], 'x y min')

        ssim_downscale = SSIM(sigmoid=True, kernel=BicubicDidee()).scale(dehalo, src.width, src.height)
        retinex_mask = retinex_edgemask(src_y, brz=7000).std.Inflate().std.Maximum().std.Inflate()
        downscaled = core.std.MaskedMerge(src_y, ssim_downscale, retinex_mask)

        bicubic_upscale = Bicubic().scale(descaled, src.width, src.height)
        restore_mask = descale_detail_mask(src_y, bicubic_upscale, thr=0.04, inflate=4, xxpand=(4, 4))
        restored = core.std.MaskedMerge(downscaled, src_y, restore_mask)

        rescale = replace_ranges(restored, src_y, self.NO_RESCALE_RANGES)
        rescale = join(rescale, src)

        denoise_y = MVTools.denoise(get_y(rescale), thSAD=48, block_size=32, overlap=16, prefilter=Prefilter.MINBLUR2, sad_mode=SADMode.SPATIAL.same_recalc)
        denoise_y = denoise_y.ttmpsm.TTempSmooth(maxr=1, thresh=1, mdiff=0, strength=1)
        denoise = join(denoise_y, rescale)
        denoise = replace_ranges(denoise, rescale, self.NO_DENOISE_RANGES)

        dumb_deband_normal = dumb3kdb(denoise, radius=16, threshold=24, use_neo=True)
        dumb_deband_strong = dumb3kdb(denoise, radius=16, threshold=48, use_neo=True)
        dumb_deband = replace_ranges(dumb_deband_normal, dumb_deband_strong, self.STRONG_DEBAND_RANGES)
        deband = core.std.MaskedMerge(dumb_deband, denoise, retinex_mask)
        contra = contrasharpening(deband, rescale)

        grain = adptvgrnMod(contra, strength=0.24, luma_scaling=8, sharp=64, grain_chroma=False, static=True)
        final = depth(grain, 10).std.Limiter(16 << 2, [235 << 2, 240 << 2], [0, 1, 2])

        for ranges, params in self.LETTERBOX_RANGES.items():
            params['ranges'] = ranges
            final = letterbox_fix(final, src, **params)

        set_output(src)
        # set_output(upscaled)
        # set_output(aa)
        # set_output(dehalo)
        # set_output(downscaled)
        # set_output(retinex_mask)
        # set_output(restore_mask)
        # set_output(restored)
        # set_output(rescale)
        # set_output(denoise)
        # set_output(deband)
        # set_output(contra)
        set_output(final)

        return final

