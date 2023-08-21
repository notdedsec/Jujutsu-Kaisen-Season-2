#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 4173
ED = 31889

src = Source(27)
SRC = src.merge(complex_ranges = [(OP+1136, OP+1611)])
SRC = src.replace('common/PV1.mkv', repl_start=1299, main_start=22805, duration=4)


flt = Filter(
    SRC,
    NO_AA_RANGES = [],
    NO_RESCALE_RANGES = [(15993, 16046)],
    NO_DENOISE_RANGES = [(15993, 16046)],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099)],
    DIMMED_SCENES = {
        (3683, 3729): 1.225,
        (13498, 13593): 1.225,
        (16300, 16318): 1.225,
        (17503, 17538): 1.35,
        (17513, 17538): 1.35,
        (19226, 19243): 1.225,
        (19315, 19671): 1.225,
        (19516, 19533): 1.1,
        (19621, 19671): 1.1,
        (19856, 19879): 1.225,
        (19869, 19879): 1.1,
        (20846, 20898): 1.225,
        (20899, 20899): 1.5,
        (20900, 20903): 1.225,
        (20904, 20905): 1.8,
        (20906, 20923): 1.225,
        (20924, 20927): 1.6,
        (20928, 21164): 1.225,
        (21386, 21418): 1.25,
        (21885, 21910): 1.1,
        (22766, 22804): 1.225,
        (22809, 22812): 2,
        (22813, 22842): 1.225,
        (23364, 23387): 1.225,
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
