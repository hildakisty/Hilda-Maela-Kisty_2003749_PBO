class Tabungan:
    def __init__(self,sld_umum, Sld_tab,tbh_umum,tbh_tab, ambil_umum,ambil_tab):
        self.saldo1=sld_umum
        self.saldo2=Sld_tab
        self.tambah1=tbh_umum
        self.tambah2=tbh_tab
        self.ambil1=ambil_umum
        self.ambil2=ambil_tab

    def saldo_umum(self):
        print("Saldo umum Anda saat ini adalah: Rp.0,-", self.saldo1)

    def saldo_tabungan(self):
        print("Saldo tabungan Anda saat ini adalah: Rp.0,-", self.saldo2)

    def tambah_umum(self):
        print("Nominal uang yang akan ditambahkan :", self.tambah1)

    def tambah_tabungan(self):
        print("Nominal uang yang akan ditambahkan :", self.tambah2)

    def ambil_umum(self):
        print("Nominal Uang yang akan diambil :", self.ambil1)
    
    def ambil_tabungan(self):
        print("Nominal Uang yang akan diambil :", self.ambil2)


#Kelas Turunan

class InformasiUm(Tabungan):
    def Infoumum(self):
        Tabungan.saldo_umum(self)

    def keterangan(self):
        print("Saldo umum Anda saat ini adalah: Rp.0,-")

class InformasiTab(Tabungan):
    def InfoTabungan(self):
        Tabungan.saldo_tabungan(self)

    def keterangan(self):
        print("Saldo Tabungan Anda saat Ini adalah: Rp.0,-")

class TambahUm(Tabungan):
    def TambahUmum(self):
        Tabungan.tambah_umum(self)

    def keterangan(self):
        print("Nominal uang yang akan ditambahkan :")

class TambahTab(Tabungan):
    def TambahTabungan(self):
        Tabungan.tambah_tabungan(self)

    def keterangan(self):
        print("Nominal Uang yang akan Ditambahkan :")

class AmbilUm(Tabungan):
    def AmbilUmum(self):
        Tabungan.ambil_umum(self)

    def keterangan(self):
        print("Nominal Uang yang akan diambil :")

class AmbilTab(Tabungan):
    def AmbilTabungan(self):
        Tabungan.ambil_tabungan(self)      

    def keterangan(self):
        print("Nominal Uang yang akan diambil :")  

print("**Aplikasi Pencatatan Uang Digital**")
print("**************")
print("[1] Informasi Saldo")
print("[2] Tambah Saldo")
print("[3] Ambil Saldo")
print("[4] Keluar")
print("**************")
option=int(input("PIlih Menu:"))
if option==1:
    i=InformasiUm
    i.Infoumum
    i.keterangan

    i=InformasiTab
    i.InfoTabungan
    i.keterangan

elif option==2:
    print("[1] Umum")
    print("[2] Tabungan")
    option=int(input("Pilih Penyimpanan:"))
    print("**************")
if option==1:
    i=TambahUm
    i.TambahUmum()
    i.keterangan()
elif option==2:
    i=TambahTab
    i.TambahTabungan
    i.keterangan

elif option==3:
    print("[1] Umum")
    print("[2] Tabungan")
    option=int(input("Pilih Penyimpanan:"))
    print("**************")
if option==1:
    i=AmbilUm
    i.AmbilUmum
    i.keterangan
elif option==2:
    i=AmbilTab
    i.AmbilTabungan
    i.keterangan