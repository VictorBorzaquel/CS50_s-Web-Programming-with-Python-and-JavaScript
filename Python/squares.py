# Import one function
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

# Import all function
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")