from utilities.schema_validator import SchemaValidator

def test_account_schema():

    response = {
        "id":"123",
        "name":"Subhendu",
        "balance":50000
    }

    SchemaValidator.validate_json(
        response,
        "schemas/account_schema.json"
    )

    print("Schema validation successful")