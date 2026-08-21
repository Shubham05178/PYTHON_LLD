from user import User
from userrepo import UserRepo  
def main():
    i=int(input("Enter  no of Users:"))
    for j in range(i):
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        email=input("Enter Email:")
        user=User(name,age,email)
        repo.add_user(user)
    repo.get_all_users()    


if __name__=="__main__":
    repo=UserRepo()
    main()  