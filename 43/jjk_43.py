#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 1462
ED = 31530

src = Source(43)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)

DSNP = src.get_source('*DSNP*.mkv')
SRC.clip = SRC.clip_cut = SRC.clip_cut[0:33961] + DSNP.clip_cut[33961:34045]


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157)],
    DIMMED_SCENES = {
        (6070, 6071): 1.05,
        (6072, 6073): 1.11,
        (6074, 6074): 1.14,
        (6075, 6080): 1.225,
        (6096, 6097): 2,
        (6096, 6116): 1.225,
        (6257, 6266): 2,
        (6317, 6317): 1.1,
        (6318, 6318): 1.18,
        (6319, 6320): 1.25,
        (6321, 6330): 1.285,
        (6594, 6595): 1.6,
        (6596, 6612): 1.225,
        (6613, 6648): 1.4,
        (6649, 6654): 1.8,
        (6655, 6655): 1.6,
        (6656, 6656): 1.5,
        (6657, 6657): 1.3,
        (6658, 6658): 1.2,
        (6659, 6659): 1.1,
        (6660, 6660): 1.05,
        (7475, 7477): 1.1,
        (7478, 7482): 1.15,
        (7483, 7486): 1.25,
        (7487, 7492): 1.5,
        (7493, 7505): 1.5,
        (7493, 7494): 1.25,
        (7498, 7505): 1.5,
        (7939, 8003): 1.625,
        (9767, 9767): 1.05,
        (9768, 9769): 1.1,
        (9770, 9770): 1.15,
        (9771, 9771): 1.2,
        (9772, 9772): 1.22,
        (9773, 9773): 1.225,
        (9774, 9774): 1.28,
        (9775, 9791): 1.4,
        (9792, 9827): 2,
        (9828, 9863): 1.28,
        (9924, 10055): 1.5,
        (10138, 10139): 1.15,
        (10140, 10140): 1.3,
        (10141, 10143): 1.4,
        (10144, 10148): 1.625,
        (10149, 10149): 1.32,
        (10150, 10151): 1.18,
        (10152, 10163): 1.15,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [
        6096, 6098, 6257, 6259, 6267, -6595, 7493, 7496, -7501, # 7487, -7490, -7492, 7498,
        7939, 7942, 7946, 7950, 10146, 10141, 12097, 12100, 12102, 13317
    ]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
