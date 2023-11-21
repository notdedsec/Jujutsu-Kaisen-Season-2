#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 1128
ED = 31889

src = Source(36)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134), (27282, 27305)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (27282, 27305)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157)],
    DIMMED_SCENES = {
        (7549, 7596): 1.4,
        (7765, 7788): 2,
        (10076, 10233): 1.15,
        (14493, 14522): 1.15,
        (14523, 14552): 1.05,
        (16409, 16414): 1.2,
        (21294, 21365): 1.2,
        (23780, 23802): 1.3,
        (23810, 23824): 1.1,
        (24906, 25019): 1.35,
        (25086, 25157): 1.35,
        (31805, 31849): 1.4,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [
        -16408, -16411, 16415, 31837, 31839, 31841, 31843, 31847,
        23803, 23810, 24969, 24972, 24975, 24978, 24981, 24984, 24996
    ]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
