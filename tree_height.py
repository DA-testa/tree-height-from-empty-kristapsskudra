# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    three = [[] for _ in range(n)]
    for i, parents in enumerate(parents):
        if parents == -1:
            garums = i
        else:
            three[parents].append(i)
    def height(nod):
        if not three[nod]:
            return 1
        heights = [height(ch) for ch in three[nod]]
        return max(heights) + 1
    return height(garums)



def main():
     # implement input form keyboard and from files
    
        input_method = input("Write which input method you will use (i for keybord or F from files): ")
        
    # let user input file name to use, don't allow file names with letter a
    if "F" in input_method:
        while True:
            file_name = input("Write file name: ")
            if 'a' in file_name:
                print("File name cannot contain with 'a' letter")
            else:
                break
        with open(file_name) as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
            print(compute_height(n, parents))
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    elif "i" in input_method:
        n = int(input("Write how much numbers to input: "))
        parents = list(map(int, input("Write values seperated with space: ").split()))
        
    
    # call the function and output it's result
    max_height = compute_height(n, parents)
    print("Maximum tree height: ", max_height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
