#!/usr/bin/env python3
"""Stitch two vertical PNG/JPG panels into one continuous long scroll."""

from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("top", type=Path)
    parser.add_argument("bottom", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("roguelike-life-full.png"))
    parser.add_argument("--crop-top-bottom", type=int, default=0,
                        help="Pixels to crop from the bottom of the top panel before stitching.")
    parser.add_argument("--crop-bottom-top", type=int, default=0,
                        help="Pixels to crop from the top of the bottom panel before stitching.")
    args = parser.parse_args()

    top = Image.open(args.top).convert("RGB")
    bottom = Image.open(args.bottom).convert("RGB")

    if top.width != bottom.width:
        target_w = min(top.width, bottom.width)
        top = top.resize((target_w, round(top.height * target_w / top.width)), Image.Resampling.LANCZOS)
        bottom = bottom.resize((target_w, round(bottom.height * target_w / bottom.width)), Image.Resampling.LANCZOS)

    if args.crop_top_bottom:
        top = top.crop((0, 0, top.width, top.height - args.crop_top_bottom))
    if args.crop_bottom_top:
        bottom = bottom.crop((0, args.crop_bottom_top, bottom.width, bottom.height))

    out = Image.new("RGB", (top.width, top.height + bottom.height))
    out.paste(top, (0, 0))
    out.paste(bottom, (0, top.height))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.save(args.output, quality=95)
    print(args.output)


if __name__ == "__main__":
    main()
