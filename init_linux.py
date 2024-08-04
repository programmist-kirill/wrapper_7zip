import platform
import os

class start_module_init_linux:
    system = platform.system()
    if system == "Linux":
        if not os.path.exists('name_user'):

            print('whoami - для того чтобы получить название пользователя')
            name_user = input('название пользователя: ')
            with open('name_user','w') as fp:
                fp.write(name_user)

        else:
            print('init is true')
            print('Platform user = Linux')