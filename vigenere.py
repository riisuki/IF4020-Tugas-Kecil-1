import re

def vigenere(key, text, isencrypt, isauto, isextended):
    # Untuk Vigenere dengan 26 huruf alfabet
    # Huruf non-alfabet akan hilang saat dienkripsi
    # key       : kunci yang digunakan
    # text      : plainteks
    # isauto    : bernilai true jika merupakan auto-key vigenere
    # isencrypt : true jika mengenkripsi, false jika dekripsi
    # isextended: true jika extended (256 karakter ASCII)

    # 1. Ambil hanya karakter alfabet dari input
    regex = re.compile('[^a-zA-Z]')
    plainteks = text
    kunci = key

    if not isextended:
        plainteks = regex.sub('', text).upper()
        kunci = regex.sub('', key).upper()
    hasil = ''

    # 2. Generate ciphertext
    counter = 1
    panjangkunci = len(kunci)

    if panjangkunci == 0:
        return ''
    
    for char in plainteks:
        # Encrypt
        if counter > panjangkunci:
            if isauto:
                # Gunakan plainteks sebagai kunci
                i = counter - panjangkunci - 1
                hasil += geser(char,plainteks[i], isencrypt, isextended)
                                 
            else:
                # Ulangi kunci jika habis
                i = counter % panjangkunci - 1
                hasil += geser(char,kunci[i],isencrypt, isextended)
        else:
            hasil += geser(char,kunci[counter-1], isencrypt, isextended)
                
        counter = counter + 1

    return hasil

def geser(char, key, enkripsi, is256):
    # Input char dan key masing-masing 1 karakter uppercase
    # enkripsi: true jika untuk enkripsi, false jika dekripsi
    # is256   : true jika untuk 256 karakter (Vigenere Extended)
    # Nilai A uppercase ASCII = 65:
    idxA = 65
    if is256:
        idxA = 0
        
    ordhasil = ord(char) - idxA
    if enkripsi:
        ordhasil = ordhasil + ord(key) - idxA  + 1
    else:
        ordhasil = ordhasil - (ord(key) - idxA  + 1)

    if is256:
        ordhasil = ordhasil % 256
    else:
        ordhasil = ordhasil % 26

    
    ordhasil = ordhasil + idxA
    
    return chr(ordhasil)


