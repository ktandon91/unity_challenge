from api.repository.repository import Repository
from api.schemas.base import OID
from api.schemas.user import UserIn, UserOut
from api import utils

async def create_user(user: UserIn, db: Repository):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    await db.users.insert_one(user.dict())
    return user


async def get_user(email: str, db: Repository):
    user = await db.users.find_one({"email":email})
    return user

async def get_users(db: Repository):
    users = db.users.find()
    users_list = []
    async for user in users:
        users_list.append(UserOut(**user, id=user['_id']))
    return users_list
