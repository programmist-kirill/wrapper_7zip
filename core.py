import os
import time
import platform

import init_linux

class init:
    system = platform.system()

    if system == "Linux":
        init_linux.start_module_init_linux()

    else:
        print('unknown system')

class write_script_linux:
    def write(directory,extract_directory,directory_create):
        with open(directory_create + '/script.sh','w') as fp:
            commande = '7z x ' + directory + ' -o' + extract_directory
            fp.write(commande)
