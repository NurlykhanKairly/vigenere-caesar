
def caesar_cipher(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[key:]+alphabet[0:key]
    cipher_text = ""

    for ch in text:
        idx = alphabet.find(ch.upper())
        if idx == -1:
            cipher_text = cipher_text + ch
        elif ch.islower():
            cipher_text = cipher_text + shifted_alphabet[idx].lower()
        else:
            cipher_text = cipher_text + shifted_alphabet[idx] 

    return cipher_text


def caesar_decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #               "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[26-key:]+alphabet[0:26-key]

    translated = '' 
    for ch in text:
        idx = alphabet.find(ch.upper())
        if idx == -1:
            translated += ch
        elif ch.islower():
            translated += shifted_alphabet[idx].lower()
        else:
            translated += shifted_alphabet[idx]
    return translated


def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic 


def form_dict():
    d = {}
    iter = 0
    for i in range(0,255):
        d[iter] = chr(i)
        iter = iter +1
    return d


def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict() 

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code


def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict() 

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code


def full_encode(value, key):
    
    key = encode_val(key)
    value = encode_val(value)
 
    dic = comparator(value, key)
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis


def full_decode(value, key):
    key = encode_val(key)

    dic = comparator(value, key)
    d = form_dict() 
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis


def vigenere_encode(value, key):
    return ''.join(decode_val(full_encode(value, key)))


def vigenere_decode(value, key):
    return ''.join(decode_val(full_decode(encode_val(value), key)))


def add_caesar_vigenere(str, key_caesar, key_vigenere):
    return vigenere_encode(caesar_cipher(str, key_caesar), key_vigenere)


def decrypt_caesar_vigenere(str, key_caesar, key_vigenere):
    return caesar_decrypt(vigenere_decode(str, key_vigenere), key_caesar)


def test_caesar():
    text = "CEASER CIPHER DEMO"
    key = 4

    print(caesar_cipher(text, key))
    print(caesar_decrypt(caesar_cipher(text, key), key))


def test_vigenere():
    word = 'Hello world'
    key = 'key'
    
    print('Слово: '+ word)
    print('Ключ: '+ key)

    shifre = full_encode(word, key)
    print('Шифр=', ''.join(decode_val(shifre)))

    decoded = full_decode(encode_val(decode_val(shifre)), key)
    print('Decode list=', decoded)
    decode_word_list = decode_val(decoded)
    print('Word=',''.join(decode_word_list))


if __name__ == "__main__":        
    word = 'Hello World!'
    key_caesar = 4
    key_vigenere = 'key'

    print('Слово : ', word)
    print('Ключ Вижнера : ', key_vigenere)
    print('Ключ Цезаря : ', key_caesar)

    cipher = add_caesar_vigenere(word, key_caesar, key_vigenere)
    print('Шифр Вижнера-Цезаря:', cipher)

    print('Расшифровка Вижнера-Цезаря:', decrypt_caesar_vigenere(cipher, key_caesar, key_vigenere))
