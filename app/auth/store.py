from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class User:
    id: int
    username: str
    password_hash: str


_users_by_username: Dict[str, User] = {}
_next_user_id = 1


def get_user_by_username(username: str) -> Optional[User]:
    return _users_by_username.get(username)


def create_user(username: str, password_hash: str) -> User:
    global _next_user_id
    user = User(id=_next_user_id, username=username, password_hash=password_hash)
    _users_by_username[username] = user
    _next_user_id += 1
    return user
