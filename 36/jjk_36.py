#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 1128
ED = 31889

src = Source(36)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (0, 117)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134), (27282, 27305)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (27282, 27305), (0, 117)],
    STRONG_DEBAND_RANGES = [(9214, 9405), (14116, 14130)]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
