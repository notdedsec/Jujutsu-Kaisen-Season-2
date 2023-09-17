#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 0
ED = 31888

src = Source(29)
SRC = src.merge(complex_ranges = [(OP+1136, OP+1611)])


flt = Filter(
    SRC,
    NO_AA_RANGES = [(18115, 18234), (18539, 18645), (20161, 20402)],
    NO_RESCALE_RANGES = [],
    NO_DENOISE_RANGES = [],
    STRONG_DEBAND_RANGES = [(ED, ED+92), (ED+1051, ED+1099)],
    DIMMED_SCENES = {
        (4989, 5011): 1.4,
        (19866, 19888): 1.5,
        (19902, 19924): 1.4,
        (19935, 20029): 1.4,
        (20030, 20160): 1.225,
    },
    NUKE_FRAMES = [19889, 19902, 19925],
    LETTERBOX_RANGES = {
        (31049, 31119): dict(height=132, offset=2),
    }
)

enc = Encoder(SRC, flt.process(ED3=ED))


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
