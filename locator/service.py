
from datetime import datetime, timedelta

class LocationAPI():
    def __init__(self, storage):
        """Location service API object

        Knows how to talk to a location storage object
        (see `location.storage.LocationStorage` etc.)
        to store and retrieve pet location data.

        Args:
        storage: a `LocationStorage` object or similar
          to manage underlying storage
        """

        self.storage = storage

    def record_triple(self, pet, where, when=None):
        """Record a pet-where-when triple in the location store.

        Args:
        pet    : The `Pet` object
        where  : `Location` object describing where the pet was
        when   : `datetime` object describing when the observation was made
          default: current time

    Returns:
        None

    """
        if when is None:
            when = datetime.now()
        self.storage.record_triple(pet, where, when)

    def find_pet_at_time(self, pet, when, tolerance=timedelta(hours=1)):
        """Find where a pet was at a particular time.  Default time tolerance is
        one hour in each direction.

        Returns a Location object, or None if we don't have any record.
        """
        collar_id = pet.associated_collar(when)
        if collar_id is None: return None

        return self.storage.find_collar(collar_id, when, tolerance=tolerance)
