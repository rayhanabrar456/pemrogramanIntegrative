
def menentukanukuran():
    print("=== Menentukan Ukuran ===")
    print("\n")

    number = int(input("Masukkan sebuah angka: "))

    print("\n")

    if number < 100:
        print("Kecil")
    elif number <= 200:
        print("Sedang")
    else:
        print("Besar")

    print("\n")
    print("=+=+=+= Thank You =+=+=+=")
    print("\n")

if __name__ == "__main__":
    menentukanukuran()