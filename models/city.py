#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city in this console.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""