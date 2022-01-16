import json
import os
import logging

from bson import ObjectId

from api.repository import Repository
from api.schemas.game import GameIn
from api.schemas.image import ImageOut

async def load_json_data(db: Repository) -> None:
    curr_dir = os.path.dirname(__file__)
    fixtures_dir = os.path.join(curr_dir, "..", "fixtures")
    sample_json_data_file = os.path.join(fixtures_dir, "UITest.json")
    
    logging.info(f"Reading Json file from {sample_json_data_file}")
    
    with open(sample_json_data_file) as json_file:
        data = json.load(json_file)
        logging.info("Read json file.")
        game_listings = data["listings"]
        games = []
        for game_listing in game_listings:
            images = []
            game = GameIn(**game_listing)
            for img in game.images:
                images.append(ImageOut(**img.dict(), id=ObjectId()))
            game.images=images
            games.append(game.dict())
        logging.info("Loading sample data...")
        await db.games.insert_many(games)  
        logging.info("Loaded sample data.")

