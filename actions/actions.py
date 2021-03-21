# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

import requests
from pony.orm import db_session

from db import City


class ActionResetAllSlots(Action):
    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionLookupCity(Action):
    def name(self) -> Text:
        return "action_lookup_city"

    def run(self, dispatcher, tracker, domain):
        locations = tracker.get_slot('location')
        if isinstance(locations, str):
            locations = [locations]
        for location in locations:
            city = location[0].upper() + location[1:]
            with db_session:
                city = City.select(lambda x: x.name == city).first()
                if city is None:
                    dispatcher.utter_message(text=f'Sorry, I don\'t know that location - \"{location}\", give another try?')
                    return []
                response = self.make_msg(self.get_info(city))
                dispatcher.utter_message(text=response)

    def get_info(self, city):
        url = "https://api.openweathermap.org/data/2.5/weather"
        file = open('openweather.api', 'r')
        api_token = file.read().replace('\n', '')
        file.close()
        payload = {
            'id': city.openweather_cityid,
            'appid': api_token,
            'units': 'metric',
        }
        response = requests.get(url, params=payload)
        if response.ok:
            return response.json()
        return None

    def make_msg(self, d: Dict[Text, Any]):
        if d is None:
            return 'Sorry, smth wrong with getting openweathermap info'
        temp = d['main']['temp']
        description = d['weather'][0]['description']
        return f'Weather in {d["name"]} now is: {description}, {temp} C'
