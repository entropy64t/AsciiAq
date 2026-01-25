from __future__ import annotations
from game import *

def profile(ncalls: int = 100):
    print(Colour.reset())
    fish = read_fdf("fishdef.fdf")

    clock = Clock(0)
    clock.tick_rate = 0
    bounds = Bounds2(Vector2(0, 0), Vector2(1400, 300))
    engine = Engine(bounds)
    renderer = Renderer(engine)
    
    clock += engine.update
    clock += renderer.clear
    clock += renderer.render
    
    for i in range(50000):
        engine.spawn_fish(fish, Vector2.random(bounds)).assign_ai(SimpleAI())
    
    for i in range(ncalls):
        clock.tick()
            
def main():
    print(Colour.reset())
    fish = read_fdf("fishdef.fdf")

    clock = Clock(0.2)
    bounds = Bounds2(Vector2(0, 0), Vector2(80, 20))
    engine = Engine(bounds)
    renderer = Renderer(engine)
    
    clock += engine.update
    clock += renderer.clear
    clock += renderer.render
    
    for i in range(10):
        engine.spawn_fish(fish, Vector2.random(bounds)).assign_ai(SimpleAI())

    try:
        while True:
            clock.tick()
    except KeyboardInterrupt:
        return
    
if __name__ == "__main__":
    main()
    print("exiting...")
    exit(0)