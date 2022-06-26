with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')

'''context manager: https://book.pythontips.com/en/latest/context_managers.html
el codigo de arriba es igual q:

file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

ya q la CLASE file tiene metodos enter y exit con gestion de excps'''
