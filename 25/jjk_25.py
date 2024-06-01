#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 15562
ED = 31888

src = Source(25)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(OP, OP+50), (OP+518, OP+719), (574, 694), (812, 1073), (1437, 1669), (20668, 20710),  (20990, 21026), (21542, 21609)],
    NO_RESCALE_RANGES = [(2422, 2814), (26574, 26922)],
    NO_DENOISE_RANGES = [(ED+760, ED+830), (ED+871, ED+907), (ED+949, ED+966), (ED+1826, ED+2018), (OP+518, OP+649), (2422, 2814), (0, 467)],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099), (0, 467)]
)

enc = Encoder(SRC, flt.process(ED3=ED))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
