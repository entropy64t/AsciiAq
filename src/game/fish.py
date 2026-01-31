from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import tea_engine as tea

class Fish(tea.Entity):
    def __init__(self, name: str, eats: list[tea.EntityTag], colouring: list[tea.Colour], animation: tea.AnimationData, engine: Optional[tea.Engine] = None) -> None:
        super().__init__(name, [tea.EntityTag("fish")], engine)
        self.eats = eats
        self.colour = colouring
        self.animation = animation
        self.sprite = self.animation._frames_l[0]
        self.sprite_len = len(self.sprite)
        self.collider = tea.Bounds2(tea.Vector2(0, 0), tea.Vector2(self.sprite_len, 1)) + self.position
        self.add_tag(tea.EntityTag(self.name))
        
        if self.engine is not None:
            self.map_bounds = tea.Bounds2.shrink(self.engine.bounds, self.sprite_len, 0)
    
    def copy(self, pos: tea.Vector2, engine: Optional[tea.Engine] = None, id: int = 0):
        eng = engine if engine else self.engine
        cpy = Fish(
            self.name,
            self.eats,
            self.colour,
            tea.AnimationData.copy(self.animation, variation=True),
            eng
        )
        cpy.position = pos
        cpy.id = id
        return cpy
        
    def on_collision(self, other: tea.Entity):
        if self.engine is None: 
            return
        
        if other.has_any_tag(self.eats):
            # eat it
            #self.engine.log.print(f"{self.nameid()} eats {other.nameid()}")
            #self.engine.log.print(f"hash: {other.__hash__()}")
            self.engine.removes.append(other)
            #if isinstance(other, Fish):
            #    self.engine.fish.remove(other)
        #else:...
            #self.engine.log.print(f"{self.nameid()} collided with {other.nameid()}")
    
    def update_sprite(self):
        if self.direction.x < 0:
            self.animation.active_frames = self.animation._frames_l
        elif self.direction.x > 0:
            self.animation.active_frames = self.animation._frames_r
    
        self.sprite = self.animation.animate()