
import os
import argparse
from encryption import encrypt_cbc
from decryption import decrypt_cbc


def locate(filename):
    __location__ = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
    return os.path.join(__location__,'data',filename)

def main(args):
    print("Выбор действия:")
    opt = int(input("1. Зашифровать, 2. Расшифровать "))

    if opt==1:
        encrypt_cbc(locate(args.main_file),locate(args.key_file),locate(args.encrypted_file),locate(args.decrypted_file))
    else:
        decrypt_cbc(locate(args.encrypted_file),locate(args.key_file),locate(args.decrypted_file))


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Запуск кода')

    parser.add_argument('--main_file', type=str, default='original.txt', 
            help='Имя файла для зашифрования.')
    
    parser.add_argument('--key_file', type=str, default='key.txt', 
            help='Ключ шифрования. 32 символа.')
    
    parser.add_argument('--encrypted_file', type=str, default='encrypted.txt', 
            help='Имя зашифрованного файла.')
    
    parser.add_argument('--decrypted_file', type=str, default='decrypted.txt', 
            help='Файл с расшифрованными данными.')

    args = parser.parse_args()
    
    main(args)