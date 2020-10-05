
from datetime import datetime
import model.exception
from dataclasses import dataclass

class Location:
    """Object contains location information."""
    lat: float                  # latitude
    lon: float                  # longitude
    alt: float = None           # altitude
