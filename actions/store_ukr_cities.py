import json
from pony.orm import *


def run():
    db = Database()

    class City(db.Entity):
        name = Required(str)
        openweather_cityid = Required(int)

        def __str__(self):
            return str(self.openweather_cityid)

    db.bind(provider='sqlite', filename='db.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)

    with open('city.list.json', 'r') as file:
        whole_file = file.read()
    with db_session:
        for item in json.loads(whole_file):
            if item['country'] == 'UA' and item['name'] != "-":
                city = City(name=item['name'],
                            openweather_cityid=int(item['id']))


if __name__ == "__main__":
    run()
