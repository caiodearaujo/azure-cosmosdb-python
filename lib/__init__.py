import os, json
from typing import Dict, Iterable
from azure.cosmos import (CosmosClient,
                          PartitionKey,
                          ContainerProxy,
                          DatabaseProxy)

SETTINGS = dict(
    HOST = os.getenv('COSMOSDB_HOST'),
    MASTER_KEY = os.getenv('COSMOSDB_MASTER_KEY'),
    DATABASE_ID = os.getenv('COSMOSDB_DATABASE_ID')
)

class DataBaseClient():
    
    def __init__(self, container_id, partition_key) -> None:
        super().__init__()
        self.container_id = container_id
        self.partition_key = partition_key
        
        
    def get_cosmosdb_client(self) -> CosmosClient:
        client = CosmosClient(
            endpoint_url=SETTINGS['HOST'],
            auth={'masterKey': SETTINGS['MASTER_KEY']}
        )
        return client
    
    def get_cosmosdb_database(self) -> DatabaseProxy:
        client = self.get_cosmosdb_client()
        database = client.create_database_if_not_exists(SETTINGS['DATABASE_ID'])
        return database
    
    def get_cosmosdb_container(self) -> ContainerProxy:
        database = self.get_cosmosdb_database()
        container = database.create_container_if_not_exists(
            id=self.container_id,
            partition_key=PartitionKey(path=self.partition_key)
        )
        return container
    
    def create_item_cosmosdb(self, item: Dict) -> Dict:
        container = self.get_cosmosdb_container()
        item = container.create_item(item)
        return item
    
    def upsert_item_cosmosdb(self, item: Dict) -> Dict:
        container = self.get_cosmosdb_container()
        item = container.upsert_item(item)
        return item
    
    def delete_item_cosmosdb(self, item: Dict) -> Dict:
        container = self.get_cosmosdb_container()
        item = container.delete_item(item)
        return item
    
    def get_item_cosmosdb(self, item: Dict) -> Dict:
        container = self.get_cosmosdb_container()
        item = container.read_item(item)
        return item
    
    def query_items_cosmosdb(self, query: str) -> Iterable:
        container = self.get_cosmosdb_container()
        items = container.query_items(query, enable_cross_partition_query=True)
        return items