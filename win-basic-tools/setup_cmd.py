import os

def main():
    program_path = os.getcwd()
    home_path = os.path.expanduser('~')

    with open(f'{home_path}\\.macros.doskey', 'a') as file:
        file.write(
            f'''ls=python {program_path}\\sources\\ls.py $1 $2\n
            ll=python {program_path}\\sources\\ls.py -lac\n
            which=python {program_path}\\sources\\which.py $1\n
            cat=type $1\n
            pwd=cd\n
            mv=move $1 $2\n
            rm=del $*\n''')
        
        
    os.system(f'reg add "HKCU\\Software\\Microsoft\\Command Processor" /v Autorun /d "doskey /macrofile=\\"{home_path}\\.macros.doskey\"" /f')

if __name__ == '__main__':
    main()