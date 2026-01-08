# ==============================
# PROJEK PBO PYTHON
# Sistem Informasi Nilai Mahasiswa
# ==============================

# Class Mahasiswa
class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan


# Class Nilai
class Nilai:
    def __init__(self, mata_kuliah, nilai):
        self.mata_kuliah = mata_kuliah
        self.nilai = nilai

    # ==============================
    # MODIFIKASI:
    # Method untuk mengubah nilai angka menjadi nilai huruf
    # ==============================
    def nilai_huruf(self):
        if self.nilai >= 85:
            return "A"
        elif self.nilai >= 70:
            return "B"
        elif self.nilai >= 60:
            return "C"
        elif self.nilai >= 50:
            return "D"
        else:
            return "E"


# Class Sistem Nilai (Program Utama)
class SistemNilai:
    def __init__(self):
        self.data = []

    def tambah_data(self):
        print("\n=== Tambah Data Mahasiswa ===")

        nama = "Qusay"  # Nama otomatis
        npm = input("NPM : ")
        jurusan = input("Jurusan : ")
        matkul = input("Mata Kuliah : ")
        nilai_angka = int(input("Nilai : "))

        mahasiswa = Mahasiswa(nama, npm, jurusan)
        nilai = Nilai(matkul, nilai_angka)

        self.data.append((mahasiswa, nilai))
        print(">> Data berhasil ditambahkan")

    def tampilkan_data(self):
        print("\n=== Data Nilai Mahasiswa ===")
        if not self.data:
            print("Belum ada data mahasiswa.")
        else:
            for i, (mhs, nilai) in enumerate(self.data, start=1):
                print(f"\nMahasiswa ke-{i}")
                print("Nama        :", mhs.nama)
                print("NPM         :", mhs.npm)
                print("Jurusan     :", mhs.jurusan)
                print("Mata Kuliah :", nilai.mata_kuliah)
                print("Nilai Angka :", nilai.nilai)
                print("Nilai Huruf :", nilai.nilai_huruf())  # PEMANGGILAN MODIFIKASI


# Menjalankan Program
app = SistemNilai()
app.jalankan()
