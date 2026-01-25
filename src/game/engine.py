from __future__ import annotations

from game import Fish, Entity, Clock, Vector2, Bounds2

class Engine:
    def __init__(self, bounds: Bounds2) -> None:
        self.entities: set[Entity] = set()
        self.fish: set[Fish] = set()
        self.bounds = bounds
        self.curr_id = 0
    
    def spawn_fish(self, data: Fish, position: Vector2):
        fish = data.copy(position, self, self.curr_id % 4)
        self.fish.add(fish)
        self.entities.add(fish)
        self.curr_id += 1
        return fish
        
    def update(self):
        self.animate()
        
        for entity in self.entities:
            if entity.ai == None: 
                continue
            
            #if entity.ai_num > 4:
            entity.ai.update(entity, self)
                #entity.ai_num = 0
            #else:
                #entity.ai_num += 1
            
            entity.position += entity.direction
            
    def animate(self):
        for fish in self.fish:
            fish.update_sprite()#
            
    #def assign_animations(self, clock: Clock):
    #    for entity in self.entities:
    #        if isinstance(entity, Fish):
    #            entity.animation.frame_time = clock.tick_rate
    #            #clock += entity.animation.animate