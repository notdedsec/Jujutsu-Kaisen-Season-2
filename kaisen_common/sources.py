import os
from typing import List, Tuple

from vsscale import SSIM
from vskernels import BicubicDidee
from vsrgtools import lehmer_diff_merge
from vstools import initialize_clip, replace_ranges, core
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
    FILE = None


    def __init__(self, episode: int):
        self.episode = episode
        self.sources = self.ROOT / str(episode) / 'sources'


    def get_source(self, pattern):
        src = next(self.sources.glob(pattern))
        trims = (24, None) if 'DSNP' in str(src) else (None, None)
        preset = [PresetWEB, PresetEAC3] if 'DSNP' in str(src) or 'AMZN' in str(src) else [PresetWEB, PresetAAC]

        SRC = FileInfo(src, trims, preset=preset)
        SRC.clip_cut = initialize_clip(SRC.clip_cut)

        return SRC


    def merge(self, complex_ranges: List[Tuple[int, int]] = []):
        CR = self.get_source('*SubsPlease*.mkv')
        BB = self.get_source('*ToonsHub*.mkv')
        AZ = self.get_source('*AMZN*.mkv')
        DP = self.get_source('*DSNP*.mkv')

        cr, bb, dp = [src.clip_cut for src in [CR, BB, DP]]
        bb = SSIM(sigmoid=True, kernel=BicubicDidee()).scale(bb, 1920, 1080)

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

