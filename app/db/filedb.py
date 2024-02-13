import json
import typing

from app.models.product import Product

def products_list() -> typing.List[typing.Any]:
    file_path = "../../products.data"
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        if isinstance(data, list):  # Check if the JSON data is already a list
            return [Product(**item) for item in data]  # Convert directly to models
        else:
            raise ValueError("Invalid JSON format: Expected a list.")

    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError(f"Error reading JSON data: {e}")
    except IOError as e:
        raise IOError(f"Error opening file: {e}")

    return []