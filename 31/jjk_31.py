#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 2997
ED = 31888

src = Source(31)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157), (19208, 19513), (19812, 19963)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (1669, 1731), (7671, 7769), (9198, 9286), (20084, 20200)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (6585, 6619), (10950, 11010)],
    DIMMED_SCENES = {
        (0, 173): 1.4,
        (2151, 2414): 1.225,
        (2170, 2175): 1.4,
        (2179, 2182): 1.1,
        (2247, 2250): 1.2,
        (2334, 2335): 1.5,
        (2748, 2804): 1.5,
        (5191, 5210): 1.4,
        (5202, 5207): 1.5,
        (5202, 5204): 1.5,
        (5708, 5863): 1.225,
        (6555, 6619): 1.225,
        (6557, 6560): 1.5,
        (6563, 6567): 1.5,
        (6580, 6619): 1.5,
        (7136, 7147): 1.1,
        (8286, 8345): 1.4,
        (8346, 8576): 1.225,
        (8859, 8954): 1.4,
        (10460, 10668): 1.225,
        (10538, 10545): 1.4,
        (10786, 11262): 1.4,
        (11359, 11430): 1.4,
        (11406, 11407): 1.225,
        (11803, 11844): 1.1,
        (11871, 11908): 1.225,
        (11903, 11944): 1.225,
        (12011, 12076): 1.225,
        (12248, 12434): 1.225,
        (12471, 12729): 1.225,
        (12682, 12685): 1.28,
        (13185, 13186): 2,
        (14841, 14922): 1.4,
        (16157, 16553): 1.225,
        (16393, 16394): 1.225,
        (18097, 18354): 1.225,
        (18929, 19147): 1.225,
        (19250, 19513): 1.4,
        (19493, 19499): 1.225,
        (19784, 20047): 1.4,
        (25779, 25876): 1.225,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [
        2165, 2166, 2170, 2171, 2170, 2172, 2176, 2179, 2247, 2248, 2249, -2333, -2335,
        5200, 5203, 5204, -5199, -12584, 12576, 12578, -16394, -16497, 16498, 16499,
        18128, -18133, -19462, 20029, -19974, 19975, 18128, -18132, 18133, 19498
    ] \
    + [x for x in range(12565, 12574) if x % 2 == 1] \
    + [x for x in range(18116, 18125) if x % 2 != 1] \
    + [x for x in range(19462, 19492) if x % 2 == 1] \
    + [x for x in range(12585, 12612) if x % 2 == 1 and x not in [12601]] \
    + [x for x in range(19025, 19072) if x % 2 == 1 and x not in [19029, 19059, 19061, 19063]] \
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
