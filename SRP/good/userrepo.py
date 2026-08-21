from user import User   
class UserRepo:
    def __init__(self):
        self.__users = []

    def add_user(self, user:User):
        self.__users.append(user)

    def get_all_users(self):
        print("All Users:")
        for user in self.__users:
            print(user.get_user_info())
        

