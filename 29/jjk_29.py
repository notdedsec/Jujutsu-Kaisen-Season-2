#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 0
ED = 31888

src = Source(29)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(OP, OP+50), (OP+518, OP+719), (2564, 2662), (2909, 3032), (3908, 4091), (4353, 4616), (13770, 14279), (15541, 15723), (18115, 18234), (18539, 18645), (19532, 20029), (20161, 20402), (27102, 28118)],
    NO_RESCALE_RANGES = [],
    NO_DENOISE_RANGES = [(ED+760, ED+830), (ED+871, ED+907), (ED+949, ED+966), (ED+1826, ED+2018), (OP+518, OP+649)],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099)],
    LETTERBOX_RANGES = {
        (31050, 31120): dict(height=132),
    }
)

enc = Encoder(SRC, flt.process(ED3=ED))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
