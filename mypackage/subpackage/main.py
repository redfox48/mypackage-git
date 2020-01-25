from subpackage.birds import Birds
from subpackage.mammals import Mammals

def main():
    birds = Birds()
    mammals = Mammals()

    birds.printMembers()
    mammals.printMembers()

if __name__ == '__main__':
    print("main: __name__: {}".format(__name__))
    print("main: __file__: {}".format(__file__))
    print("main: __package__: {}".format(__package__))

    main()