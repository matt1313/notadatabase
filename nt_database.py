import random
import sys
import os

user_list = []
user_code = []

class Opener:

    def __init__(self, data_filename="info.csv"):
        self.data_filename = data_filename
        self.data = []
        with open(self.data_filename, "r") as f:
            for line in f:
                self.data.append(line.strip())
        print(self.data)

    def add_user(self):
        user_name, password = get_user_info()
        self.data.append(user_name + "," + password)

    def save(self):
        with open(self.data_filename, "w") as f:
            for data in self.data:
                f.write(data)
                f.write("\n")


    def is_valid_user(self, user_name, password):
        print(self.data, user_name, password)
        return user_name + "," + password in self.data


    def user_name(user_list):
        user_info = input("Please enter your name: ")
        user_list.append(user_info)
        if user_info >= user_list[0]:
            def user_password(user_code):
                user_pass = input("Please enter your password: ")
                user_code.append(user_info)
                if user_pass >= user_code[0]:
                    def login_prompt():
                        confirm = input("""Your information does not match our not-a-database.
                        Would you like to join? y/n """)
                        if confirm == ("y"):
                            create_config()
                        else:
                            user_name(user_list)

    #
    def create_config():
        account_create = input("""Please enter your name: ?
        Please enter a password: ?""")




    # def save(self):
    #     with open(self.data_filename, "w") as f:
    #         for data in self.data:
    #             f.write(data)
    #             f.write("\n")

def login(o):
    user_name, password = get_user_info()
    return o.is_valid_user(user_name, password)


def get_user_info():
    user_name = input("Input user name: ")
    password = input("Input password: ")
    return user_name, password


def main():
    o = Opener()
    while not (login(o)):
        pass
    print("You logged in!")
    o.add_user()
    o.save()

main()

# if __name__ == "__main__":
#     main()
