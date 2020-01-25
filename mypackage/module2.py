# MODULE 2

print("module1.py's __name__: {}".format(__name__))
print("module1.py's __file__: {}".format(__file__))
print("module1.py's __package__: {}".format(__package__))

from mypackage.subpackage import birds

def function_a():
    print("Doing function_a")
    thesebirds = birds.Birds()
    thesebirds.printMembers()

def function_b():
    print("Doing function_b")