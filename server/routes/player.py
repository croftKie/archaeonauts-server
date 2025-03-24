from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import bcrypt

from ..database import (
    add_player,
    delete_player,
    retrieve_player,
    retrieve_players,
    update_player,
    login_player
)
from ..models.player import (
    ErrorResponseModel,
    ResponseModel,
    PlayerSchema,
    UpdatePlayerModel,
)

router = APIRouter()

@router.post("/", response_description="Player data added into the database")
async def add_player_data(player: PlayerSchema = Body(...)):
    p = player.dict()
    password = p["hash"]
    p_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    p_hash = bcrypt.hashpw(p_bytes, salt)
    print('$2b$12$5yQ2QmsEjcCDNLxqv6BDaeUIY8sYNVyklyXmEsuXmpHvOCY4sWflO'.encode("utf-8"))
    p["hash"] = p_hash

    player = jsonable_encoder(p)
    new_player = await add_player(player)
    return ResponseModel(new_player, "Player added successfully.")

@router.get("/", response_description="Players retrieved")
async def get_players():
    players = await retrieve_players()
    if players:
        return ResponseModel(players, "Players data retrieved successfully")
    return ResponseModel(players, "Empty list returned")

@router.get("/login/{username}/{password}", response_description="Player data retrieved")
async def get_player_data(username, password):
    player = await login_player(username)
    if player:
        result = bcrypt.checkpw(password.encode("utf-8"), player["hash"].encode("utf-8"))
        player["logged_in"] = result
        if result:
            return ResponseModel(player, "Player data retrieved successfully")
        else:
            return ResponseModel({}, "Player data not retrieved")
    return ErrorResponseModel("An error occurred.", 404, "Player doesn't exist.")

@router.get("/{id}", response_description="Player data retrieved")
async def get_player_data(id):
    player = await retrieve_player(id)
    if player:
        return ResponseModel(player, "Player data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Player doesn't exist.")

@router.put("/{id}")
async def update_player_data(id: str, req: UpdatePlayerModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_player = await update_player(id, req)
    if updated_player:
        return ResponseModel(
            "Player with ID: {} update is successful".format(id),
            "Player updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the Player data.",
    )

@router.delete("/{id}", response_description="Player data deleted from the database")
async def delete_player_data(id: str):
    deleted_player = await delete_player(id)
    if deleted_player:
        return ResponseModel(
            "Player with ID: {} removed".format(id), "Player deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Player with id {} doesn't exist".format(id)
    )