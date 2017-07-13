import shelve

db = shelve.open('class-shelve')

for key in db:
    print(key, '=>\t', db[key].name, db[key].pay, sep='')

# bob=>	Bob Smith30000
# sue=>	Sue Jones40000
# tom=>	Tom Doe50000
