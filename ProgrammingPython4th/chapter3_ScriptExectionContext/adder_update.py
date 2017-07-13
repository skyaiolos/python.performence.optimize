import sys

sum = 0
while True:
    # or call sys.stdin.readlines()
    try:
        line = input('Enter numbers ->')
        if not line.isalnum():
            print("pls enter a number")
        else:
            sum += int(line)  # was sting.atoi() in 2nd ed

    except EOFError:  # or for line in sys.stdin:
        break  # input strips \n at end
print(sum)
