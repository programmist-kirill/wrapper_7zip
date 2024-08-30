import os

def main():
    if not os.path.exists('count_start_program.log'):
        with open('count_start_program.log','w') as file:
            file.write('1')

    else:
        with open('count_start_program.log','r') as file:
            count_start_program = int(file.read()) + 1

        with open('count_start_program.log','w') as file:
            file.write(str(count_start_program))