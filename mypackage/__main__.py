"""
Code to be run when run from command line using any of the following
python mypackage
python - m mypackage
python mypkg.zip
"""

print("package0: __name__: {}".format(__name__))
print("package0: __file__: {}".format(__file__))
print("package0: __package__: {}".format(__package__))

from mypackage import module1

if __name__ == "__main__":
    """Entry point for __main__ """
    module1.main()