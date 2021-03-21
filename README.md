# openweather map Rasa chatbot for UA, exploration

This is Rasa chatbot that can tell current weather info taken from
openweathermap. It recognizes Latin names of Ukrainian (UA) cities.

## see demo screens
- screen1.jpg
- screen2.jpg

## Install dependencies

Run:
```bash
pip install -r requirements.txt
```

## Add openweathermap API key
Provide API key string in file actions/openweather.api

## Run the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions
```

Then talk to your bot by running:
```
rasa shell --debug
```

Note that `--debug` mode will produce a lot of output meant to help you understand how the bot is working
under the hood. To simply talk to the bot, you can remove this flag.


## Overview of the files

`data/core.md` - contains stories

`data/nlu.md` - contains NLU training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble


## Things you can ask the bot

1. Ask for current weather or "forecast" in Ukrainian cities (UA), in Latin typing
2. Say hi
3. Ask bot what it can do
4. Express yourself...

## Possible further development

Use duckling to recognize datetime entities.
Improve chat flow and scenarios, add locations by name and coordinates, plug in something like Google's places autocomplete to recognize more locations.