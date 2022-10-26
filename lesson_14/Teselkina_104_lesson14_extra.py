import os
import shutil


def sort_files(path):  # объявляем функцию с одним параметром
    os.chdir(path)  # изменяем текуший директорий
    list_ = os.listdir(path)  # создаем список файлов из директории

    for i in list_:  # цикл
        try:  # блок когда, где могут возникнуть исключения
            if '.docx' in i:
                shutil.move(path + '\\' + i, r'D:\сортированные файлы\docx')  # перемещаем файл

            elif '.py' in i:
                shutil.move(path + '\\' + i, r'D:\сортированные файлы\py')

            elif '.exe' in i:
                shutil.move(path + '\\' + i, r'D:\сортированные файлы\exe')

            elif '.rtf' in i:
                shutil.move(path + '\\' + i, r'D:\сортированные файлы\rtf')

            elif '.ini' in i:
                shutil.move(path + '\\' + i, r'D:\сортированные файлы\ini')

            elif '.pdf' in i:
                shutil.move(path + '\\' + i, r'D:\сортированные файлы\pdf')

            elif '.xlsx' in i:
                shutil.move(path + '\\' + i, r'D:\сортированные файлы\xlsx')
        except shutil.Error:  # если возникает исключение
            os.remove(path + '\\' + i)  # удаляем файл


path_1 = r'd:\-=Документы=-\Downloads'
path_2 = r'd:\-=Документы=-\Downloads\Telegram Desktop'
sort_files(path_1)
sort_files(path_2)
