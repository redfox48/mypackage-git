# MODULE 1

print("module1.py's __name__: {}".format(__name__))
print("module1.py's __file__: {}".format(__file__))
print("module1.py's __package__: {}".format(__package__))

# Note: use absolute/explicit imports/namespaces
# generally preferred for clarity
from mypackage.module2 import function_a

def main():
    print("Running main")
    function_a()