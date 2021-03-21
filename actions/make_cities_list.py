import json
import yaml
from pprint import pprint


def run():
    with open('city.list.json', 'r') as file:
        whole_file = file.read()
    file = open('training.yml', 'a')
    for i, item in enumerate(json.loads(whole_file)):
        if item['country'] == 'UA' and item['name'] != "-":
            if i % 10 == 0:
                file.write(f'- weather [{item["name"]}](location)\n')
            # file.write(f'- {item["name"]}\n')
    file.close()
    print('done')


if __name__ == "__main__":
    run()
