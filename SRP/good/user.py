class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email
    def get_user_info(self):
        return f"Name: {self.__name}, Age: {self.__age}, Email: {self.__email}"
    def is_adult(self):
        return self.__age >= 18