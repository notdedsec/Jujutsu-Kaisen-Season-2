#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 7336
ED = None

src = Source(44)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(3056, 3130), (3227, 3262), (3293, 3421), (3483, 3526), (27526, 27720), (33567, 33685)],
    NO_RESCALE_RANGES = [(2858, 2899), (2948, 2983), (3026, 3055)],
    NO_DENOISE_RANGES = [(OP, OP+2157), (2858, 2899), (2948, 2983), (3026, 3055), (14295, 14498), (18560, 18637), (19468, 19631), (27364, 27525), (33567, 33685)],
    STRONG_DEBAND_RANGES = [(18734, 18741), (18993, 19042)]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
