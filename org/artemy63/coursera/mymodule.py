# import sys
#1variant works good
# import mypypackage.utils

#2variant works good
# from mypypackage.utils import *

#3variant
from mypypackage import utils

# print(sys.path)
# print(mypypackage)

if __name__ == "__main__":
    #1variant
    # print(mypypackage.utils.multiply(3,7))

    #2variant
    # print(multiply(3, 6))

    #3variant
    print(utils.multiply(5,6))
