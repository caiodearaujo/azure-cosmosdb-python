import logging
from typing import Dict
from .lib import DataBaseClient

PARAMETERS = dict(
    CONTAINER_NAME='<container_name>',
    PARTITION_KEY = '</partition_key>'
)

DATABASE: DataBaseClient = DataBaseClient(PARAMETERS['CONTAINER_NAME'],
                                          PARAMETERS['PARTITION_KEY'])

def create_item(item: Dict) -> Dict:
    """
    Create an item in the database
    """
    return DATABASE.create_item_cosmosdb(item)

def upsert_item(item: Dict) -> Dict:
    """
    Upsert an item in the database
    """
    return DATABASE.upsert_item_cosmosdb(item)

def delete_item(item: Dict) -> Dict:
    """
    Delete an item in the database
    """
    return DATABASE.delete_item_cosmosdb(item)

def get_item(item: Dict) -> Dict:
    """
    Get an item in the database
    """
    return DATABASE.get_item_cosmosdb(item)

def query_items(query: str) -> Dict:
    """
    Query items in the database
    """
    return DATABASE.query_items_cosmosdb(query)



