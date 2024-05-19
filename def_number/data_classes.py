from dataclasses import dataclass, asdict


@dataclass
class PhoneProvider:
    ndc: int
    snA: int
    snB: int
    capacity: int
    provider: str
    region: str
    territory_gar: str
    inn: int

    def to_dict(self):
        return asdict(self)


@dataclass
class PhoneNumber:
    ndc: int
    sn: int

    def to_dict(self):
        return asdict(self)
