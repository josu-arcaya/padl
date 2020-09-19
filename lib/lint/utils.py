import json
import yaml
from collections import namedtuple
from jsonschema import validate

class Padl:

    def __init__(self, input_data):
        schema_location = 'lint/resources/config_schema_v1.0.json'
        with open(schema_location, 'r') as input_data_file:
            self.schema = json.loads(input_data_file.read())
        self.padl = self.parse(input_data)

    def parse(self, input_data):
        padl = yaml.load(input_data, Loader=yaml.FullLoader)
        return padl

    def validate(self):
        validate(instance=self.padl, schema=self.schema)
        return True

    def object_hook(self, d):
        return namedtuple('X', d.keys())(*d.values())

    def file2obj(self):
        return json.loads(json.dumps(self.padl), object_hook=self.object_hook)