#!C:/KaizokuEncoderV2/python

from kaisen_common.sources import Source
from kaisen_common.filters import Filter
from kaisen_common.encoder import Encoder


OP = None
ED = 32176

src = Source(41)
SRC = src.merge(complex_ranges = [], black_frame=1)
SRC = src.replace('common/ED4.mkv', repl_start=1522, main_start=ED+1522, duration=13)
SRC = src.replace('common/ED4.mkv', repl_start=1552, main_start=ED+1552, duration=15)
SRC = src.replace('common/ED4.mkv', repl_start=1598, main_start=ED+1598, duration=14)
SRC = src.replace('common/ED4.mkv', repl_start=2137, main_start=ED+2137, duration=18)


from debandshit import dumb3kdb
from vstools import replace_ranges

cursed_banding = dumb3kdb(SRC.clip_cut, radius=24, threshold=48, use_neo=True)
SRC.clip_cut = replace_ranges(SRC.clip_cut, cursed_banding, [(19091, 19256), (23528, 23941), (25694, 25729)])


flt = Filter(
    SRC,
    NO_AA_RANGES = [(ED, ED+2157)],
    NO_RESCALE_RANGES = [(ED+1973, ED+2134)],
    NO_DENOISE_RANGES = [(ED+1973, ED+2134), (20261, 20422), (21825, 21938), (22136, 22531), (23066, 23095), (23942, 24205)],
    STRONG_DEBAND_RANGES = [(ED+1522, ED+1535), (ED+1552, ED+1567), (ED+1598, ED+1612), (ED+2137, ED+2157), (29967, 30017), (30063, 30263)] + [(14205, 14232), (15304, 15340), (17567, 17638), (18017, 18124), (19091, 19256), (20123, 20154), (23528, 23941), (25694, 25729)],
    DIMMED_SCENES = {
        (7119, 7160): 1.225,
        (7322, 7363): 1.225,
        (7322, 7335): 1.225,
        (10011, 10043): 1.2,
        (10016, 10020): 1.6,
        (10016, 10016): 1.8,
        (10017, 10017): 1.3,
        (14205, 14235): 2.5,
        (14205, 14208): 1.15,
        (14219, 14221): 1.35,
        (14220, 14221): 1.15,
        (14232, 14232): 1.45,
        (15304, 15340): 1.225,
        (16085, 16087): 3,
        (16503, 16505): 2.5,
        (16505, 16505): 1.5,
        (18017, 18124): 1.4,
        (19103, 19354): 1.225,
        (19099, 19354): 1.1,
        (19103, 19354): 1.1,
        (19105, 19354): 1.1,
        (19107, 19354): 1.1,
        (19109, 19354): 1.1,
        (19111, 19354): 1.1,
        (19113, 19354): 1.1,
        (19117, 19212): 1.15,
        (19117, 19189): 1.25,
        (20123, 20260): 1.4,
        (20149, 20154): 1.4,
        (20155, 20260): 1.1,
        (23798, 23941): 2.8,
        (25640, 25729): 1.4,
        (25696, 25729): 2,
        (ED+1503, ED+1521): 1.225,
        (ED+1545, ED+1551): 1.225,
        (ED+2135, ED+2136): 1.5,
    },
    NUKE_FRAMES = [
        -11781, 11783, 11802, 11807, 15310, -15312, 15313, 15315, 15318, 15320, -15322, 15328, 15336, 16085, 16503, 20148,
        -25604, 25607, -25612, 25613, 25614, 25615, -25620, 25621, 25622, 25623, -25628, 25629, 25630, 25631, -25638,
        25685, 25687, 25691, 25700, 25702, 25704, 25706, 25708, 25710, 25712, 25714, 25716, 25719, 25721, 25723, 25728,
        14210, 14213, 14216, 14223, -14228, 14229, -14221
    ],
    LETTERBOX_RANGES = {
        (262, 26407): dict(height=104, offset=2)
    }
)

enc = Encoder(SRC, flt.process())


if __name__ == '__main__':
    enc.run()
    enc.clean()
    enc.compare()
