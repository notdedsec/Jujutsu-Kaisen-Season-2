#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 312
ED = 31889

src = Source(40)
SRC = src.merge(complex_ranges = [(OP+647, OP+676), (OP+856, OP+905), (OP+1107, OP+1465), (OP+1497, OP+1536), (OP+1582, OP+1860), (OP+2026, OP+2157)], black_frame=OP)
SRC = src.replace('common/OP4.mkv', repl_start=1316, main_start=OP+1324, duration=4)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


from debandshit import dumb3kdb
from vstools import replace_ranges

cursed_banding = dumb3kdb(SRC.clip_cut, radius=24, threshold=96, use_neo=True)
SRC.clip_cut = replace_ranges(SRC.clip_cut, cursed_banding, [(19712, 19757)])


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (29255, 29506)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (19712, 19757), (19362, 19423), (20104, 20111)],
    DIMMED_SCENES = {
        (4343, 4355): 1.1,
        (4895, 4896): 1.225,
        (4907, 4908): 2,
        (5787, 5788): 1.1,
        (5788, 5830): 1.05,
        (5789, 5830): 1.225,
        (5790, 5830): 1.225,
        (5791, 5830): 1.225,
        (5792, 5793): 1.225,
        (8999, 9032): 1.225,
        (9031, 9033): 1.225,
        (10934, 10963): 1.225,
        (10958, 10963): 1.5,
        (10959, 10963): 1.225,
        (19362, 19423): 2,
        (19676, 19757): 1.225,
        (19706, 19757): 1.8,
        (19712, 19757): 1.5,
        (19732, 19757): 1.2,
        (19727, 19729): 1.5,
        (20104, 20111): 2.225,
        (20124, 20127): 2.5,
        (20132, 20134): 2.5,
        (20755, 20807): 1.1,
        (20760, 20807): 1.225,
        (20872, 20893): 1.4,
        (21420, 21532): 2.45,
        (23084, 23095): 1.225,
        (23084, 23084): 1.5,
        (23098, 23104): 1.5,
        (23105, 23157): 1.225,
        (23137, 23157): 1.28,
        (23631, 23723): 1.6,
        (23850, 23885): 1.4,
        (24812, 24847): 1.225,
        (24812, 24816): 1.25,
        (24815, 24816): 1.25,
        (24816, 24816): 1.25,
        (24817, 24847): 1.128,
        (24841, 24852): 1.4,
        (24848, 24852): 1.4,
        (24857, 24870): 1.4,
        (24876, 24880): 2.5,
        (24881, 24909): 1.4,
        (34128, 34155): 2,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [
        4886, 4888, 4890, 4892, 4895, 4901, 9029, 9032, 9034, -10963, -10962, -10961, -10960, -10959, 20230, -20893,
        21470, 21474, 21476, 19716, 19721, 19723, 19725, 19730, 20112, -20125, -20134, 21480, 21482, -23097, 23098
    ],
    LETTERBOX_RANGES = {
        (0, 233): dict(height=104, offset=2),
        (19055, 19278): dict(height=104, offset=2),
        (19279, 19361): dict(height=132, offset=2),
        (27293, 27520): dict(height=132, offset=2),
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
