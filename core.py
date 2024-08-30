import os

import __init__

class init:
    __init__.start_module_init()


class archiving:
    def write_is_password(password , directory_to_file_or_folder , what_is_name_archive , compression_ratio , directory_create_is_script):

        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7z a -tzip -ssw -mx' + compression_ratio + ' -p' + password + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7z a -tzip -ssw -mx' + compression_ratio + ' -p' + password + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)

    def write_no_password(directory_to_file_or_folder , what_is_name_archive , compression_ratio , directory_create_is_script):

        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7z a -tzip -ssw -mx' + compression_ratio + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7z a -tzip -ssw -mx' + compression_ratio + ' ' + what_is_name_archive + ' ' + directory_to_file_or_folder
                fp.write(commande)


class extract:
    def write_is_password(password , directory_to_archive , directory_to_extract , directory_create_is_script):

        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7z x -p' + password + ' ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7z x -p' + password + ' ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)
    

    def write_no_password(directory_to_archive , directory_to_extract , directory_create_is_script):
    
        if directory_create_is_script == 'abc':
            with open('script.sh','w') as fp:
                commande = '7z x ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)

        else:
            with open(directory_create_is_script + '/script.sh','w') as fp:
                commande = '7z x ' + directory_to_archive + ' -o' + directory_to_extract
                fp.write(commande)