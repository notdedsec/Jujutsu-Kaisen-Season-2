#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 1606
ED = 31266

src = Source(37)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (29106, 30605)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (14782, 14841), (15165, 28421), (29106, 30605)],
    STRONG_DEBAND_RANGES = [],
    LETTERBOX_RANGES = {
        (27607, 27876): dict(height=132)
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
