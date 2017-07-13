import pickle

# dbfile = open('people-pickle', 'rb')  # use binary mode files in 3.X
with open('people-pickle', 'rb') as f:
    db = pickle.load(f)
for key in db:
    print(key, '=>\n  ', db[key])
print(db['sue']['name'])
# bob =>
#    {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
# sue =>
#    {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
# tom =>
#    {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
# Sue Jones
