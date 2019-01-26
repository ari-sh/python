
__author__ = 'Шонтукова Арина Артуровна'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.path.dirname(
        os.path.abspath(os.path.realpath(__file__))), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

file_name = input("Введите имя файла: ")
def cp_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.path.dirname(
        os.path.abspath(os.path.realpath(__file__))), file_name)
    if os.path.isfile(file_path):
        shutil.copy(file_path, file_name + '.(1)')
        if os.path.exists(file_path):
            print("Файл {} был успешно создан".format(file_name + '.(1)'))
            return True
        else:
            print("Проблемы копирования")
            return False

file_name = input("Введите имя файла: ")
def rm_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.path.dirname(
        os.path.abspath(os.path.realpath(__file__))), file_name)
    if os.path.isfile(file_path):
        user_agree = input("Вы уврены, что хотите удалить файл %s: Yes/No" %file_name)
        if user_agree == 'Yes':
            os.remove(file_path)
            print("Файл %s удален" %file_name)
        elif user_agree == 'No':
            print("Отмена удаления файла")
    else:
        print("Выбранный объект - не файл")


def cd():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.path.dirname(
        os.path.abspath(os.path.realpath(__file__))), dir_name)
    try:
        os.chdir(dir_path)
        print("Вы перешли в нужную папку")
    except OSError:
        print("Перейти в выбранную папке не возможно")


def ls():
    print(os.path.abspath(os.getcwd()))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_file,
    "rm": rm_file,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None


try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")