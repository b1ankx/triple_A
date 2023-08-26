import random

class UserInfo:
    login: str
    password: str
    access_level: int

    def __init__(self, login, password, access_level: int = 0):
        self.login = login
        self.password = password
        self.access_level = access_level
    
class UserInfoHandler:
    def process(self, userinfo: UserInfo):
        raise NotImplementedError()

class NoneUserInfo(UserInfoHandler):
    def process(self, userinfo: UserInfo):
        return userinfo

class UserInfoPart(UserInfoHandler):
    next_user_info_part: UserInfoHandler

    def set_next_part(self, next_user_part: UserInfoHandler):
        self.next_user_info_part = next_user_part

    def process(self, userinfo: UserInfo):
        self.proccess_current(userinfo=userinfo)
        self.next_user_info_part.process(userinfo=userinfo)

    def proccess_current(self, userinfo: UserInfo):
        raise NotImplementedError()
    
class UserInfoLogin(UserInfoPart):
    def proccess_current(self, userinfo: UserInfo):
        if userinfo.login == 'admin' or userinfo.login == 'student':
            print('login :', userinfo.login, 'successful')
        else:
            print('login :', userinfo.login, 'unsuccessful')

class UserInfoPasswd(UserInfoPart):
    def proccess_current(self, userinfo: UserInfo):
         if userinfo.password == 'qwerty' or userinfo.password == '123':
            print('password :', userinfo.password, 'successful')
         else:
            print('password :', userinfo.password, 'unsuccessful')
     

class UserInfoHello(UserInfoPart):
    def proccess_current(self, userinfo: UserInfo):
        userinfo.access_level = random.randint(1, 3)
        if userinfo.access_level == 3:
            print("you're welcome")
        else :
            print("upgrade your access level")

check1 = UserInfoLogin()
check2 = UserInfoPasswd()
check3 = UserInfoHello()

check1.set_next_part(check2)
check2.set_next_part(check3)
check3.set_next_part(NoneUserInfo())

input_login = str(input('Введите логин:'))
input_password = str(input('Введите пароль:'))
user_info_for_test = UserInfo(login=input_login,
                              password=input_password,)

check1.process(userinfo=user_info_for_test)