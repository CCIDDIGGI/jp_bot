
from enum import Enum

class MtgGenerics(Enum):
    id = 1
    game_id = 1
    display_name = "Magic: the Gathering"
    name = "Magic: the Gathering"


class PkmGenerics(Enum):
    id = 5
    game_id = 5
    display_name = "Pokémon"
    name = "Pokémon"

class Conditions(Enum):
    near_mint = 1
    slightly_played = 2
    moderately_played = 3
    played = 4
    poor = 5 
    
