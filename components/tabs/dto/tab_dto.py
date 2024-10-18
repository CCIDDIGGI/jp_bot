from dataclasses import dataclass

@dataclass
class TabDTO:

    id: str
    name: str
    tcg: str
    expansion: str
    exp_id: int
    price_difference_type: int
    price_difference: str
    condition_comparison: dict
    maximum_threshold: str

    