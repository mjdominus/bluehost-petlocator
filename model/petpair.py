
from datetime import datetime
from dataclasses import dataclass
import model.exception

@dataclass
class PetPair:
    """Class contains a pet ID and a collar ID, utilities for looking up
    which pet had which collar at which time
    """
    pet_id: int
    collar_id: int

    @classmethod
    def from_pet_id(cls, pet_id, when=None):
        if when is None: when = datetime.now()
        # do something to look up which collar the pet was wearing at the specified time
        # ...
        if collar_id is None:
            raise model.exception.NoMatch(f"pet_id={pet_id} collar_id={collar_id}")
        return cls(pet_id=pet_id, collar_id=collar_id)

    @classmethod
    def from_collar_id(cls, pet_id, when=None):
        if when is None: when = datetime.now()
        # do something to look up which pet was wearing this collar at the specified time
        # ...
        return cls(pet_id=pet_id, collar_id=collar_id)
