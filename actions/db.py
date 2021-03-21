from pony.orm import *

db = Database()


class City(db.Entity):
    name = Required(str)
    openweather_cityid = Required(int)

    def __str__(self):
        return f'{self.name}: {self.openweather_cityid}'


db.bind(provider='sqlite', filename='db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
