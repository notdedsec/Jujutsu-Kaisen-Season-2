#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 7170
ED = 31888

src = Source(30)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (0, 116), (30501, 30563), (30671, 30742)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157)],
    DIMMED_SCENES = {
        (1012, 1106): 1.225,
        (1594, 1722): 1.225,
        (5511, 5565): 1.225,
        (5948, 6038): 1.1,
        (12896, 12940): 1.225,
        (17082, 17140): 1.225,
        (31715, 31887): 1.225,
        (31734, 31739): 1.4,
        (31743, 31746): 1.1,
        (31811, 31814): 1.2,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [31729, 31730, 31734, 31735, 31734, 31736, 31740, 31743, 31811, 31812, 31813],
    LETTERBOX_RANGES = {
        (14264, 16429): dict(height=52, shift=-2),
        (16514, 17043): dict(height=52, shift=-2),
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
