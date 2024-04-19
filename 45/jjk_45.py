#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 5251
ED = 31529

src = Source(45)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (19956, 20117)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (19956, 20117)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157)],
    DIMMED_SCENES = {
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
        (2092, 2330): 1.5,
        (8578, 8673): 1.225,
        (10613, 10616): 3,
        (11485, 11748): 2.4,
        (13189, 13434): 1.225,
        (13369, 13434): 1.5,
        (14788, 14877): 1.4,
        (14850, 14877): 1.2,
        (15208, 15369): 1.4,
        (15784, 15873): 1.85,
        (19728, 19739): 2.5,
        (20606, 20671): 1.5,
        (22922, 23023): 1.5,
        (22940, 22963): 1.225,
        (23024, 23095): 1.225,
        (23210, 23269): 1.225,
        (24044, 24139): 1.2,
        (24326, 24373): 1.5,
        (24361, 24373): 2.1,
        (24382, 24421): 1.225,
        (25559, 25649): 1.225,
        (25562, 25649): 1.225,
        (25595, 25649): 1.28,
        (25806, 26087): 1.225,
        (25975, 25991): 2,
        (30673, 30744): 1.225,
    },
    NUKE_FRAMES = [10613, 10615]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
