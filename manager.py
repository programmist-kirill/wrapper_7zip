import main

action = input('1 = создать архив\n2 = распаковать архив\n')
if action == '1':
    password_or_no_password = input('1 = c паролем\n2 = без пароля\n')

    if password_or_no_password == '1':
        main.main_archiving.create_archive_is_password()

    elif password_or_no_password == '2':
        main.main_archiving.create_archive_no_password()

elif action == '2':
    password_or_no_password = input('1 = c паролем\n2 = без пароля\n')

    if password_or_no_password == '1':
        main.main_extract.extract_archive_is_password()

    elif password_or_no_password == '2':
        main.main_extract.extract_archive_no_password()