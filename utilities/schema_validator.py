from jsonschema import validate
import json

class SchemaValidator:

    @staticmethod
    def validate_json(response, schema_file):

        with open(schema_file) as file:
            schema = json.load(file)

        validate(
            instance=response,
            schema=schema
        )