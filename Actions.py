from typing import Tuple, Optional

from Rectangle import Rectangle
from State import State

# Check if results of an action yields valid state
def _is_valid(s: State, r1: Rectangle, r2: Rectangle) -> bool:
    r1x, r1y = r1.get_dims()
    r2x, r2y = r2.get_dims()

    _set = set(map(lambda r: r.get_dims(), s.rectangles))

    return (r1x, r1y) not in _set and (r1y, r1x) not in _set and \
           (r2x, r2y) not in _set and (r2y, r2x) not in _set and \
           (r1x, r1y) != (r2x, r2y) and (r1x, r1y) != (r2y, r2x)

# Split rectangle horizontally
def split_horizontal(r: Rectangle, ratio: Tuple[int, int]) -> Optional[Tuple[Rectangle, Rectangle]]:
    a, b = ratio

    if r.h < 3 or a + b != r.h:
        return None

    r1 = Rectangle(r.x, r.y, r.w, a)
    r2 = Rectangle(r.x, r.y + a, r.w, b)

    return (r1, r2)

# Split rectangle vertically
def split_vertical(r: Rectangle, ratio: Tuple[int, int]) -> Optional[Tuple[Rectangle, Rectangle]]:
    a, b = ratio

    if r.w < 3 or a + b != r.w:
        return None

    r1 = Rectangle(r.x, r.y, a, r.h)
    r2 = Rectangle(r.x + a, r.y, b, r.h)

    return (r1, r2)

# Calculate maximum utility (score) of the state 'depth' moves ahead
def _max_utility(s: State, depth: int) -> int:
    if depth <= 0:
        return s.score()

    r = max(s.rectangles, key=lambda r: r.area)

    best_score = s.score()

    for a, b in s.ratios:
        res_v = split_vertical(r, (a, b))

        if res_v:
            r1, r2 = res_v
            if _is_valid(s, r1, r2):
                s.update(r, r1, r2)
                best_score = min(best_score, _max_utility(s, depth - 1))
                s.restore(r, r1, r2)

        # if width and height of the rectangle we are splitting are the same
        # then splitting it horizontally is the same as vertically
        # and so makes it a useless branch to explore
        if r.w != r.h:
            res_h = split_horizontal(r, (a, b))

            if res_h:
                r1, r2 = res_h
                if _is_valid(s, r1, r2):
                    s.update(r, r1, r2)
                    best_score = min(best_score, _max_utility(s, depth - 1))
                    s.restore(r, r1, r2)

    return best_score

# Calculate next action to take
def next_action(s: State, depth: int) -> Optional[Tuple[Rectangle, Rectangle, Rectangle]]:
    actions = []

    r = max(s.rectangles, key=lambda r: r.area)

    for a, b in s.ratios:
        res_v = split_vertical(r, (a, b))
        if res_v:
            r1, r2 = res_v
            if _is_valid(s, r1, r2):
                s.update(r, r1, r2)
                actions.append(((r, r1, r2), _max_utility(s, depth - 1)))
                s.restore(r, r1, r2)

        if r.w != r.h:
            res_h = split_horizontal(r, (a, b))
            if res_h:
                r1, r2 = res_h
                if _is_valid(s, r1, r2):
                    s.update(r, r1, r2)
                    actions.append(((r, r1, r2), _max_utility(s, depth - 1)))
                    s.restore(r, r1, r2)

    if actions:
        _best = min(actions, key=lambda x: x[1])

        return _best[0] if _best[1] < s.score() else None
    else:
        return None
