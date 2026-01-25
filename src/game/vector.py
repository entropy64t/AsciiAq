from __future__ import annotations

_dirs = [
    (dx, dy)
    for dx in (-1, 0, 1)
    for dy in (-1, 0, 1)
    if not (dx == 0 and dy == 0)  # exclude no-move
]

import random

class Vector2:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, other: Vector2):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vector2):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __repr__(self) -> str:
        return f"Vec2({self.x}, {self.y})"
    
    @staticmethod
    def random_dir(vec: Vector2, pos: Vector2, bounds: Bounds2):
        """Random vector `new` with `lenght(vec - new) = 1` and `pos + new in bounds`"""
        vx, vy = vec.x, vec.y
        px, py = pos.x, pos.y

        fallback = None
        valid = []

        for dx, dy in _dirs:
            nx = px + dx
            ny = py + dy

            # inline bounds check (WAY faster than __contains__)
            if not (bounds._tl.x <= nx <= bounds._br.x and bounds._tl.y <= ny <= bounds._br.y):
                continue

            if fallback is None:
                fallback = (dx, dy)

            # (new - vec).length2 == 1
            ddx = dx - vx
            ddy = dy - vy
            if ddx * ddx + ddy * ddy == 1:
                valid.append((dx, dy))

        if valid:
            dx, dy = random.choice(valid)
        elif fallback:
            dx, dy = fallback
        else:
            return Vector2(0, 0)

        return Vector2(dx, dy)
    
    @staticmethod
    def random(bounds: Bounds2):
        x = random.randint(bounds._tl.x, bounds._br.x)
        y = random.randint(bounds._tl.y, bounds._br.y)
        return Vector2(x, y)
    
    @property
    def length2(self):
        return self.x * self.y + self.y * self.y
    
    @property
    def length(self):
        return float(self.length2) ** 0.5
        
class Bounds2:
    def __init__(self, top_left: Vector2, bottom_right: Vector2) -> None:
        self._tl = top_left
        self._br = bottom_right
        
    def __contains__(self, point: Vector2):
        return self._tl.x <= point.x <= self._br.x and self._tl.y <= point.y <= self._br.y