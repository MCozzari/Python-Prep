import sys

if len(sys.argv)==4:
    print("El primer parametro es:", sys.argv[1])
    print("El segundo parametro es:", sys.argv[2])
    print("El tercer parametro es:", sys.argv[3])
else:
    print("La cantidad de parametro introducida es incorrecta, debe introducir 3")