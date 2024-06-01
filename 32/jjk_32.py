#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 3909
ED = 31889

src = Source(32)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (7340, 7399), (7383, 7399), (9013, 9312), (9493, 9790), (10825, 10903)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157)],
    STRONG_DEBAND_RANGES = []
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
