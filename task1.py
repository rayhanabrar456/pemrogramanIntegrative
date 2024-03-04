
def gaji():
    print("--- Hitung Gaji Bulanan ---")
    print("\n")

    nama = input("Masukkan Nama Anda: ")
    gaji_tahunan = int(input("Masukkan Gaji Tahunan Anda: "))

    print("\n")

    gaji_bulanan = round(gaji_tahunan / 12, 0)

    print("Nama :", nama)
    print("Gaji Bulanan: Rp.", gaji_bulanan)

    print("\n")
    print("----- Thank You -----")
    print("\n")

if __name__ == "__main__":
    gaji()