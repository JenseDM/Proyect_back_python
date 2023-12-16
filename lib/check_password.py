from model.handle_db import HandleDB
from werkzeug.security import check_password_hash
from fastapi.responses import RedirectResponse

#Para verificar el usuario en el login
def check_user(username, password):
    user = HandleDB()
    filter_user = user.get_only(username)
    if filter_user:
        same_passwword = check_password_hash(filter_user[4], password)
        if same_passwword:
            return filter_user
    return None
    
#Para verificar el usuario en el delete y update
def check_user_id(user_id, password):
    user = HandleDB()
    filter_user = user.get_only_id(user_id)
    if filter_user:
        same_passwword = check_password_hash(filter_user[4], password)
        if same_passwword:
            return filter_user
    return None