#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 6834
ED = 31889

src = Source(35)
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
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (15730, 21693)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (21160, 21411)],
    DIMMED_SCENES = {
        (5029, 5051): 1.4,
        (10262, 10266): 1.5,
        (10262, 10263): 1.5,
        (10355, 10357): 2.5,
        (12903, 12990): 1.75,
        (25483, 25536): 2.25,
        (28132, 28184): 1.3,
        (28132, 28134): 1.8,
        (30631, 30797): 1.1,
        (30798, 30842): 1.25,
        (30814, 30842): 1.25,
        (30727, 30733): 1.8,
        (30808, 30813): 2.5,
        (30824, 30830): 1.2,
        (30707, 30707): 1.5,
        (30661, 30661): 1.5,
        (31102, 31103): 1.225,
        (31104, 31106): 1.4,
        (31107, 31155): 1.525,
        (31108, 31111): 1.2,
        (26193, 26194): 1.4,
        (27448, 27501): 1.35,
        (27482, 27484): 1.65,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [
        10355, 10356, 27216, 27218, 27220, 27222, 27448, 30808, 30810, 30812, 30818, 30820, 30822, 30824, 30826,
        30727, 30729, 30731, 30734, 25485, 25487, 25489, 25491, 25493, 25495, 25497, 25499, 25503, 25505, 25507,
        25509, 25511, 25513, 25515, 25517, 25519, 25521, 25523, 25525, 25527, 25529, 25531, 25533, -25536
    ]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
