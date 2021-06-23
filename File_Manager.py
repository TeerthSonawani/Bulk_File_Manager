import os

operation = input('''
choose an operation-1)Rename
                    2)Delete
                    3)Create
>>>''')
if operation == '1':
    Number = 0
    Stuff = os.listdir()
    Name = input('what should the files be renamed-')
    Extension = input('File Extension-')
    for lmao in Stuff:
            if lmao == 'File_Manager.py':
                pass
            else:
                os.rename(lmao,f'{Name}{Number}{Extension}')
                Number += 1
if operation == '3':
    Number = 0
    Amount = int(input('amount of files to be made-'))
    Name = input('what should the files be named-')
    Extension = input('File Extension-')
    for lmao in range(Amount):
        with open(f'{Name} {Number}{Extension}', 'w') as fp:
            pass
        Number +=1
if operation == '2':
    what = input('''
Please Select an option-1)delete using extension
                        2)delete using name
                        3)delete all files in the directory
''')
    if what == '1':
        ext = input('Which Extension-')
        Stuff = os.listdir()
        for items in Stuff:
            nameee = os.path.splitext(items)
            if nameee[1] == f'{ext}':
                os.remove(items)
    if what == '2':
        Number = 0
        Stuff = os.listdir()
        namee = input('what name-')
        ext = input('Extension -')
        for items in Stuff:
            Stuff = os.listdir()
            if items == f'{namee} {Number}{ext}':
                os.remove(items)
                Number += 1
            else:
                Number += 1
    if what == '3':
        Number = 0
        Stuff = os.listdir()
        for items in Stuff:
            if items == 'File_Manager.py':
                pass
            else:
                os.remove(items)
            Number += 1
if operation == '4':
    Number = 0
    dst = os.path.abspath(os.getcwd())
    src = input('Which file should be duplicated-')
    amount = int(input('How many copies-'))
    names = input('do you want different names?-')
    if names.upper() == 'YES':
        name = input('what should the name be-')
    for items in range(amount):
        ext = os.path.splitext(src)
        copy(src, f'{ext[0]} {Number}{ext[1]}')
        Number += 1 
        
    
    
