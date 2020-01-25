from mypackage.subpackage.mammals import Mammals
from mypackage.subpackage.birds import Birds
 
def run():
    # Create an object of Mammals class & call a method of it
    myMammal = Mammals()
    myMammal.printMembers()
    
    # Create an object of Birds class & call a method of it
    myBird = Birds()
    myBird.printMembers()

    return True