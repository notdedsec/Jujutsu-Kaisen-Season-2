#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 7816
ED = 31889

src = Source(38)
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
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (1274, 1507)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (12294, 12302), (16212, 16222), (27930, 27943)],
    DIMMED_SCENES = {
        (12294, 12302): 3,
        (16212, 16222): 3,
        (16528, 16564): 1.225,
        (17812, 17879): 1.255,
        (20712, 20756): 1.225,
        (24190, 24373): 1.5,
        (24718, 24803): 1.225,
        (25131, 25178): 1.225,
        (25915, 25952): 1.5,
        (27896, 27943): 1.225,
        (27929, 27943): 1.225,
        (27931, 27943): 1.225,
        (27935, 27943): 2,
        (27942, 27943): 1.225,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [12277, 12279, -12302, 18978, 18980, 18984, 18988, -27933, -27932]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
