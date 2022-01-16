from api.repository.repository import Repository
from api.schemas.user import UserIn, UserOut
from api import utils

async def create_user(user: UserIn, db: Repository) -> UserOut:
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    await db.users.insert_one(user.dict())
    return user


async def get_user(email: str, db: Repository) -> UserOut:
    user = await db.users.find_one({"email":email})
    return user

