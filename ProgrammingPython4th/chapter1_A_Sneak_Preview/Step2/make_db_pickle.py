from initdata import db
import pickle

# dbfile = open()  # use binary mode files in 3.X
# pickle.dump(db, dbfile)  # data is bytes, not str
# dbfile.close()
with open('people-pickle', 'wb') as f:  # use binary mode files in 3.X
    pickle.dump(db, f)  # data is bytes, not str
