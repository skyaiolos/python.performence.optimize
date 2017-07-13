"collect command-line options in a dictionary"

"""
    Parsing Command-Line Arguments
Once you start using command-line arguments regularly, though, you’ll probably find
it inconvenient to keep writing code that fishes through the list looking for words. More
typically, programs translate the arguments list on startup into structures that are more
conveniently processed. Here’s one way to do it: the script in Example 3-2 scans the
argv list looking for  -optionname optionvalue word pairs and stuffs them into a dic-
tionary by option name for easy retrieval.
"""

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':  # find "-name value" pairs
            opts[argv[0]] = argv[1]  # dict key is "-name" arg
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts


if __name__ == '__main__':
    from sys import argv  # example client code

    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)

# C:\...\PP4E\System> python testargv2.py
# {}
# C:\...\PP4E\System> python testargv2.py -i data.txt -o results.txt
# data.txt
# {'-o': 'results.txt', '-i': 'data.txt'}
