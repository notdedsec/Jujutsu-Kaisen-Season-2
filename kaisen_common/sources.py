import os
from typing import List, Tuple, Optional

from vsscale import SSIM
from vskernels import BicubicDidee
from vsrgtools import lehmer_diff_merge
from vstools import initialize_clip, replace_ranges, core
from vardautomation import FileInfo, VPath, Preset, PresetType, PresetBD, PresetEAC3, PresetAAC

from kaisen_common.utils import circle_mask


PresetWEB = Preset(
    idx=core.ffms2.Source,
    a_src=None,
    a_src_cut=None,
    a_enc_cut=None,
    chapter=None,
    preset_type=PresetType.VIDEO
)


class Source:

    ROOT = VPath(os.path.dirname(__file__)).parent
    BDMV = ROOT / 'BDMV'
    FILE = None

    VOLUME = {
        1: BDMV / 'JUJUTSUKAISEN_SEASON2_1',
        2: BDMV / 'JUJUTSUKAISEN_SEASON2_2',
        3: BDMV / 'JUJUTSUKAISEN_SEASON2_3',
        4: BDMV / 'JUJUTSUKAISEN_SEASON2_4',
        5: BDMV / 'JUJUTSUKAISEN_SEASON2_5',
        6: BDMV / 'JUJUTSUKAISEN_SEASON2_6',
        7: BDMV / 'JUJUTSUKAISEN_SEASON2_7',
        8: BDMV / 'JUJUTSUKAISEN_SEASON2_8',
    }

    EPISODE = {
        25: VOLUME[1] / 'BDMV/STREAM/00002.m2ts',
        26: VOLUME[1] / 'BDMV/STREAM/00003.m2ts',
        27: VOLUME[1] / 'BDMV/STREAM/00004.m2ts',
        28: VOLUME[2] / 'BDMV/STREAM/00002.m2ts',
        29: VOLUME[2] / 'BDMV/STREAM/00003.m2ts',
    }

    BONUS = {
        'NCOP3': VOLUME[1] / 'BDMV/STREAM/00005.m2ts',
        'NCED3': VOLUME[1] / 'BDMV/STREAM/00010.m2ts',
    }


    def __init__(self, episode: Optional[int] = None, bouns: Optional[str] = None):
        assert episode or bouns

        self.episode = episode
        self.sources = self.ROOT / str(episode) / 'sources'

        if bouns in self.BONUS and self.BONUS[bouns].exists():
            self.FILE = FileInfo(self.BONUS[bouns], preset=[PresetBD, PresetAAC])

        if episode in self.EPISODE and self.EPISODE[episode].exists():
            self.FILE = FileInfo(self.EPISODE[episode], preset=[PresetBD, PresetAAC])


    def get_file(self):
        assert self.FILE
        return self.FILE


    def get_source(self, pattern):
        src = next(self.sources.glob(pattern))
        trims = (24, None) if 'DSNP' in str(src) else (None, None)
        preset = [PresetWEB, PresetEAC3] if 'DSNP' in str(src) or 'AMZN' in str(src) else [PresetWEB, PresetAAC]

        SRC = FileInfo(src, trims, preset=preset)
        SRC.clip_cut = initialize_clip(SRC.clip_cut)

        return SRC


    def merge(self, complex_ranges: List[Tuple[int, int]] = [], black_frame: int = 0, use_amzn: bool = False):
        CR = self.get_source('*SubsPlease*.mkv')
        BB = self.get_source('*ToonsHub*.mkv')
        AZ = self.get_source('*AMZN*.mkv')
        DP = self.get_source('*DSNP*.mkv' if not use_amzn else '*AMZN*.mkv')

        cr, bb, dp = [src.clip_cut for src in [CR, BB, DP]]
        bb = SSIM(sigmoid=True, kernel=BicubicDidee()).scale(bb, 1920, 1080)

        if black_frame:
            cr = core.std.MaskedMerge(cr, dp, circle_mask(cr)[black_frame])
            dp = core.std.MaskedMerge(dp, cr, circle_mask(dp)[black_frame])

        src_a = lehmer_diff_merge(cr, dp)
        src_b = lehmer_diff_merge(cr, bb)
        merge = replace_ranges(src_a, src_b, complex_ranges)

        AZ.clip = AZ.clip_cut = merge
        self.FILE = AZ

        return self.FILE


    def replace(self, replacement: str, repl_start: int, main_start: int, duration: int):
        assert self.FILE
        main_clip = self.FILE.clip_cut

        repl_file = FileInfo(self.ROOT / replacement)
        repl_clip = initialize_clip(repl_file.clip_cut)
        repl_clip = repl_clip.std.AssumeFPS(fpsnum=24000, fpsden=1001)

        if repl_clip.height > 1080:
            repl_clip = SSIM(sigmoid=True, kernel=BicubicDidee()).scale(repl_clip, 1920, 1080)

        repl_end = repl_start + duration
        main_end = main_start + duration

        replaced = main_clip[:main_start] + repl_clip[repl_start:repl_end] + main_clip[main_end:]
        self.FILE.clip = self.FILE.clip_cut = replaced

        return self.FILE


    def get_encode(self):
        enc = self.sources.parent / f'jjk_{self.episode}_premux.mkv'
        ENC = FileInfo(enc, preset=[PresetWEB, PresetEAC3])        

        return ENC

