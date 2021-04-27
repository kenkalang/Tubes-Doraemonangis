from load import Gadget


def check_input(rarity_input):
    if rarity_input == 'A' or rarity_input == 'B' or rarity_input == 'C' or rarity_input == 'S':
        return True
    else:
        return False

def input_valid(rarity_input):
    while not (check_input(rarity_input)):
        print("Masukkan rarity salah")
        rarity_input = input ("Masukkan ulang rarity : ")
    return rarity_input


def printGroup(i,arr):
    if arr[i][0][0] == 'G':
        print("Type Item        :  Gadget")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print("Tahun Ditemukan  : ", arr[i][5])
        print()
    elif arr[i][0][0] == 'C':
        print("Type Item        :  Consumable")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==5:
        print("ID Peminjaman       : ", arr[i][0])
        print("Nama Pengambil      : ", arr[i][1])
        print("Nama Gadget         : ", arr[i][2])
        print("Tanggal Peminjaman  : ", arr[i][3])
        print("Jumlah              : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==4:
        print("ID Pengembalian       : ", arr[i][0])
        print("Nama Pengambil        : ", arr[i][1])
        print("Nama Gadget           : ", arr[i][2])
        print("Tanggal Pengembalian  : ", arr[i][3])
        print()    
    elif arr[0][1] =='id_pengambil':
        print("ID Pengambilan       : ", arr[i][0])
        print("Nama Pengambil       : ", arr[i][1])
        print("Nama consumable      : ", arr[i][2])
        print("Tanggal Pengambilan  : ", arr[i][3])
        print("Jumlah               : ", arr[i][4])


def searchrarity(Gadget):
    n = len(Gadget)
    found = 0
    rarity_input = str(input("Masukkan rarity : "))
    rarity_input = input_valid(rarity_input)
    print()
    print ("Hasil pencarian")
    print()
    for i in range (1,n):
        if Gadget[i][4] == rarity_input:
            found += 1
            printGroup(i,Gadget)
    if found == 0:
        print ("Tidak ada gadget yang ditemukan")