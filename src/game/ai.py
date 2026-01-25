from __future__ import annotations

from abc import ABC, abstractmethod

from typing import Optional

from game import Entity, Engine, Vector2

class AIBase(ABC):
    @abstractmethod
    def update(self, entity_tied: Entity, engine: Optional[Engine]):
        "do nothing"
        
class SimpleAI(AIBase):
    def update(self, entity_tied: Entity, engine: Optional[Engine]):
        if engine is None:
            raise ValueError("SimpleAI needs access to Engine")
        
        d = Vector2.random_dir(entity_tied.direction, entity_tied.position, engine.bounds)
                        
        entity_tied.direction = d