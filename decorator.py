import time

def auth(authtype):
    print(authtype)
    def outwarpper(func):
        def type():
            def wrapper(*args, **kwargs):
                user, passwd = "aohaibo", "AHB123asd"
                if authtype=="local":
                    username = input("input your user name:").strip()
                    password = input("input your password:").strip()
                    if user == username and passwd == password:
                        print("your auth is pass")
                        res=func(*args,**kwargs)
                        print("after auth")
                        return res()
                    else:
                        print("invalid username or password")
                        exit()
                else:
                    print("no type")
            print("no type")
            return wrapper()
        return type()
    return outwarpper()
@auth
def index():
    print("welcome to index")
@auth(authtype="ysj")
def home():
    print("welcome to home")
@auth
def tag():
    print("welcome to tag")
home()
