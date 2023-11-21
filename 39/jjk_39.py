#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 6498
ED = 31888

src = Source(39)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (18691, 18714), (18721, 18727), (20205, 20846), (25507, 26385), (26749, 26820), (29857, 30081)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (5992, 6142), (8754, 9117), (11693, 11695), (14629, 14680), (14633, 14680), (14747, 14818), (18040, 18327), (24052, 24105)],
    DIMMED_SCENES = {
        (5886, 6142): 1.3,
        (6017, 6028): 3,
        (6074, 6142): 1.6,
        (8754, 8995): 1.6,
        (8996, 9031): 1.4,
        (9032, 9117): 1.6,
        (9515, 9637): 1.6,
        (9638, 9727): 1.35,
        (9878, 10003): 1.4,
        (9920, 9958): 1.65,
        (10244, 10309): 1.225,
        (10859, 10934): 1.225,
        (10916, 10934): 2.5,
        (10950, 10952): 1.55,
        (10950, 10951): 1.55,
        (11219, 11350): 1.225,
        (11600, 11716): 1.225,
        (11903, 11950): 1.225,
        (11917, 11920): 1.25,
        (11917, 11919): 1.5,
        (12850, 12874): 1.8,
        (14207, 14284): 1.225,
        (14215, 14224): 1.225,
        (14633, 14680): 1.85,
        (14747, 14818): 2.8,
        (18040, 18327): 1.225,
        (18150, 18327): 1.15,
        (18150, 18165): 1.5,
        (18247, 18327): 1.285,
        (24052, 24105): 1.5,
        (24052, 24060): 3.5,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [
        6015, 6017, 6019, 10896, 10898, 10900, 10903,
        10916, 10920, 10922, 10924, 10928, 10930, 10932, -10934,
        11693, 11917, 10950, 11683, 14215, 14225, 18247, 24052, 24067, 24063
    ]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
