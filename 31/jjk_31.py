#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 2997
ED = 31888

src = Source(31)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (1669, 1731), (7671, 7769), (9198, 9286), (20084, 20200)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157)],
    STRONG_DEBAND_RANGES = []
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
