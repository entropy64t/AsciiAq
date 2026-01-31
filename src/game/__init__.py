"""
game package: core components for the console game.
Exposes the main engine and useful helpers for easy importing.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fish import Fish
    from .fdf_parser import read_fdf
    # from .vector import Vector2, Bounds2
    from .ai import SimpleAI
    # from ...usefuls.log import Log
    from .aquarium import start

#from .input_handler import InputHandler
#from .state import GameState

__all__ = [
    "Fish",
    "read_fdf",
    "SimpleAI",
    # "Log",
    "start",
]

_import_cache = {}

def __getattr__(name: str):
    if name in _import_cache:
        print("in import cache")
        return _import_cache[name]
    
    if name == 'Fish':
        print("importing fish!")
        from .fish import Fish
        print("imported to __init__")
        _import_cache[name] = Fish
        print("set _ic")
        return Fish
    if name == 'read_fdf':
        from .fdf_parser import read_fdf
        _import_cache[name] = read_fdf
        return read_fdf
    if name == 'SimpleAI':
        from .ai import SimpleAI
        _import_cache[name] = SimpleAI
        return SimpleAI
    if name == 'start':
        from .aquarium import start
        _import_cache[name] = start
        return start
    


        