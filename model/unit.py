from dataclasses import dataclass, field
from typing import List


@dataclass
class Unit:
    id: str
    team: int

    # position
    x: int
    y: int

    # stats (base)
    max_hp: int = 3
    current_hp: int = 3
    move: int = 1
    melee_accuracy: int = 0
    ranged_accuracy: int = 0
    evasion: int = 0
    armor: int = 0

    # progression
    level: int = 1

    # upgrades
    upgrades: List[str] = field(default_factory=list)

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def max_upgrade_slots(self) -> int:
        return 5 + (self.level - 1)

    def can_add_upgrade(self) -> bool:
        return len(self.upgrades) < self.max_upgrade_slots()