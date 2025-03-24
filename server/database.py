from bson.objectid import ObjectId
from decouple import config
import pymongo
import certifi

MONGO_DETAILS = config("MONGO_DETAILS")

client = pymongo.MongoClient(MONGO_DETAILS, tlsCAFile=certifi.where())

database = client.archaeonauts

players_collection = database.get_collection("players_collection")

async def retrieve_players():
    players = []
    for player in players_collection.find():
        players.append(player_helper(player))
    return players

async def add_player(player_data: dict) -> dict:
    print(players_collection)
    player = players_collection.insert_one(player_data)
    new_player = players_collection.find_one({"_id": player.inserted_id})
    return player_helper(new_player)

async def retrieve_player(id: str) -> dict:
    player = players_collection.find_one({"_id": ObjectId(id)})
    if player:
        return player_helper(player)

async def update_player(id: str, data: dict):
    print(data)
    if len(data) < 1:
        return False
    player = players_collection.find_one({"_id": ObjectId(id)})
    if player:
        updated_player = players_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_player:
            return True
        return False

async def delete_player(id: str):
    player = players_collection.find_one({"_id": ObjectId(id)})
    if player:
        players_collection.delete_one({"_id": ObjectId(id)})
        return True









## Helpers

def player_helper(player) -> dict: 
    return {
        "id": str(player["_id"]),
        "username": player["username"],
        "email": player["email"],
        "hash": player["hash"],
        "stats": player["stats"]
    }