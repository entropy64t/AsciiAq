"""
game package: core components for the console game.
Exposes the main engine and useful helpers for easy importing.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .engine import Engine
    from .renderer import Renderer
    from .clock import Clock
    from .fish import Fish
    from .fdf_parser import read_fdf
    from .graphic_things import AnimationData, Colour, FgPresets
    from .entity import Entity, EntityTag
    from .vector import Vector2, Bounds2
    from .ai import AIBase, SimpleAI

#from .input_handler import InputHandler
#from .state import GameState

__all__ = [
    "Engine",
    "Renderer",
    "Clock",
    "Fish",
    "read_fdf",
    "AnimationData",
    "Colour",
    "EntityTag",
    "FgPresets",
    "Vector2",
    "Entity",
    "AIBase",
    "SimpleAI",
    "Bounds2",
    #"InputHandler",
    #"GameState",
]

_import_cache = {}

def __getattr__(name: str):
    if name in _import_cache:
        return _import_cache[name]
    
    if name == 'Engine':
        from .engine import Engine
        _import_cache[name] = Engine
        return Engine
    if name == 'Renderer':
        from .renderer import Renderer
        _import_cache[name] = Renderer
        return Renderer
    if name == 'Clock':
        from .clock import Clock
        _import_cache[name] = Clock
        return Clock
    if name == 'Fish':
        from .fish import Fish
        _import_cache[name] = Fish
        return Fish
    if name == 'read_fdf':
        from .fdf_parser import read_fdf
        _import_cache[name] = read_fdf
        return read_fdf
    if name == 'AnimationData':
        from .graphic_things import AnimationData
        _import_cache[name] = AnimationData
        return AnimationData
    if name == 'Colour':
        from .graphic_things import Colour
        _import_cache[name] = Colour
        return Colour
    if name == 'EntityTag':
        from .entity import EntityTag
        _import_cache[name] = EntityTag
        return EntityTag
    if name == 'Entity':
        from .entity import Entity
        _import_cache[name] = Entity
        return Entity
    if name == 'FgPresets':
        from .graphic_things import FgPresets
        _import_cache[name] = FgPresets
        return FgPresets
    if name == 'Vector2':
        from .vector import Vector2
        _import_cache[name] = Vector2
        return Vector2
    if name == 'Bounds2':
        from .vector import Bounds2
        _import_cache[name] = Bounds2
        return Bounds2
    if name == 'AIBase':
        from .ai import AIBase
        _import_cache[name] = AIBase
        return AIBase
    if name == 'SimpleAI':
        from .ai import SimpleAI
        _import_cache[name] = SimpleAI
        return SimpleAI
    


        