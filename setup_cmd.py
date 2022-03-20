import os


program_path = os.getcwd()
home_path = os.path.expanduser('~')

with open(f'{home_path}\\.macros.doskey', 'a') as file:
    file.write(f'ls=python {program_path}\\sources\\ls.py $1 $2\n')
    file.write(f'll=python {program_path}\\sources\\ls.py -lac')

os.system(f'reg add "HKCU\\Software\\Microsoft\\Command Processor" /v Autorun /d "doskey /macrofile=\\"{home_path}\\.macros.doskey\"" /f')