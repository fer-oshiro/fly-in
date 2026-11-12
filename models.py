from dataclasses import dataclass, field
from enum import Enum


class ZoneType(Enum):
    NORMAL = "NORMAL"
    BLOCKED = "BLOCKED"
    RESTRICTED = "RESTRICTED"
    PRIORITY = "PRIORITY"

class Role(Enum):
    START = "start"
    END = "end"
    HUB = "hub"

@dataclass(frozen=True, slots=True)
class Zone:
    name: str
    position: tuple[int, int]
    zone_type: ZoneType = ZoneType.NORMAL
    color: str | None = None
    max_drones: int = 1
    role: Role = Role.HUB

    def __post_init__(self) -> None:
        if self.max_drones < 1:
            raise ValueError("max_drones must be positive")
        if "-" in self.name:
            #nao sei ingles ;-;
            raise ValueError("")

    @property
    def capacity(self) -> int | None:
        if self.role in [Role.START, Role.END]:
            return None
        return self.max_drones

    @property
    def entry_cost(self) -> None:
        raise NotImplementedError()

    @property
    def is_blocked(self) -> bool:
        raise NotImplementedError()

@dataclass
class Connection:
    zone_a: Zone
    zone_b: Zone
    key: str
    max_link_capacity: int = 1

    def other(self, zone: Zone) -> Zone:
        raise NotImplementedError()

    def connects(self, a, b) -> bool:
        raise NotImplementedError()


@dataclass(eq=False)
class Map:
    nb_drones: int = 0
    zones: dict[str, Zone] = field(default_factory=dict)
    connections: list[Connection] = field(default_factory=list)
    adjacency: dict[Zone, list[Connection]] = field(default_factory=dict)
    _connections_by_pair: dict[frozenset[str], Connection] = field(
        default_factory=dict
    )
    start: Zone | None = None
    end: Zone | None = None
