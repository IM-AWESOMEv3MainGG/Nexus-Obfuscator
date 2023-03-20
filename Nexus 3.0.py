import marshal, zlib, base64, os, lzma, shutil, time
def Compile():
    parent = os.getcwd()
    shutil.copy2(f'{parent}\obfuscated1.py',f'{parent}\decompiledscript.py')
    os.remove(f'{parent}\obfuscated1.py')
    main_choice = int(input('''
(1) Console Open
(2) Windowed (no console, runs in the background)
>> '''))
    if main_choice == 1:
        os.system('pip install pyinstaller')
        os.system(f'pyinstaller --noconfirm --onefile --console  "{parent}\decompiledscript.py"')
        os.remove(f'{parent}\decompiledscript.spec')
        shutil.copy2(f'{parent}\dist\decompiledscript.exe', f'{parent}\decompiledscript.exe')
        shutil.rmtree(f'{parent}\\build', ignore_errors=True)
        shutil.rmtree(f'{parent}\\dist', ignore_errors=True)
        os.system('cls')
        print('Compiled script!')
        time.sleep(3)
    if main_choice == 2:
        os.system('pip install pyinstaller')
        os.system(f'pyinstaller --noconfirm --onefile --windowed  "{parent}\decompiledscript.py"')
        os.remove(f'{parent}\decompiledscript.spec')
        shutil.copy2(f'{parent}\dist\decompiledscript.exe', f'{parent}\decompiledscript.exe')
        shutil.rmtree(f'{parent}\\build', ignore_errors=True)
        shutil.rmtree(f'{parent}\\dist', ignore_errors=True)
        os.system('cls')
        print('Compiled script!')
        time.sleep(3)
    if main_choice is not[1,2]:
        print('u mustve mistyped on ur keyboard cuz that isnt 1 or 2')
def ObfuscateLevel1():
    with open('script-here.txt', 'r',errors='ignore') as f:
        mysrc = f.read()
    marsrc = compile(mysrc, 'coduter', 'exec')
    encode1 = marshal.dumps(marsrc)
    encode2 = zlib.compress(encode1)
    encode3 = lzma.compress(encode2)
    encode4 = base64.b64encode(encode3)
    me = '__'
    n = 0
    while n < 75:
        n += 1
        me += 'NEXUS_VERSION_3__'
    me += f' = ""'
    realcode = f'## Obfuscated by Nexus lol\n## Github: https://github.com/IM-AWESOMEv3MainGG/Nexus-Obfuscator \nimport marshal, zlib, base64, lzma'
    with open('importshere.txt', 'r',errors='ignore') as f:
        AwesomeSauce = f.read()
    realcode += f'\n{AwesomeSauce}'
    x = 0
    while x < 150:
        x += 1
        realcode += '\n'+str(me)
    realcode += f'\nexec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode({encode4})))))'
    realcode += '\n'+str(me)
    L = [str(realcode)]
    with open("script-here.txt", "w") as file1:
        file1.writelines(L)
    parent = os.getcwd()
    shutil.copy2(f'{parent}\script-here.txt',f'{parent}\copy.txt')
    f = open("script-here.txt", "r+")
    f.truncate(0)
    os.rename(f'{parent}\copy.txt', f'obfuscated1.py')
    compile_choice = input("Compile script? (Y/N)")
    if compile_choice == 'y':
        Compile()
    if compile_choice == 'n':
        print('Exiting program...')
        time.sleep(3)
    if compile_choice == 'Y':
        Compile()
    if compile_choice == 'N':
        print('Exiting program...')
        time.sleep(3)
    elif compile_choice is not['y', 'n', 'Y', 'N']:
        print('Invalid choice! Only use y/n and Y/N.')
def ObfuscateLevel2():
    with open('script-here.txt', 'r',errors='ignore') as f:
        mysrc = f.read()
    marsrc = compile(mysrc, 'coduter', 'exec')
    encode1 = marshal.dumps(marsrc)
    encode2 = zlib.compress(encode1)
    encode3 = lzma.compress(encode2)
    encode4 = base64.b64encode(encode3)
    encode5 = base64.b85encode(encode4)
    me = '__'
    n = 0
    while n < 75:
        n += 1
        me += 'NEXUS_VERSION_3__'
    me += f' = ""'
    realcode = f'## Obfuscated by Nexus lol\n## Github: https://github.com/IM-AWESOMEv3MainGG/Nexus-Obfuscator \nimport marshal, zlib, base64, lzma'
    with open('importshere.txt', 'r',errors='ignore') as f:
        AwesomeSauce = f.read()
    realcode += f'\n{AwesomeSauce}'
    x = 0
    while x < 150:
        x += 1
        realcode += '\n'+str(me)
    realcode += f'\nexec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b85decode({encode5}))))))'
    realcode += '\n'+str(me)
    L = [str(realcode)]
    with open("script-here.txt", "w") as file1:
        file1.writelines(L)
    parent = os.getcwd()
    shutil.copy2(f'{parent}\script-here.txt',f'{parent}\copy.txt')
    f = open("script-here.txt", "r+")
    f.truncate(0)
    os.rename(f'{parent}\copy.txt', f'obfuscated1.py')
    compile_choice = input("Compile script? (Y/N)")
    if compile_choice == 'y':
        Compile()
    if compile_choice == 'n':
        print('Exiting program...')
        time.sleep(3)
    if compile_choice == 'Y':
        Compile()
    if compile_choice == 'N':
        print('Exiting program...')
        time.sleep(3)
    elif compile_choice is not['y', 'n', 'Y', 'N']:
        print('Invalid choice! Only use y/n and Y/N.')
def ObfuscateLevel3():
    with open('script-here.txt', 'r',errors='ignore') as f:
        mysrc = f.read()
    marsrc = compile(mysrc, 'coduter', 'exec')
    encode1 = marshal.dumps(marsrc)
    encode2 = zlib.compress(encode1)
    encode3 = lzma.compress(encode2)
    encode4 = base64.b64encode(encode3)
    encode5 = base64.b85encode(encode4)
    encode6 = base64.b32encode(encode5)
    me = '__'
    n = 0
    while n < 75:
        n += 1
        me += 'NEXUS_VERSION_3__'
    me += f' = ""'
    realcode = f'## Obfuscated by Nexus lol\n## Github: https://github.com/IM-AWESOMEv3MainGG/Nexus-Obfuscator \nimport marshal, zlib, base64, lzma'
    with open('importshere.txt', 'r',errors='ignore') as f:
        AwesomeSauce = f.read()
    realcode += f'\n{AwesomeSauce}'
    x = 0
    while x < 150:
        x += 1
        realcode += '\n'+str(me)
    realcode += f'\nexec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b85decode(base64.b32decode({encode5})))))))'
    realcode += '\n'+str(me)
    L = [str(realcode)]
    with open("script-here.txt", "w") as file1:
        file1.writelines(L)
    parent = os.getcwd()
    shutil.copy2(f'{parent}\script-here.txt',f'{parent}\copy.txt')
    f = open("script-here.txt", "r+")
    f.truncate(0)
    os.rename(f'{parent}\copy.txt', f'obfuscated1.py')
    compile_choice = input("Compile script? (Y/N)")
    if compile_choice == 'y':
        Compile()
    if compile_choice == 'n':
        print('Exiting program...')
        time.sleep(3)
    if compile_choice == 'Y':
        Compile()
    if compile_choice == 'N':
        print('Exiting program...')
        time.sleep(3)
    elif compile_choice is not['y', 'n', 'Y', 'N']:
        print('Invalid choice! Only use y/n and Y/N.')
def ObfuscateLevel4():
    with open('script-here.txt', 'r',errors='ignore') as f:
        mysrc = f.read()
    marsrc = compile(mysrc, 'coduter', 'exec')
    encode1 = marshal.dumps(marsrc)
    encode2 = zlib.compress(encode1)
    encode3 = lzma.compress(encode2)
    encode4 = base64.b64encode(encode3)
    encode5 = base64.b85encode(encode4)
    encode6 = base64.b32encode(encode5)
    encode7 = base64.b16encode(encode6)
    me = '__'
    n = 0
    while n < 75:
        n += 1
        me += 'NEXUS_VERSION_3__'
    me += f' = ""'
    realcode = f'## Obfuscated by Nexus lol\n## Github: https://github.com/IM-AWESOMEv3MainGG/Nexus-Obfuscator \nimport marshal, zlib, base64, lzma'
    with open('importshere.txt', 'r',errors='ignore') as f:
        AwesomeSauce = f.read()
    realcode += f'\n{AwesomeSauce}'
    x = 0
    while x < 150:
        x += 1
        realcode += '\n'+str(me)
    realcode += f'\nexec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b85decode(base64.b32decode(base64.b16decode{encode5})))))))'
    realcode += '\n'+str(me)
    L = [str(realcode)]
    with open("script-here.txt", "w") as file1:
        file1.writelines(L)
    parent = os.getcwd()
    shutil.copy2(f'{parent}\script-here.txt',f'{parent}\copy.txt')
    f = open("script-here.txt", "r+")
    f.truncate(0)
    os.rename(f'{parent}\copy.txt', f'obfuscated1.py')
    compile_choice = input("Compile script? (Y/N)")
    if compile_choice == 'y':
        Compile()
    if compile_choice == 'n':
        print('Exiting program...')
        time.sleep(3)
    if compile_choice == 'Y':
        Compile()
    if compile_choice == 'N':
        print('Exiting program...')
        time.sleep(3)
    elif compile_choice is not['y', 'n', 'Y', 'N']:
        print('Invalid choice! Only use y/n and Y/N.')
        time.sleep(3)
if __name__ == '__main__':
    print(
"""
VeryVeryCool123#0686 - Nexus 3.0 - https://github.com/IM-AWESOMEv3MainGG/Nexus-Obfuscator
888b    888 8888888888 Y88b   d88P 888     888  .d8888b.        .d8888b.       .d8888b.  
8888b   888 888         Y88b d88P  888     888 d88P  Y88b      d88P  Y88b     d88P  Y88b 
88888b  888 888          Y88o88P   888     888 Y88b.                .d88P     888    888 
888Y88b 888 8888888       Y888P    888     888  "Y888b.            8888"      888    888 
888 Y88b888 888           d888b    888     888     "Y88b.           "Y8b.     888    888 
888  Y88888 888          d88888b   888     888       "888      888    888     888    888 
888   Y8888 888         d88P Y88b  Y88b. .d88P Y88b  d88P      Y88b  d88P d8b Y88b  d88P 
888    Y888 8888888888 d88P   Y88b  "Y88888P"   "Y8888P"        "Y8888P"  Y8P  "Y8888P"  
""")
    main_choice = int(input('Enter obfuscation level (1-4)'))
    if main_choice == 1:
        ObfuscateLevel1()
    if main_choice == 2:
        ObfuscateLevel2()
    if main_choice == 3:
        ObfuscateLevel3()
    if main_choice == 4:
        ObfuscateLevel4()
    elif main_choice is not[1,2,3,4]:
        print('Invalid choice!')
        time.sleep(3)