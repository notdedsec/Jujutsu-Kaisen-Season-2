#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 1606
ED = 31266

src = Source(37)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)])
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134), (29106, 30605)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (27607, 27876), (29106, 30605)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (8233, 8304), (24128, 24145), (24267, 24315)],
    DIMMED_SCENES = {
        (5514, 5525): 1.55,
        (7297, 7306): 1.4,
        (7523, 7564): 1.5,
        (8233, 8304): 1.225,
        (8257, 8304): 1.225,
        (8593, 8605): 1.5,
        (8645, 8649): 2,
        (10872, 10895): 1.225,
        (10881, 10881): 1.225,
        (11195, 11196): 1.5,
        (11215, 11216): 1.5,
        (11215, 11216): 1.5,
        (11226, 11227): 1.5,
        (11266, 11289): 1.225,
        (13968, 14009): 1.5,
        (24128, 24145): 1.5,
        (24267, 24315): 1.225,
        (26016, 26078): 1.225,
        (26016, 26041): 1.225,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [5514, 8593, 8600, 8645, -11069, -26037, 26038, 26040, 26042],
    LETTERBOX_RANGES = {
        (27607, 27876): dict(height=132, offset=2)
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
