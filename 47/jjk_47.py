#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = 0
ED = 31889

src = Source(47)
src.replace('47/masks/geto.png', repl_start=0, main_start=28530, duration=192)
src.replace('47/masks/gojo.png', repl_start=0, main_start=28722, duration=252)
src.replace('47/masks/yaga.png', repl_start=0, main_start=28974, duration=228)
src.replace('47/masks/yuji.png', repl_start=0, main_start=29202, duration=180)
src.replace('47/masks/yuta.png', repl_start=0, main_start=29382, duration=180)
SRC = src.get_file()


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157), (19867, 20334)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134), (28530, 29561)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (OP, OP+2157), (8858, 9148), (9848, 10246), (11080, 11889), (27407, 28286)],
    STRONG_DEBAND_RANGES = [(10247, 10945), (27464, 27957)]
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
