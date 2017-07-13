import pickle, glob

for filename in glob.glob('*.pkl'):  # for 'bob','sue','tom'
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\t  ', record)

print()
sue_file = open('sue.pkl', 'rb')
print("Sue's full name is: " + pickle.load(sue_file)['name'])  # fetch sue's name

print()
bob_file = open('bob.pkl', 'rb')
print(f"bob's pay is: {pickle.load(bob_file)['pay']}")

print()
tom_file = open('tom.pkl', 'rb')
print("tom's age is: ", pickle.load(tom_file)['age'])

# bob.pkl =>	   {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
# sue.pkl =>	   {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
# tom.pkl =>	   {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
#
# Sue's full name is: Sue Jones
#
# bob's pay is: 30000
#
# tom's age is:  50
