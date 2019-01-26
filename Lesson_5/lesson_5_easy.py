
__author__ = 'Шонтукова Арина Артуровна'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
dir_path = os.path.join(os.getcwd(), 'dir_')

try:
    for i in range(1, 10):
        os.mkdir(dir_path + str(i))
    print("Директории успешно созданы")
except OSError:
    print('Такая директория уже существует')


# теперь удалим:
dir_path = os.path.join(os.getcwd(), 'dir_')
try:
    for d in range(1, 10):
        os.rmdir(dir_path + str(d))
    print("Директории успешно удалены")
except OSError:
    print("Дирректория уже удалена")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
 
print(os.listdir(os.getcwd()))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil 

filename = sys.argv[0]

def duplicate_file(filename):
    newfile = filename + '.(1)'
    shutil.copy(filename, newfile)
    if os.path.exists(newfile):    # ф-ия exists возвращает true если файл существует и false, если нет
        print("Файл %s был успешно создан" %newfile)
        return True
    else:
        print("Проблемы копирования")
        return False
duplicate_file(filename)