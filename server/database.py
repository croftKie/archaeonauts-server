import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.archaeonauts

players_collection = database.get_collection("players_collection")



async def retrieve_players():
    players = []
    async for player in players_collection.find():
        players.append(player_helper(player))
    return players


async def add_player(player_data: dict) -> dict:
    player = await players_collection.insert_one(player_data)
    new_player = await players_collection.find_one({"_id": player.inserted_id})
    return player_helper(new_player)


async def retrieve_player(id: str) -> dict:
    player = await players_collection.find_one({"_id": ObjectId(id)})
    if player:
        return player_helper(player)


async def update_player(id: str, data: dict):
    if len(data) < 1:
        return False
    player = await players_collection.find_one({"_id": ObjectId(id)})
    if player:
        updated_player = await players_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_player:
            return True
        return False


# Delete a player from the database
async def delete_player(id: str):
    player = await players_collection.find_one({"_id": ObjectId(id)})
    if player:
        await players_collection.delete_one({"_id": ObjectId(id)})
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