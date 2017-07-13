"""
    Using Per-Record Pickle Files
As mentioned earlier, one potential disadvantage of this section’s examples so far is
that they may become slow for very large databases: because the entire database must
be loaded and rewritten to update a single record, this approach can waste time. We
could improve on this by storing each record in the database in a separate flat file. The
next three examples show one way to do so; Example 1-8 stores each record in its own
flat file, using each record’s original key as its filename with a .pkl appended (it creates
the files bob.pkl, sue.pkl, and tom.pkl in the current working directory).

"""
from initdata import bob, sue, tom
from initdata import db
import pickle
from pprint import pprint

pprint(db)
# {'bob': {'age': 42, 'job': 'dev', 'name': 'Bob Smith', 'pay': 30000},
#  'sue': {'age': 45, 'job': 'hdw', 'name': 'Sue Jones', 'pay': 40000},
#  'tom': {'age': 50, 'job': None, 'name': 'Tom', 'pay': 0}}

db = [('bob', bob), ('tom', tom), ('sue', sue)]
# [('bob', {'age': 42, 'job': 'dev', 'name': 'Bob Smith', 'pay': 30000}),
#  ('tom', {'age': 50, 'job': None, 'name': 'Tom', 'pay': 0}),
#  ('sue', {'age': 45, 'job': 'hdw', 'name': 'Sue Jones', 'pay': 40000})]

pprint(db)
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    # recfile = open(f'{key}.plk', 'wb')
    # pickle.dump(record, recfile)
    # recfile.close()

    # (it creates the files bob.pkl, sue.pkl, and tom.pkl in the current working directory
    with open(f'{key}.pkl', 'wb') as f:
        pickle.dump(record, f)

    # (it creates the files bob.txt, sue.txt, and tom.txt in the current working directory
    with open(f'{key}.txt', 'w') as f:
        pprint(record, f)
