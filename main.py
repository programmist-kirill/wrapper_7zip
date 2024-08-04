import core

core.init()

directory = input('директория до архива: ')
extract_directory = input('директория для распаковки: ')
directory_create = input('директория для создания скрипта: ')

core.write_script_linux.write(directory,extract_directory,directory_create)