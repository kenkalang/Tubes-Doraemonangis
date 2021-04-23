from load import User as User
# Fungsi Login untuk masuk ke dalam sistem Kantong Ajaib

# KAMUS

data_username = []
for i in range(len(User)):
    data_username.append(User[i][1])

data_password = []
for i in range(len(User)):
    data_password.append(User[i][4])

data_role = []
for i in range(len(User)):
    data_role.append(User[i][5])


def login():
    username = input("Masukkan username: ")
    while Is_Username(username, User) == False : 
        print("Username Salah! Silahkan masukkan username yang tepat")
        username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    while Is_Password(username, password, User) == False:
        print("Password yang di input salah! ")
        password = input("Masukkan password; ")
    role = data_role[Get_Position(username, User)]
    print("Selamat Datang " + role + ' ' + username +" di Kantong Ajaib !")
    

def Is_Username(username, User):
    Bool = False
    Position = 0
    for i in range(len(User)):
        if username == data_username[i]:
            Bool = True
            Position = Position + i
    return(Bool)
    return(Position)

def Get_Position(username, User):
    Position = 0
    for i in range(len(User)):
        if username == data_username[i]:
            Position = Position + i
    return(Position)

def Is_Password(username, password, User):
    Bool = False
    for i in range(len(User)):
        if password == data_password[Get_Position(username, User)]:
            Bool = True
    return(Bool)

login()
