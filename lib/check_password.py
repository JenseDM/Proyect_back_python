from model.handle_db import HandleDB
from werkzeug.security import check_password_hash
from fastapi.responses import RedirectResponse

def check_user(username, password):
    user = HandleDB()
    filter_user = user.get_only(username)
    if filter_user:
        same_passwword = check_password_hash(filter_user[4], password)
        if same_passwword:
            return filter_user
    return None