#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 4651
ED = 31887

src = Source(26)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(OP, OP+50), (OP+518, OP+719), (14255, 14614), (15517, 15581), (15987, 17181)],
    NO_RESCALE_RANGES = [(1854, 1901), (31827, 31862)],
    NO_DENOISE_RANGES = [(ED+760, ED+830), (ED+871, ED+907), (ED+949, ED+966), (ED+1826, ED+2018), (OP+518, OP+649), (12956, 12991), (13028, 13182), (13502, 13643), (30775, 30903)],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099)]
)

enc = Encoder(SRC, flt.process(ED3=ED))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
