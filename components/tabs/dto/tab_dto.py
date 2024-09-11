from dataclasses import dataclass

@dataclass
class TabDTO:

    name: str
    tcg: str
    expansion: str
    price_difference_type: int
    price_difference: str
    
    maximum_threshold: str