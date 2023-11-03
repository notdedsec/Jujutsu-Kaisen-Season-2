#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 1344
ED = 31888

src = Source(33)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (0, 835)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (21804, 23297), (23346, 23537), (23636, 24308)],
    DIMMED_SCENES = {
        (4618, 4641): 1.3,
        (7744, 8421): 1.4,
        (8505, 8553): 1.4,
        (8578, 8695): 1.4,
        (8714, 8727): 1.4,
        (12452, 12498): 1.55,
        (12499, 12591): 1.75,
        (15687, 15767): 1.225,
        (19235, 19324): 1.285,
        (21804, 22016): 2,
        (22017, 22087): 1.5,
        (22088, 22135): 1.85,
        (22136, 22183): 1.5,
        (22184, 22964): 2,
        (22965, 23008): 1.5,
        (23009, 23092): 2,
        (23093, 23123): 1.5,
        (23124, 23297): 2,
        (23346, 23537): 1.625,
        (23636, 23755): 2,
        (23756, 23793): 1.65,
        (23794, 24078): 1.55,
        (24079, 24222): 2,
        (24223, 24308): 1.65,
        (27115, 27160): 1.3,
        (27187, 27231): 1.4,
        (27259, 27304): 1.4,
        (30641, 30748): 1.5,
        (30674, 30695): 1.4,
        (30714, 30745): 1.4,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [-21802, -21803, -30640]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
