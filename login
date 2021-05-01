from load import User as User # Memanggil variabel User dari load sebagai User pada file ini
# Fungsi Login untuk masuk ke dalam sistem Kantong Ajaib

# KAMUS

data_username = []  # inisialisasi list kosong
for i in range(len(User)):  # Mengisi list dengan username milik user dari variabel User
    data_username.append(User[i][1])

data_password = [] # inisialisasi list kosong
for i in range(len(User)): # Mengisi list dengan password milik user dari variabel User
    data_password.append(User[i][4])

data_role = [] # inisialisasi list kosong
for i in range(len(User)): # Mengisi list dengan role milik user dari variabel User
    data_role.append(User[i][5])

data_nama = [] # inisialisasi list kosong
for i in range(len(User)): # Mengisi list dengan nama milik user dari variabel User
    data_nama.append(User[i][2])



def login():
    global role
    global nama

    username = input("Masukkan username: ")  
    while Is_Username(username, User) == False : # Jika username yang diinput user salah / tidak terdaftar, meminta input hingga valid
        print("Username Salah! Silahkan masukkan username yang tepat")  
        username = input("Masukkan username: ") 

    # Input username sudah benar
    password = input("Masukkan password: ")  
    while Is_Password(username, password, User) == False:  # Jika password yang diinput salah / tidak sesuai, meminta input hingga valid
        print("Password yang di input salah! ")  
        password = input("Masukkan password; ") 

    # Username dan password user sudah benar dan sesuai
    role = data_role[Get_Position(username, User)]  # Mengambil role dari akun yang digunakan user
    nama = data_nama[Get_Position(username, User)]
    print("Selamat Datang " + role + ' ' + username +" di Kantong Ajaib !") 


def Is_Username(username, User):  # Memeriksa apakah username yang diinput user ada pada varibel user melalui data_username
    Bool = False
    Position = 0
    for i in range(len(User)):
        if username == data_username[i]:
            Bool = True
            Position = Position + i
    return(Bool)
    return(Position)

def Get_Position(username, User):  # Mencari posisi username yang sudah divalidasi melalui Is_Username
    Position = 0
    for i in range(len(User)):
        if username == data_username[i]:
            Position = Position + i
    return(Position)

def Is_Password(username, password, User):  # Mmeriksa apakah password yang diinput sudah benar dan sesuai dengan pasangan usernya berdasarkan posisi dari Get_Posisition dan dari data_usernamea
    Bool = False
    for i in range(len(User)):
        if password == data_password[Get_Position(username, User)]:
            Bool = True
    return(Bool)

login()
