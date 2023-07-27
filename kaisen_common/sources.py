import os
from typing import List, Tuple

from vsscale import SSIM
from vskernels import BicubicDidee
from vsrgtools import lehmer_diff_merge
from vstools import depth, replace_ranges, core
from vardautomation import FileInfo, VPath, Preset, PresetType, PresetEAC3, PresetAAC


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


    def __init__(self, episode: int):
        self.episode = episode
        self.sources = self.ROOT / str(episode) / 'sources'


    def get_source(self, pattern):
        src = next(self.sources.glob(pattern))
        trims = (24, None) if 'DSNP' in str(src) else (None, None)
        preset = [PresetWEB, PresetEAC3] if 'DSNP' in str(src) or 'AMZN' in str(src) else [PresetWEB, PresetAAC]
        SRC = FileInfo(src, trims, preset=preset)
        return SRC


    def merge(self, complex_ranges: List[Tuple[int, int]] = []):
        CR = self.get_source('*SubsPlease*.mkv')
        BB = self.get_source('*ToonsHub*.mkv')
        AZ = self.get_source('*AMZN*.mkv')
        DP = self.get_source('*DSNP*.mkv')

        cr, bb, dp = [depth(src.clip_cut, 16) for src in [CR, BB, DP]]
        bb = SSIM(sigmoid=True, kernel=BicubicDidee()).scale(bb, 1920, 1080)

        src_a = lehmer_diff_merge(cr, dp)
        src_b = lehmer_diff_merge(cr, bb)
        merge = replace_ranges(src_a, src_b, complex_ranges)

        AZ.clip = AZ.clip_cut = merge
        return AZ


    def get_encode(self):
        enc = self.sources.parent / f'jjk_{self.episode}_premux.mkv'
        ENC = FileInfo(enc, preset=[PresetWEB, PresetEAC3])        
        return ENC

