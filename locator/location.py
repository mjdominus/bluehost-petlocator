
from datetime import datetime

class LocationService():
    def __init__(self, storage):
        self.storage = storage

    def record_triple(self, pet_id, where, when=None):
        """Record a pet-where-when triple in the location store.

        Args:
        pet_id (int): The pet
        where  (:obj:`location`): Where the pet was located
        when   (:obj:`datetime`, optional): The time at which the pet was located
          default: current time

    Returns:
        None

    Raises
        XXX SOMETHING
    """
        if when is None:
            when = datetime.now()

class LocationFileStorageService(LocationService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
