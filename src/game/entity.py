from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from game import Engine, AIBase, Colour
    
from game import Vector2

class EntityTag:
    def __init__(self, tag_name: str) -> None:
        self.tag_name = tag_name.upper().strip()
         
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, EntityTag): 
            return False
        
        return self.tag_name == value.tag_name
    
    def __repr__(self) -> str:
        return self.tag_name
    
class Entity(ABC):
    sprite: str = "<nosprite>"
    colour: list[Colour] = []
    def __init__(self, name: str, tags: list[EntityTag], engine: Optional[Engine] = None) -> None:
        self.name = name
        self.tags = tags
        self.engine = engine
        self.position = Vector2()
        self.direction = Vector2()
        self.ai = None
        self.ai_num = 0
        
    def add_tag(self, tag: EntityTag):
        self.tags.append(tag)
        
    def has_tag(self, tag: EntityTag | str):
        if isinstance(tag, EntityTag):
            return tag in self.tags
        else:
            return EntityTag(tag) in self.tags
        
    def has_any_tag(self, tags: Iterable[EntityTag | str]):
        return any(self.has_tag(t) for t in tags)
    
    def move_to(self, nx: int, ny: int):
        self.x = nx
        self.y = ny
        
    def assign_ai(self, ai: AIBase):
        self.ai = ai
        
    def update(self):    
        if self.ai == None: 
            return
        
        if self.ai_num > 4:
            self.ai.update(self, self.engine)
            self.ai_num = 0
        else:
            self.ai_num += 1
        
        self.position += self.direction
        
    @abstractmethod
    def on_collision(self, other: Entity):
        "Abstract method for managing collisions" 