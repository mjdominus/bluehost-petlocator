
from pathlib import Path
import locator.exception
import json

class LocationStorage():
    def __init__(self, *args, **kwargs):
        pass

    def record_triple(pet, where, when, **kwargs):
        """Save a pet-where-when triple in the data store

        Args:
        pet    : The `Pet` object
        where  : `Location` object describing where the pet was
        when   : `datetime` object describing when the observation was made
        """

        raise exception.AbstractMethod("record_triple")


class LocationStorage_File(LocationStorage):
    def __init__(self, *args, **kwargs):
        self.path = kwargs.pop("path", self.default_path())
        self.fh = open(self.path, "a+")
        super().__init__(*args, **kwargs)

    def default_path(self):
        return Path("/home/mjd/bluehost/data")

    def record_triple(self, pet, where, when):
        data = { "pet_id": pet.pet_id,
                 "location_hash": where.loc_hash,
                 "timestamp": when.timestamp(),
        }
        self.append_record(json.dumps(data))

    def append_record(self, rec):
        """Store the record at the end of the file."""
        # assumes self.fh was opened in append mode
        print(rec, file=self.fh, flush=True)
