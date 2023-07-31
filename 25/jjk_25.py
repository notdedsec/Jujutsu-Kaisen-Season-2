#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 15562
ED = 31888

src = Source(25)
SRC = src.merge(complex_ranges = [(OP+1136, OP+1611)])

flt = Filter(
    SRC,
    NO_AA_RANGES = [(574, 694), (812, 1073), (1437, 1669), (20990, 21026), (21542, 21609)],
    NO_RESCALE_RANGES = [(2422, 2814), (26574, 26922)],
    NO_DENOISE_RANGES = [(2422, 2814)],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099), (0, 467)],
    DIMMED_SCENES = {
        (1334, 1357): 1.225,
        (26922, 27298): 1.225,
    }
)

enc = Encoder(SRC, flt.process(ED3=ED))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
