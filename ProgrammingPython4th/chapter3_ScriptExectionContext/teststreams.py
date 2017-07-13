"""
Redirecting Streams to Files and Programs
Technically, standard output (and  print ) text appears in the console window where a
program was started, standard input (and  input ) text comes from the keyboard, and
standard error text is used to print Python error messages to the console window. At
least that’s the default. It’s also possible to redirect these streams both to files and to
other programs at the system shell, as well as to arbitrary objects within a Python script.
On most systems, such redirections make it easy to reuse and combine general-purpose
command-line utilities.
Redirection is useful for things like canned (precoded) test inputs: we can apply a single
test script to any set of inputs by simply redirecting the standard input stream to a
different file each time the script is run. Similarly, redirecting the standard output
stream lets us save and later analyze a program’s output; for example, testing systems
might compare the saved standard output of a script with a file of expected output to
detect failures.
Although it’s a powerful paradigm, redirection turns out to be straightforward to use.
For instance, consider the simple read-evaluate-print loop program in Example 3-5.

"""
"read numbers till eof and show squares"


def interact():
    print('Hello stream world')  # print sends to sys.stdout
    while True:
        try:
            reply = input('Enter a number (type "exit" or "e" you can quit the loop)>')  # input reads sys.stdin
            if reply in ['exit', 'e']:
                break
        except EOFError:
            break  # raises an except on eof
        else:  # input given as a string
            num = int(reply)
            print("%d squared is %d" % (num, num ** 2))
    print('Bye')


if __name__ == '__main__':
    interact()  # when run, not imported
