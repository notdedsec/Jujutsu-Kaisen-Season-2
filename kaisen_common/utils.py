from typing import List, Tuple

from vapoursynth import VideoNode
from vstools import core, depth, get_depth, get_y, iterate, replace_ranges
from vsmasktools import squaremask
from awsmfunc import bbmod
from rekt import rektlvls


def letterbox_fix(clip: VideoNode, src: VideoNode, height: int, ranges: List[Tuple[int, int]], offset: int = 2, shift: int = 0, rekt_args = {}, bb_args = {}):
    src = depth(src, get_depth(clip))

    src_shift = core.resize.Bicubic(src, src_top=shift)
    src_shift = replace_ranges(src, src_shift, ranges)

    clip_shift = core.resize.Bicubic(clip, src_top=shift)
    clip_shift = replace_ranges(clip, clip_shift, ranges)

    mask_a = squaremask(clip, clip.width, offset, 0, height)
    mask_b = squaremask(clip, clip.width, offset, 0, clip.height - height - offset)
    border_mask = core.std.Expr([mask_a, mask_b], 'x y max')
    border_restore = core.std.MaskedMerge(clip_shift, src_shift, border_mask)

    crop = border_restore.std.Crop(top=height, bottom=height)
    edge_fix = crop

    if rekt_args:
        edge_fix = rektlvls(edge_fix, **rekt_args)

    if bb_args:
        edge_fix = bbmod(edge_fix, **bb_args)

    revert_crop = edge_fix.std.AddBorders(top=height, bottom=height)
    revert_shift = core.resize.Bicubic(revert_crop, src_top=-shift)
    fixed = replace_ranges(clip, revert_shift, ranges)

    return fixed


def circle_mask(clip: VideoNode, bzr: int = 4444, inflate: int = 4):
    mask = get_y(clip).std.Binarize(bzr)
    mask = iterate(mask, core.std.Inflate, inflate)

    return mask

