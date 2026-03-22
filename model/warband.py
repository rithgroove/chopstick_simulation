from dataclasses import dataclass, field
from typing import List
from models.unit import Unit


@dataclass
class Warband:
    id: str

    gold: int = 0
    units: List[Unit] = field(default_factory=list)

    def add_unit(self, unit: Unit):
        self.units.append(unit)

    def remove_unit(self, unit: Unit):
        self.units.remove(unit)