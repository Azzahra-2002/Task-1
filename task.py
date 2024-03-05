class MyClass:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Membuat objek dari kelas MyClass
objek1 = MyClass("Karima Azzahra Karim", "A", "Pendidikan Komputer", "Fakultas Keguruan dan Ilmu Pendidikan", "Samarinda", "Batam")

# Menampilkan nilai atribut objek
print("Nilai atribut objek1:")
print("Nama:", objek1.nama)
print("Kelas:", objek1.kelas)
print("Prodi:", objek1.prodi)
print("Fakultas:", objek1.fakultas)
print("Tempat Tinggal:", objek1.tempat_tinggal)
print("Asal:", objek1.asal)
