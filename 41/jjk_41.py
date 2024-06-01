#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = None
ED = None

src = Source(41)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(18293, 18321), (20921, 21012), (22222, 22227), (33583, 33810)],
    NO_RESCALE_RANGES = [(7119, 7178), (7219, 7278), (7322, 7393)],
    NO_DENOISE_RANGES = [(7119, 7178), (7219, 7278), (7322, 7393), (18165, 18174), (18185, 18190), (19789, 19848), (22420, 22581), (23555, 23799), (23920, 24201), (24310, 24705), (25852, 26121), (26266, 26529), (27820, 27963), (31242, 31322)],
    STRONG_DEBAND_RANGES = [(262, 318), (916, 1206), (11300, 11338), (17682, 17753), (31443, 31538)],
    LETTERBOX_RANGES = {
        (262, 9181): dict(height=104, rekt_args=dict(rownum=[0, 871], rowval=[50, 50]), bb_args=dict(top=2, bottom=2, blur=500, thresh=5, y=False)),
        (9302, 28731): dict(height=104, rekt_args=dict(rownum=[0, 871], rowval=[50, 50]), bb_args=dict(top=2, bottom=2, blur=500, thresh=5, y=False))
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
