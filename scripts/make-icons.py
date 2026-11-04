#!/usr/bin/env python3
"""Rasterize the simple favicon monogram with standard-library PNG output."""
from pathlib import Path
import math
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]
POINTS = [(18, 46), (18, 19), (32, 35), (46, 19), (46, 46)]


def distance(x, y, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = max(0, min(1, ((x-a[0])*dx + (y-a[1])*dy)/(dx*dx+dy*dy)))
    return math.hypot(x-a[0]-t*dx, y-a[1]-t*dy)


def pixel(x, y):
    # Rounded 64-unit square, matching favicon.svg exactly.
    cx, cy = max(14, min(50, x)), max(14, min(50, y))
    if (x-cx)**2 + (y-cy)**2 > 14**2:
        return (0, 0, 0, 0)
    if any(distance(x, y, a, b) <= 3 for a, b in zip(POINTS, POINTS[1:])):
        return (247, 247, 243, 255)
    return (23, 63, 53, 255)


def png(size):
    samples = 4 if size <= 48 else 2
    raw = bytearray()
    for row in range(size):
        raw.append(0)
        for col in range(size):
            values = [pixel((col+(sx+.5)/samples)*64/size, (row+(sy+.5)/samples)*64/size) for sy in range(samples) for sx in range(samples)]
            alpha = sum(p[3] for p in values)
            rgb = [round(sum(p[channel]*p[3] for p in values)/alpha) if alpha else 0 for channel in range(3)]
            raw.extend((*rgb, round(alpha/len(values))))
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind+data) & 0xffffffff)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")


if __name__ == "__main__":
    for size, filename in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
        (ROOT / "assets/icons" / filename).write_bytes(png(size))
    sizes = [16, 32, 48]
    images = [png(size) for size in sizes]
    offset = 6 + 16*len(sizes)
    directory = bytearray(struct.pack("<HHH", 0, 1, len(sizes)))
    for size, data in zip(sizes, images):
        directory.extend(struct.pack("<BBBBHHII", size, size, 0, 0, 1, 32, len(data), offset))
        offset += len(data)
    (ROOT / "favicon.ico").write_bytes(bytes(directory) + b"".join(images))
    print("Generated SVG-matched PNG icons and multi-size favicon.ico.")
