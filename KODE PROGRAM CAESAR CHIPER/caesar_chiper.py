def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Menyesuaikan arah pergeseran berdasarkan mode
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Enkripsi/Dekripsi huruf kapital
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Enkripsi/Dekripsi huruf kecil
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Karakter selain huruf (spasi, angka, simbol) tidak diubah
        else:
            result += char
            
    return result

# --- Contoh Penggunaan ---
pesan = "Halo Dunia!"
kunci = 3

# Proses Enkripsi
terenkripsi = caesar_cipher(pesan, kunci, mode='encrypt')
print(f"Teks Asli: {pesan}")
print(f"Hasil Enkripsi (Shift {kunci}): {terenkripsi}")

# Proses Dekripsi
terdekripsi = caesar_cipher(terenkripsi, kunci, mode='decrypt')
print(f"Hasil Dekripsi: {terdekripsi}")