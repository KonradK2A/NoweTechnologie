from mysql.connector import connect, Error
import ctypes


class DatabaseAccountManager:
    def __init__(self):
        try:
            with open("access.dat", "r") as f:
                access = f.readlines()
                self.connection = connect(
                    host=access[0][:-1],
                    user=access[1][:-1],
                    password=access[2][:-1],
                    database=access[3][:-1],
                )
            self.cursor = self.connection.cursor()
        except Error as e:
            # print(f"Error while connecting to database occurred: {e}")
            raise ctypes.windll.user32.MessageBoxW(0, f"Application raised an error. \n "
                                                      f"Error: {e}",
                                                   "Warning!", 0x10)

    # create account, does not login to the account automatically
    def connection_create_account(self, login: str, password: str) -> bool:
        # check if username is not taken and if password is correct
        query = "SELECT login FROM users;"
        self.cursor.execute(query)
        result = list(self.cursor)
        isTaken = False
        for row in result:
            if login in row:
                isTaken = True
                break
        if not isTaken:
            # creating actual account
            query = f"""INSERT INTO users (login, password, money)
                        VALUES ('{login}', '{password}', 0);"""
            self.cursor.execute(query)
            self.connection.commit()
            # print("Account created")
            self.connection.close()
            return True
        else:
            # print(f"Username taken or '{login}' is shorter than 3 characters.")
            self.connection.close()
            return False

    # login to the account, returns T/F weather password and login is correct or not
    def connection_login(self, login: str, password: str) -> bool:
        query = f"SELECT login, password, money FROM users WHERE login='{login}';"
        self.cursor.execute(query)
        result: list = self.cursor.fetchall()
        if len(result) != 0:
            if login == result[0][0] and password == result[0][1]:
                # print(f"Logged into system. Welcome {login}. Your account balance is {result[0][2]} USD")
                self.connection.close()
                return True
            else:
                # print(f"Login failed. No such user or incorrect password")
                self.connection.close()
                return False
        else:
            # print("Login failed. No such user or incorrect password!")
            self.connection.close()
            return False


class DatabaseItemsManager:
    def __init__(self):
        try:
            with open("access.dat", "r") as f:
                access = f.readlines()
                self.connection = connect(
                    host=access[0][:-1],
                    user=access[1][:-1],
                    password=access[2][:-1],
                    database=access[3][:-1],
                )
            self.cursor = self.connection.cursor()
        except Error as e:
            # print(f"Error while connecting to database occurred: {e}")
            raise ctypes.windll.user32.MessageBoxW(0, f"Application raised an error. \n "
                                                      f"Error: {e}",
                                                   "Warning!", 0x10)

    # if user is logged in he can check his account balance
    def connection_show_items(self, login: str) -> list:
        query = f"""SELECT cars.brand, cars.model, cars.engine, cars.price, cars.plate_num FROM cars 
                    INNER JOIN users ON users.login=cars.user_login 
                    WHERE users.login='{login}';"""
        self.cursor.execute(query)
        result: list = self.cursor.fetchall()
        self.connection.close()
        return result
