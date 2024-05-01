import json
import typing

from fastapi import HTTPException

from app.models.product import Product

def products_list() -> typing.List[typing.Any]:
    file_path = "./products.data"
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
    

def card_products_list() -> typing.List[typing.Any]:
    file_path = "./card.data"
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


def remove_from_card(id: str) -> bool:
    file_path = "./card.data"
    
    products = card_products_list()  # Load existing products
    # Find the product to remove
    index = next((i for i, product in enumerate(products) if product.id == id), None)
    if index is None:
        return True  # Product not found
    
    # Remove the product from the list
    del products[index]
        
    # Save the updated product list to the file
    try:
        with open(file_path, "w") as json_file:
            product_dict = [
                {
                    **product.dict(),
                    "created_at": product.created_at.isoformat(),
                    "updated_at": product.updated_at.isoformat(),
                }
                for product in products
            ]
            json.dump(product_dict, json_file, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")

    return True  # Product removed successfully


def add_to_card(id: str) -> bool:
    file_path = "./card.data"
    
    products = products_list()  # Load existing products
    card_products = card_products_list()  # Load existing products
    # Find the product to remove
    index = next((i for i, product in enumerate(products) if product.id == id), None)
    if index is None:
        return True  # Product not found
    
    # Add to the card
    card_products.append(products[index])
        
    # Save the updated product list to the file
    try:
        with open(file_path, "w") as json_file:
            product_dict = [
                {
                    **product.dict(),
                    "created_at": product.created_at.isoformat(),
                    "updated_at": product.updated_at.isoformat(),
                }
                for product in card_products
            ]
            json.dump(product_dict, json_file, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")

    return True  # Product added to the card successfully


def checkout() -> bool:
    file_path = "./card.data"
    
    products = card_products_list()  # Load existing products
    
    products.clear()
        
    # Save the updated product list to the file
    try:
        with open(file_path, "w") as json_file:
            product_dict = [
                {
                    **product.dict(),
                    "created_at": product.created_at.isoformat(),
                    "updated_at": product.updated_at.isoformat(),
                }
                for product in products
            ]
            json.dump(product_dict, json_file, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")

    return True  # Checkout successfully
