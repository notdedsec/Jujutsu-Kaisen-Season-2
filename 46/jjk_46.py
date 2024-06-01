#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 9734
ED = 31529

src = Source(46)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (16995, 17294), (19827, 19910)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134), (4413, 4574)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (4413, 4574)],
    STRONG_DEBAND_RANGES = []
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
