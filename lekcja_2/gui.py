from tkinter import Tk, Frame, Entry, Label, Button
from _tkinter import TclError
import ctypes


class GuiAuthorize:
    def __init__(self):
        # window ROOT
        rootDescription = "Authorization - NT-L2"
        self.RootWindow = Tk(className=rootDescription)
        self.RootWindow.geometry("420x150")
        # window ICONS
        self.RootWindow.iconbitmap("icon.ico")
        # window FRAME
        self.loginFrame: Frame = Frame(self.RootWindow)
        self.loginFrame.grid()
        # window WIDGETS
        # logging in labels and entries
        self.loginLabel: Label = Label(self.loginFrame,
                                       text="Login: ",
                                       justify="left")
        self.passwordLabel: Label = Label(self.loginFrame,
                                          text="Password:",
                                          justify="left")
        self.loginButton: Button = Button(self.loginFrame,
                                          text="Login",
                                          justify="center",
                                          pady=5,
                                          command=self.return_values)
        self.loginEntry: Entry = Entry(self.loginFrame)
        self.passwordEntry: Entry = Entry(self.loginFrame, show="•")

        # new account labels end entries
        self.registerLabel: Label = Label(self.loginFrame,
                                          text="Create login: ",
                                          justify="left")
        self.newPasswordLabel: Label = Label(self.loginFrame,
                                             text="Create password:",
                                             justify="left")
        self.confirmPasswordLabel: Label = Label(self.loginFrame,
                                                 text="Confirm password:",
                                                 justify="left")
        self.registerEntry: Entry = Entry(self.loginFrame)
        self.newPasswordEntry: Entry = Entry(self.loginFrame, show="•")
        self.confirmPasswordEntry: Entry = Entry(self.loginFrame, show="•")
        self.registerButton: Button = Button(self.loginFrame,
                                             text="Register",
                                             justify="center",
                                             pady=5,
                                             command=self.return_values)

    def grid_authentication(self):
        # logging in
        self.loginLabel.grid(row=0, column=0)
        self.loginEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        # registering
        self.registerLabel.grid(row=0, column=2)
        self.registerEntry.grid(row=0, column=3)
        self.newPasswordLabel.grid(row=1, column=2)
        self.newPasswordEntry.grid(row=1, column=3)
        self.confirmPasswordLabel.grid(row=2, column=2)
        self.confirmPasswordEntry.grid(row=2, column=3)

        self.loginButton.grid(row=3, column=1)
        self.registerButton.grid(row=3, column=3)

        try:
            self.loginFrame.mainloop()
            self.loginFrame.update()
        except TclError:
            pass

    def return_values(self) -> list:
        try:
            if len(self.registerEntry.get()) >= 3 and \
                    len(self.newPasswordEntry.get()) >= 6 and \
                    len(self.loginEntry.get()) == 0 and \
                    self.newPasswordEntry.get() == self.confirmPasswordEntry.get():
                isRegister = True  # registering
            elif len(self.registerEntry.get()) == 0 and \
                    len(self.passwordEntry.get()) != 0 and \
                    len(self.loginEntry.get()) != 0:
                isRegister = False  # logging in
            else:  # improperly filled form
                isRegister = None
                ctypes.windll.user32.MessageBoxW(0, f"Improperly filled form.\n"
                                                    f"Check this: \n"
                                                    f"Passwords do not match or does not meet standards of length (>6)",
                                                    "Notice!", 0x10)
                exit("Improperly filled form.")
            self.RootWindow.quit()
            if not isRegister:  # logging in
                return [isRegister, self.loginEntry.get(), self.passwordEntry.get()]
            else:  # registering
                return [isRegister, self.registerEntry.get(), self.newPasswordEntry.get()]

        except TclError:
            exit("Authorization forced exit")


class GuiUnauthorized:
    def __init__(self):
        # window ROOT
        rootDescription = "Authorization failed - NT-L2"
        self.RootWindow = Tk(className=rootDescription)
        self.RootWindow.geometry("250x150")
        # window ICONS
        self.RootWindow.iconbitmap("icon.ico")
        # window FRAME
        self.windowFrame: Frame = Frame(self.RootWindow)
        self.windowFrame.grid()
        # window WIDGETS
        self.infoLabel: Label = Label(self.windowFrame,
                                      text="Authorization failed.\n"
                                           "Incorrect login or password!",
                                      justify="center")

    def grid_unauthorized(self):
        self.infoLabel.grid(row=0, column=0)
        try:
            self.RootWindow.quit()
            self.windowFrame.mainloop()
            self.windowFrame.update()
        except TclError:
            exit("TclError update")


class GuiUserItems:
    def __init__(self, items: list, login: str):
        self.items: list = items
        # window ROOT
        rootDescription = f"{login}'s cars - NT-L2"
        self.RootWindow = Tk(className=rootDescription)
        # window ICONS
        self.RootWindow.iconbitmap("icon.ico")
        # window FRAME
        self.windowFrame: Frame = Frame(self.RootWindow)
        self.windowFrame.grid()
        # window WIDGETS
        self.welcomeLabel: Label = Label(self.windowFrame,
                                         text=f"Welcome back {login}\n"
                                              f"Here is the list of your cars:",
                                         borderwidth=2,
                                         relief="ridge",
                                         anchor="w",
                                         pady=10,
                                         width=25
                                         )

    def grid_items(self):
        lst = ["Brand", "Model", "Engine", "Price", "Plate number"]
        width = 25
        for i in range(len(lst)):
            out: Label = Label(self.windowFrame,
                               text=f"{lst[i]}",
                               borderwidth=2,
                               relief="ridge",
                               width=width)
            out.grid(row=1, column=i)
        for i in range(len(self.items)):
            for j in range(len(self.items[0])):
                out: Label = Label(self.windowFrame,
                                   text=self.items[i][j],
                                   borderwidth=2,
                                   relief="ridge",
                                   anchor="w",
                                   width=width)
                out.grid(row=i + 2, column=j)

        self.welcomeLabel.grid(row=0, column=2)

        self.windowFrame.update()
        self.windowFrame.mainloop()


class GuiUserCreated:
    def __init__(self):
        # window ROOT
        rootDescription = "Account created - NT-L2"
        self.RootWindow = Tk(className=rootDescription)
        self.RootWindow.geometry("250x150")
        # window frame
        self.windowFrame: Frame = Frame(self.RootWindow)
        self.windowFrame.grid()
        # window widgets
        self.infoLabel: Label = Label(self.windowFrame)
