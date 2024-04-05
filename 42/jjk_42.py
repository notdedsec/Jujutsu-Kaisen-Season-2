#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 2494
ED = 31530

src = Source(42)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)

DSNP = src.get_source('*DSNP*.mkv')
SRC.clip = SRC.clip_cut = SRC.clip_cut[0:33925] + DSNP.clip_cut[33925:34045]


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (13782, 13949), (14094, 14159)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (11346, 11573), (24551, 24610)],
    DIMMED_SCENES = {
        (8384, 8454): 1.05,
        (10090, 10095): 1.15,
        (10096, 10184): 1.4,
        (11310, 11345): 1.1,
        (11346, 11573): 1.4,
        (15957, 16052): 1.4,
        (16500, 16572): 1.15,
        (16902, 16997): 1.225,
        (17052, 17147): 1.8,
        (17244, 17303): 1.225,
        (23100, 23103): 1.4,
        (23102, 23102): 4,
        (23174, 23245): 1.225,
        (24551, 24610): 1.5,
        (27191, 27286): 1.2,
        (29304, 29367): 1.5,
        (30575, 30622): 1.15,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [-8383, 10094, 10096, 10099, 10101, 10103, 10105, 23098, 27191]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
