import core

from getpass import getpass
import os

core.init()

class main_archiving:
    def create_archive_is_password():

        with open('count_start_program.log','r') as file:
            count_start_program = int(file.read())
        
        if count_start_program == 1:
            print('В целях безопасности пароль не будет виден')
            password = getpass('Введите пароль:')

        else:
            password = getpass('Введите пароль:')

        
        directory_to_file_or_folder = input('директория до файла или директории: ')
        if os.path.exists(directory_to_file_or_folder):
            print('directory found')
        else:
            print('directory not found')
            
            a = True
            while a == True:
                directory_to_file_or_folder = input('директория до файла или директории: ')
                if os.path.exists(directory_to_file_or_folder):
                    print('directory found')
                    a = False
                    break
                else:
                    print('directory not found')
                    a = False
                    continue
        
        compression_ratio = input('Введите степень сжатия от 1 до 9(1 - быстрое сжатие , 9 - медленное сжатие): ')

        what_is_name_archive = input('как будет называться архив(без расширения): ')

        directory_create_is_script = input('где хотите создать скрипт(если хотите создать скрипт в корне введите - abc): ')

        core.archiving.write_is_password(password,directory_to_file_or_folder,what_is_name_archive,compression_ratio,directory_create_is_script)



    def create_archive_no_password():

        compression_ratio = input('Введите степень сжатия от 1 до 9(1 - быстрое сжатие , 9 - медленное сжатие): ')

        directory_to_file_or_folder = input('директория до файла или директории: ')
        if os.path.exists(directory_to_file_or_folder):
            print('directory found')
        else:
            print('directory not found')
            
            a = True
            while a == True:
                directory_to_file_or_folder = input('директория до файла или директории: ')
                if os.path.exists(directory_to_file_or_folder):
                    print('directory found')
                    a = False
                    break
                else:
                    print('directory not found')
                    a = False
                    continue

        what_is_name_archive = input('как будет называться архив(без расширения): ')

        directory_create_is_script = input('где хотите создать скрипт(если хотите создать скрипт в корне введите - abc): ')

        core.archiving.write_no_password(directory_to_file_or_folder,what_is_name_archive,compression_ratio,directory_create_is_script)



class main_extract:
    def extract_archive_is_password():
        
        with open('count_start_program.log','r') as file:
            count_start_program = int(file.read())

        if count_start_program == 1:
            print('В целях безопасности пароль не будет виден')
            password = getpass('Введите пароль:')
            
        else:
            password = getpass('Введите пароль:')

        directory_to_archive = input('директория до архива: ')

        directory_to_extract = input('директория для распаковки: ')

        directory_create_is_script = input('где хотите создать скрипт(если хотите создать скрипт в корне введите - abc): ')

        core.extract.write_is_password(password,directory_to_archive,directory_to_extract,directory_create_is_script)
    

    def extract_archive_no_password():

        directory_to_archive = input('директория до архива: ')

        directory_to_extract = input('директория для распаковки: ')

        directory_create_is_script = input('где хотите создать скрипт(если хотите создать скрипт в корне введите - abc): ')

        core.extract.write_no_password(directory_to_archive,directory_to_extract,directory_create_is_script)
