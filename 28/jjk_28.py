#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 1846
ED = 28363

src = Source(28)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(OP, OP+50), (OP+518, OP+719), (14243, 14494)],
    NO_RESCALE_RANGES = [(7030, 7235), (12328, 12360), (27469, 27601)],
    NO_DENOISE_RANGES = [(ED+760, ED+830), (ED+871, ED+907), (ED+949, ED+966), (ED+1826, ED+2018), (OP+518, OP+649), (7030, 7235), (10427, 10696), (12328, 12360), (16798, 16893), (19321, 19487), (21009, 21174), (22064, 22171), (22196, 22324), (22351, 22446), (23944, 24406), (25483, 25800), (27030, 27207), (27469, 27601)],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099), (11101, 11132)]
)

enc = Encoder(SRC, flt.process(ED3=ED))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
