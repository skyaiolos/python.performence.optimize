class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


def main():
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(f"bob's full name is {bob.name},\t sue's pay is {sue.pay}")
    print(f"bob's last name is : {bob.name.split()[-1]}")

    sue.pay *= 1.10
    print(sue.pay)


if __name__ == '__main__':
    main()

# bob's full name is Bob Smith,	 sue's pay is 40000
# bob's last name is : Smith
# 44000.0
