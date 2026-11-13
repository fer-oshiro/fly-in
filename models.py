from dataclasses import dataclass, field
from enum import Enum


class ZoneType(Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


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
        if not self.name.strip():
            raise ValueError("zone name must not be empty")
        if "-" in self.name:
            raise ValueError("zone names cannot contain dashes")
        if self.role not in (Role.START, Role.END) and self.max_drones < 1:
            raise ValueError("max_drones must be positive")

    @property
    def capacity(self) -> int | None:
        if self.role in (Role.START, Role.END):
            return None
        return self.max_drones

    @property
    def entry_cost(self) -> int:
        if self.zone_type == ZoneType.RESTRICTED:
            return 2
        return 1

    @property
    def is_blocked(self) -> bool:
        return self.zone_type == ZoneType.BLOCKED


@dataclass(eq=False)
class Connection:
    zone_a: Zone
    zone_b: Zone
    max_link_capacity: int = 1

    @property
    def key(self) -> str:
        a, b = sorted((self.zone_a.name, self.zone_b.name))
        return f"{a}-{b}"

    @property
    def pair(self) -> frozenset[str]:
        return frozenset((self.zone_a.name, self.zone_b.name))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Connection):
            return NotImplemented
        return self.pair == other.pair

    def __hash__(self) -> int:
        return hash(self.pair)


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
