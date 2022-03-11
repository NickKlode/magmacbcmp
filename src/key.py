
def make_key(char_key):
    if len(char_key)!=32:
        print("Неверная длина ключа!")
        exit()
    
    bin_key = ''.join(format(ord(x),'08b') for x in char_key)
    K = []
    for j in range(0, 256, 32):
        K.append( bin_key[j:j+32] )
    
    return K