
from datetime import datetime

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
