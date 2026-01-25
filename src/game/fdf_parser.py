from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from game import Engine
from game import AnimationData, Colour, EntityTag, Fish

def read_fdf(path: str, engine: Optional[Engine] = None):
    with open(path, 'r') as file:
        data = file.read().splitlines()
        text = file.read()
       
    name = "<error>"
    eats_data: list[str] = []
    colouring_data: list[str] = []
    animation: Optional[AnimationData] = None
    for i, line in enumerate(data):
        if line.startswith("@name"):
            name = line.removeprefix("@name").strip()
        elif line.startswith("@eats"):
            eats_data = [v.strip() for v in line.removeprefix("@eats").split(',')]
        elif line.startswith("@colouring"):
            colouring_data = [v.strip() for v in line.removeprefix("@colouring").split(',')]
        elif line.startswith("@animation"):
            animation = _parse_animation(data[i:])
        
    text.find("@")
    
    #print(name)
    #print(eats_data)
    #print(colouring_data)
    
    colouring = [Colour.from_str(c) for c in colouring_data]
    eats = [EntityTag(e) for e in eats_data]
    
    if animation is None:
        raise ValueError("Error with animation")
    
    return Fish(
        name=name,
        eats=eats,
        colouring=colouring,
        animation=animation,
        engine=engine
    )
    
def _parse_animation(data: list[str]) -> AnimationData:
    frame_count: int = 0
    frame_time: float = 0
    frames_l: list[str] = []
    frames_r: list[str] = []
    
    for i, line in enumerate(data):
        if line.startswith("@animation"):
            line_data = line.removeprefix("@animation").split()
            for param in line_data:
                if param.startswith("frames="):
                    frame_count = int(param[7:])
                elif param.startswith("time="):
                    frame_time = float(param[5:])
        elif line.startswith("@facing"):
            params = line.removeprefix("@facing").split()
            slicer = slice(i + 1, i + 1 + frame_count)
            if "left" in params:
                frames_l = data[slicer]
            elif "right" in params:
                frames_r = data[slicer]
            
    #print(frame_count)
    #print(frame_time)
    #print(frames_l)
    #print(frames_r)
                
    return AnimationData(frame_count, frames_l, frames_r, frame_time)
            
