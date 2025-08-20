from dataclasses import dataclass
import random

@dataclass
class Agent:
    id:int
    x:int=0
    def step(self):
        self.x+=random.choice([-1,1])
