import json
import yaml
from pprint import pprint
from pony.orm import *


from db import City


def run():
    db = Database()

    with db_session:
        city = City.select(lambda x: x.name == 'Kyiv').first()
        print(city)


if __name__ == "__main__":
    run()
