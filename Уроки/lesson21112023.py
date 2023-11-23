import dotenv


class Instagram:
    accounts = [("John", "qwerty123")]

    def sign_in(self, username, password):
        for account in self.accounts:
            if account[0] == username:
                print("Username found")
                if account[1] == password:
                    print("Yoy are signed in")
                else:
                    print("Wrond password")


inst = Instagram()

inst.sign_in("John", "qwerty123")