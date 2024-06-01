#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 312
ED = 31889

src = Source(40)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (3389, 3616), (4071, 4177), (4293, 4355), (4663, 5021), (10723, 10847), (11428, 11460), (21636, 21667), (24106, 24141)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (10516, 10578), (29255, 29950)],
    STRONG_DEBAND_RANGES = [],
    LETTERBOX_RANGES = {
        (0, 233): dict(height=104, rekt_args=dict(rownum=[0, 871], rowval=[50, 50]), bb_args=dict(top=2, bottom=2, blur=500, thresh=5, y=False)),
        (19055, 19278): dict(height=104, rekt_args=dict(rownum=[0, 871], rowval=[50, 50]), bb_args=dict(top=2, bottom=2, blur=500, thresh=5, y=False)),
        (19279, 19361): dict(height=132),
        (27293, 27520): dict(height=132),
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
