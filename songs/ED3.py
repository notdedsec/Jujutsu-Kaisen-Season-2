#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder

src = Source(bouns='NCED3')
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [],
    NO_RESCALE_RANGES = [],
    NO_DENOISE_RANGES = [(760, 830), (871, 907), (949, 966), (1826, 2018)],
    STRONG_DEBAND_RANGES = [(0, 92), (1051, 1099)]
)

enc = Encoder(SRC, flt.process(ED3=0))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
