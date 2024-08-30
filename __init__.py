import platform
import os
import sys
import tkinter as tk
from tkinter import messagebox

import count_start_program

class start_module_init:
    
    system = platform.system()
    if system == "Linux":
        with open('system','w') as fp:
            fp.write('Linux')

        if os.path.exists('main.py'):
            if os.path.exists('core.py'):
                print('init is true')
                print('Platform user = Linux')

                count_start_program.main()

            else:
                print('not found core.py')
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror('Error', 'Not found core.py')
                sys.exit()
        else:
            print('not found main.py')
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror('Error', 'Not found main.py')
            sys.exit()
    

    elif system == 'Windows':
        with open('system','w') as fp:
            fp.write('Windows')

        if os.path.exists('main.py'):
            if os.path.exists('core.py'):
                print('init is true')
                print('Platform user = Windows')

                count_start_program.main()
                
            else:
                print('not found core.py')
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror('Error', 'Not found core.py')
                sys.exit()
        else:
            print('not found main.py')
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror('Error', 'Not found main.py')
            sys.exit()
    
    else:
        print('Platform is not supported')
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror('Error', 'Platform is not supported')
        sys.exit()