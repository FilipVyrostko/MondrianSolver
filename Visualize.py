import string
import numpy as np

from State import State


def visualize(s: State):
    arr = np.full((s.dim, s.dim), '~', dtype=str)

    for ix, v in enumerate(zip(s.rectangles, string.ascii_lowercase)):
        rec, c = v
        if ix % 2 == 0:
            c = c.upper()
        arr[rec.x:rec.x + rec.w, rec.y:rec.y + rec.h] = c

    print(f"Score >> {s.score()}\n{arr}")