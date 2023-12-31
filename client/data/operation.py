from dataclasses import dataclass


@dataclass
class Operation:
    id: int
    customer: str
    user: str
    material: str
    material_from_storage: bool
    width: float
    height: float
    thickness: float
    work_duration: float
    amount: float
    laser_cut: bool
    is_active: bool
    date: str

