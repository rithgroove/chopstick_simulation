from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class UpgradeCategory(Enum):
    TRAIT = "trait"
    ABILITY = "ability"
    ITEM = "item"


class UpgradeType(Enum):
    PASSIVE = "passive"
    ACTIVE = "active"
    REACTION = "reaction"


@dataclass
class Upgrade:
    id: str
    name: str

    category: UpgradeCategory
    type: UpgradeType

    # stat modifiers (passive)
    health_bonus: int = 0
    move_bonus: int = 0
    melee_accuracy_bonus: int = 0
    ranged_accuracy_bonus: int = 0
    evasion_bonus: int = 0
    armor_bonus: int = 0

    # requirements
    required_upgrades: Optional[List[str]] = None