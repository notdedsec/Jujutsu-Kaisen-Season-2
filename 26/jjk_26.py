#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 4651
ED = 31887

src = Source(26)
SRC = src.merge(complex_ranges = [(OP+1136, OP+1611)])

flt = Filter(
    SRC,
    NO_AA_RANGES = [],
    NO_RESCALE_RANGES = [(1854, 1901), (31827, 31862)],
    NO_DENOISE_RANGES = [],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099)],
    DIMMED_SCENES = {
        (3718, 3760): 1.225,
        (19736, 19803): 1.225,
        (21301, 21437): 1.325,
        (25406, 25451): 1.25,
        (25572, 25623): 1.25,
    }
)

enc = Encoder(SRC, flt.process(ED3=ED))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
