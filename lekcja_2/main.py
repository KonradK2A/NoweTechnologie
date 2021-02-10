from gui import *
from database_manager import *

# TODO account created info window
# TODO account creation failed info window
# TODO account creation window ???
# TODO edit creating account


def authentication(is_register: bool,
                   login: str,
                   password: str
                   ):

    if is_register:
        if databaseManager.connection_create_account(login, password):
            return True, login
        else:
            return False
    elif not is_register:
        if databaseManager.connection_login(login, password):
            return True, login
        else:
            return False


def show_user_items(login: str):
    databaseItemsManager = DatabaseItemsManager()
    userItems = databaseItemsManager.connection_show_items(login=login)
    guiUserItems = GuiUserItems(items=userItems, login=login)
    guiUserItems.grid_items()


if __name__ == '__main__':
    guiAuthorize = GuiAuthorize()
    guiAuthorize.grid_authentication()
    values = guiAuthorize.return_values()

    databaseManager = DatabaseAccountManager()

    isAuthorized = authentication(values[0],
                                  values[1],
                                  values[2])

    if isAuthorized:
        show_user_items(isAuthorized[1])
    else:
        guiUnauthorized = GuiUnauthorized()
        guiUnauthorized.grid_unauthorized()
