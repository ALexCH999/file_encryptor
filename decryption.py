import pyAesCrypt
import os
import sys

# функция дешифровки файла
def decryption(file, password):
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print("[файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    os.remove(file)


def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)

        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для расшифровки:")
walking_by_dirs("/Users/lesacervonnyj/Desktop/TEST_encryption", password)

#os.remove(sys.argv[0])
