import pyAesCrypt
import os
import sys

# функция шифрования файла
def encryption(file, password):
    # задаем размер буфера
    buffer_size = 512 * 1024
    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    print("[файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    os.remove(file)

def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                encryption(path,password)
            except Exception as ex:
                print(ex)
        # если находим дерикторию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path,password)


password = input("Введите пароль для шифрования:")
walking_by_dirs("/Users/lesacervonnyj/Desktop/TEST_encryption", password)

#os.remove(sys.argv[0])
