from __future__ import annotations
# from game import *
from game.aquarium import start, read_fdf
import argparse
import random

import tea_engine as tea

def randomvec(bounds: tea.Bounds2):
    x = random.randint(bounds.tl.x, bounds.br.x)
    y = random.randint(bounds.tl.y, bounds.br.y)
    return tea.Vector2(x, y)

def profile(ncalls: int = 100):
    print(tea.Colour.reset())
    fish = read_fdf("fish/fishdef.fdf")

    clock = tea.Clock(0)
    clock.tick_rate = 0
    bounds = tea.Bounds2(tea.Vector2(0, 0), tea.Vector2(1300, 300))
    engine = tea.Engine(bounds)
    renderer = tea.Renderer(engine)
    
    clock += engine.update
    clock += renderer.clear
    clock += renderer.render
    
    for i in range(50000):
        engine.spawn(fish, randomvec(bounds)).assign_ai(tea.SimpleAI())
    print("fish done")
    
    for i in range(ncalls):
        clock.tick()
            
def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("nfish", help="Number of initial fish", metavar="<nfish>")
    parser.add_argument("-t", "--tick", help="Specify tick rate. Default: 250ms", default=0.25, metavar="<tick>")
    parser.add_argument("--log", action="store_true", help="If set, enables logging", default=False)
    parser.add_argument("-W", help="Width of aquarium. Default: 60", default=60, metavar="<width>")
    parser.add_argument("-H", help="Height of aquarium. Default: 25", default=25, metavar="<height>")
    
    args = parser.parse_args()
    print(args)
    
    start(int(args.nfish), args.log, tea.Vector2(int(args.W), int(args.H)), float(args.tick))
    
if __name__ == "__main__":
    main()
    print("exiting...")
    exit(0)