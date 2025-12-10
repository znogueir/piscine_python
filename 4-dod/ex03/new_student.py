import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """ Student class """

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: int = field(init=False)

    def __post_init__(self):
        """Init non instanciable values"""
        self.login = self.name[0] + self.surname
        self.id = generate_id()
