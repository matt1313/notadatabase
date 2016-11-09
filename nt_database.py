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
                self.data.append(line)

    def user_name(user_list):
        user_info = input("Please enter you're name: ")
        user_list.append(user_info)
        if user_info >= user_list[0]:
            def user_password(user_code):
                user_pass = input("Please enter your password: ")
                user_code.append(user_info)
                if user_pass >= user_code[0]:
                    return user_pass, user info

    def _save(self):
        with open(self.data_filename, "w") as f:
            for data in self.data:
                f.write(data)
                f.write("\n")




# def main():
#     Opener.user_name(user_list)
#
# main()

# if __name__ == "__main__":
#     main()
