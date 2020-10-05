
from dataclasses import dataclass

@dataclass
class Pet:
    """Backed by `PET` table in database"""
    pet_id: int
    name: str
