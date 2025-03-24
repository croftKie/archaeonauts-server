from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_player,
    delete_player,
    retrieve_player,
    retrieve_players,
    update_player,
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
    player = jsonable_encoder(player)
    new_player = await add_player(player)
    return ResponseModel(new_player, "Player added successfully.")

