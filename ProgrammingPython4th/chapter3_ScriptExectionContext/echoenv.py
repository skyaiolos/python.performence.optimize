import os

print('echoenv...', end=' ')

# if os.environ.get('USERNAME') == None or "none":
try:
    if os.environ.get('USERNAME') in [None, 'None', 'none']:
        print("Please input the Name for USERNAME.")

    else:
        print('Hello,', os.environ['USERNAME'])

except KeyError as e:
    print(e)
