from __future__ import annotations

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from game import Colour, AnimationData, Engine
from game import EntityTag, Entity, Vector2

class Fish(Entity):
    def __init__(self, name: str, eats: list[EntityTag], colouring: list[Colour], animation: AnimationData, engine: Optional[Engine] = None) -> None:
        super().__init__(name, [EntityTag("fish")], engine)
        self.eats = eats
        self.colour = colouring
        self.animation = animation
        self.sprite = self.animation._frames_l[0]
    
    def copy(self, pos: Vector2 = Vector2(0, 0), engine: Optional[Engine] = None, ai_num: int = 0):
        eng = engine if engine else self.engine
        cpy = Fish(
            self.name,
            self.eats,
            self.colour,
            self.animation,
            eng
        )
        cpy.position = pos
        cpy.ai_num = ai_num
        return cpy
        
    def on_collision(self, other: Entity):
        if other.has_any_tag(self.eats):
            # eat it
            print(f"{self.name} eats {other.name}")
        else:
            print(f"{self.name} collided with {other.name}")
    
    def update_sprite(self):
        self.animation.animate()
        frame = self.animation._frame

        if self.direction.x < 0:
            self.sprite = self.animation._frames_l[frame]
        elif self.direction.x > 0:
            self.sprite = self.animation._frames_r[frame]