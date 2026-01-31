from __future__ import annotations
import random
import tea_engine as tea
from game.fdf_parser import read_fdf
            
def randomvec(bounds: tea.Bounds2):    
    x = random.randint(bounds.tl.x, bounds.br.x)
    y = random.randint(bounds.tl.y, bounds.br.y)
    return tea.Vector2(x, y)
            
def start(n_fish: int, logging: bool, size: tea.Vector2, tick: float):
    print(tea.Colour.reset())

    clock = tea.Clock(tick)
    bounds = tea.Bounds2(tea.Vector2(0, 0), size)
    engine = tea.Engine(bounds, logging=logging)
    renderer = tea.Renderer(engine)
    
    fish = read_fdf("fish/fishdef.fdf", engine)
    tp = read_fdf("fish/predator.fdf", engine)
    
    clock += engine.update
    clock += renderer.clear
    clock += renderer.render
    
    fl = [fish]
    
    for i in range(n_fish):
        f = random.choice(fl)
        engine.spawn(f, randomvec(fish.map_bounds)).assign_ai(tea.SimpleAI())
        
    # engine.spawn_fish(tp, Vector2(5, 5)).assign_ai(SimpleAI())

    try:
        while True:
            clock.tick()
    except KeyboardInterrupt:
        return