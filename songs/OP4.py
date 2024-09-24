#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder

src = Source(bouns='NCOP4')
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [],
    NO_RESCALE_RANGES = [],
    NO_DENOISE_RANGES = [(0, 2157)],
    STRONG_DEBAND_RANGES = []
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
