class Mahasiswa:
    def __init__(self):
        self.nama = ""
        self.prak1 = 0
        self.prak2 = 0
        self.prak3 = 0
    def getRata(self):
        return round((self.prak1+self.prak2+self.prak3)/3,2)
filename = input("Nama file ? ")
datamhs = list()
try: 
    with open(filename, "r") as text:
        for line in text.read().splitlines():
            for i in range(len(line)):
                if line[i].isdigit():
                    temp = i
                    break
            mhs = Mahasiswa()
            mhs.nama = line[0 : temp].rstrip()
            prak = line[temp:len(line)].split(" ")
            mhs.prak1 = int(prak[0])
            mhs.prak2 = int(prak[1])
            mhs.prak3 = int(prak[2])
            datamhs.append(mhs)
    text.close()    
except:
    exit("file not found")
while True :
    print("--------------[Menu]-------------------------")
    print("| 1. Lihat Nilai")
    print("| 2. Update Nilai")
    print("| 3. Hapus Data")
    print("| 4. Lihat Semua")
    print("| 5. Simpan ke file")
    print("| 6. Keluar")
    print("_______________________________")
    menu = input("pilih? ")
    if menu == "1":
        found = False
        key_nama = input("Nama mahasiswa? ")
        for mhs in datamhs:
            if mhs.nama == key_nama:
                print(str(mhs.prak1)+" "+str(mhs.prak2)+" "+str(mhs.prak3)+"(Rerata = "+str(mhs.getRata())+")")
                found = True
                break
        if not found :
            print("Nama tidak ditemukan")
        
    elif menu == "2":
        found = False
        key_nama = input("Nama mahasiswa? ")
        for mhs in datamhs:
            if mhs.nama == key_nama:
                prakke = input("Update praktikum ke-? ")
                if prakke == '1':
                    mhs.prak1 = int(input("Nilai Baru : "))
                elif prakke == '2':
                    mhs.prak2 = int(input("Nilai Baru : "))
                elif prakke == '3':
                    mhs.prak3 = int(input("Nilai Baru : "))
                else :
                    print("Praktikum hanya 1-3")
                found = True
                print("Data berhasil terupdate")
                break
        if not found :
            print("Nama tidak ditemukan")
    elif menu == "3":
        found = False
        key_nama = input("Nama mahasiswa? ")
        for mhs in datamhs:
            if mhs.nama == key_nama:
                datamhs.remove(mhs)
                found = True
                print("Data berhasil terhapus")
                break
        if not found :
            print("Nama tidak ditemukan")
    elif menu == "4":
        print("-----------------------------------------------------")
        print("|{:^15}|{:^8}|{:^8}|{:^8}|{:^8}|".format("NAMA","PRAK 1","PRAK 2","PRAK 3","RERATA"))
        print("-----------------------------------------------------")
        for mhs in datamhs:
            print("|{:^15}|{:^8}|{:^8}|{:^8}|{:^8}|".format(mhs.nama,mhs.prak1,mhs.prak2,mhs.prak3,mhs.getRata()))
        print("-----------------------------------------------------")
    elif menu == "5":
        sourceFile = open(filename, 'w')
        for mhs in datamhs:
            print(mhs.nama+" "+str(mhs.prak1)+" "+str(mhs.prak2)+" "+str(mhs.prak3)+" "+str(mhs.getRata()), file = sourceFile)
        sourceFile.close()
        print("Data berhasil tersimpan")
    elif menu == "6":
        exit("TERIMA KASIH!")
    print("\n")
    

    
