from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    name: str
    mobile: str
    mobile2: str
    company: str
    rating: int
    comment: str
