import os
import hashlib
import shutil

# Path ke flashdisk dan file yang digunakan
flashdisk_path = "/media/pi/FLASHDISK"  # Sesuaikan dengan path flashdisk
key_file = "security_key.txt"           # File kunci
program_file = "update_program.py"      # File pembaruan program
destination_program_path = "/path/to/robot_program.py"  # Path program robot yang lama

# Fungsi untuk memeriksa apakah flashdisk terhubung
def check_flashdisk():
    if not os.path.exists(flashdisk_path):
        print("Flashdisk tidak terhubung!")
        return False
    return True

# Fungsi untuk memverifikasi kunci di flashdisk
def verify_key():
    if check_flashdisk():
        key_path = os.path.join(flashdisk_path, key_file)
        if not os.path.isfile(key_path):
            print("File kunci tidak ditemukan!")
            return False

        with open(key_path, 'r') as f:
            key = f.read().strip()

        # Verifikasi kunci dengan hash
        key_hash = hashlib.sha256(key.encode()).hexdigest()
        expected_hash = "expected_hash_of_security_key"  # Gantilah dengan hash kunci yang diinginkan

        if key_hash == expected_hash:
            print("Kunci valid. Pembaruan dapat dilakukan.")
            return True
        else:
            print("Kunci tidak valid!")
            return False
    else:
        print("Flashdisk tidak terdeteksi.")
        return False

# Fungsi untuk mengupdate program robot
def update_program():
    if verify_key():
        print("Membaca pembaruan dari flashdisk...")
        update_file_path = os.path.join(flashdisk_path, program_file)
        if os.path.isfile(update_file_path):
            # Menyalin file program baru ke robot
            shutil.copy(update_file_path, destination_program_path)
            print("Pembaruan selesai.")
        else:
            print("File pembaruan tidak ditemukan di flashdisk.")
    else:
        print("Akses pembaruan diblokir karena kunci tidak valid.")

# Fungsi utama untuk menjalankan pembaruan
def main():
    update_program()

if __name__ == "__main__":
    main()
