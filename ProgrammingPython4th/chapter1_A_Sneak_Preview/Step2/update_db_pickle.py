import pickle
from pprint import pprint

# dbfile = open('people-pickle', 'rb')
# db = pickle.load(dbfile)
# dbfile.close()
with open('people-pickle', 'rb') as f:
    db = pickle.load(f)

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

# dbfile = open('people-pickle', 'wb')
# pickle.dump(db, dbfile)
# dbfile.close()
with open('people-pickle', 'wb') as f:
    pickle.dump(db, f)
    pprint(db)

# {'bob': {'age': 42, 'job': 'dev', 'name': 'Bob Smith', 'pay': 30000},
#  'sue': {'age': 45,
#          'job': 'hdw',
#          'name': 'Sue Jones',
#          'pay': 70862.44000000005},
#  'tom': {'age': 50, 'job': None, 'name': 'Tom Tom', 'pay': 0}}

