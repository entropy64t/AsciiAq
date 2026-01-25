from __future__ import annotations
from typing import TYPE_CHECKING
import sys

if TYPE_CHECKING:
    from game import Engine, Entity
from game import Fish, Vector2, Colour

ansi_rgb = {}

class Renderer:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        
        self.w = self.engine.bounds._br.x - self.engine.bounds._tl.x + 2
        self.h = self.engine.bounds._br.y - self.engine.bounds._tl.y + 2
        self.buffer = [[" "] * self.w for j in range(self.h)]
        self.clr_buffer = [[(0, 0, 0)] * self.w for j in range(self.h)]
        self.bord_w = ["#"] * self.w
        self.bord_h = ["#"] * self.h
        self.cbord_w = [(100, 200, 255)] * self.w
        self.cbord_h = [(100, 200, 255)] * self.h
    
    def render(self):
        self.clear()

        for entity in self.engine.entities:
            x = entity.position.x
            y = entity.position.y

            if not (0 <= y < self.h):
                continue

            spr = entity.sprite   # MUST be cached!
            clr = entity.colour
            row = self.buffer[y + 1]
            clrow = self.clr_buffer[y + 1]

            for i, ch in enumerate(spr):
                xi = x + i + 1
                if 0 <= xi < self.w:
                    row[xi] = ch
                    clrow[xi] = clr[i].tpl
                    
        self.buffer[0][:] = self.bord_w
        self.buffer[-1][:] = self.bord_w
        self.clr_buffer[0][:] = self.cbord_w
        self.clr_buffer[-1][:] = self.cbord_w
        
        for i in range(self.h):
            self.buffer[i][0] = "#"
            self.clr_buffer[i][0] = (100, 200, 255)
            self.buffer[i][-1] = "#"
            self.clr_buffer[i][-1] = (100, 200, 255)

        out = []
        out.append("\x1b[H")

        current_color = (-1, -1, -1)

        for y in range(self.h):
            row = self.buffer[y]
            crow = self.clr_buffer[y]

            for x in range(self.w):
                c = crow[x]
                if c != current_color:
                    if c not in ansi_rgb:
                        ansi_rgb[c] = f"\x1b[38;2;{c[0]};{c[1]};{c[2]}m"
                    out.append(ansi_rgb[c])
                    current_color = c
                out.append(row[x])

            out.append("\x1b[0m\n")
            current_color = (-1, -1, -1)

        sys.stdout.write("".join(out))
        sys.stdout.flush()
        
    def clear(self):
        blank = [" "] * self.w
        bclr = [(0, 0, 0)] * self.w
        for y in range(self.h):
            self.buffer[y][:] = blank
            self.clr_buffer[y][:] = bclr