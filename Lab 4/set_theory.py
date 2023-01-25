
# You are not allowed to import any modules whatsoever

# Assume a set is represented as a Python list

# Do not modify these
A = [1, 2, 5, 8, 12, 5]
B = [3, 5, 7, 8, 11, 3]



# Define a function that takes in a set, represented as a Python list,
# and returns an equivalent set with all duplicates removed
def simplify(A):
# Provide your code here...


    A2 = []

    
    return list(set(A) - set(A2))

# Testing the simplify function
print("Simplify Function:")
print ("A = ", simplify(A))
print ("B = ", simplify(B) )
print ("")
# Expected:
# A =  [1, 2, 5, 8, 12]
# B =  [3, 5, 7, 8, 11]

print



# Define a function that takes in two sets and returns their union.
# The resulting set should be a Python list with no duplicates
def union(A, B):
    # Provide your code here...
   return list(set(A) | set(B))



# Testing the union function
print ("Union function")
print ("A union B = ", union(A, B))
print("")

# Expected:
# A union B =  [1, 2, 5, 8, 12, 3, 7, 11]

print



# Define a function that takes in two sets and returns their intersection.
# The resulting set should be a Python list with no duplicates
def intersection(A, B):
    # Provide your code here...

    
    return list(set(B) & set(A))

# Testing the intersection function
print("Intersection Function")
print ("A intersection B = ", intersection(A,B))
print("")
# Expected:
# A intersection B =  [5, 8]

print



# Define a function that takes in two sets, A and B, and returns True
# if A is a subset of B, and False otherwise
def subset(A, B):
    # Provide your code here...


    
    if set(A) .issubset(B):
        return True
    else:
        return False

# Testing the subset function
print("Subset Function")
print ("A subset of B:", subset(A, B))
print ("[5, 7, 8] subset of B:", subset([5,7,8], B))
print("")


# Expected:
# A subset of B: False
# [5, 7, 8] subset of B: True

print



# Define a function that takes in two sets and returns True
# if they are equal, and False otherwise
def equal(A, B):
    # Provide your code here...

    
    if set(A) == set(B):
        return True
    
# Testing the equal function
print ("Equal Function")
print ("A == B:", equal(A, B))
print ("[1, 2, 3, 4] == [1, 1, 2, 2, 4, 2, 3, 3]:", equal([1, 2, 3, 4],[1, 1, 2, 2, 4, 2, 3, 3]))
print("")
# Expected:
# A == B: False
# [1, 2, 3, 4] == [1, 1, 2, 2, 4, 2, 3, 3]: True

print



# Define a function that takes in two sets and returns their Cartesian product
# The result should be represented as a list of tuples, ex: [(1, 1), (1, 2), ...]
def cartesian_product(A, B):
    
    # Provide your code here...
    cProduct = []

    for num in simplify(A):
        for num1 in simplify(B):
            cProduct.append((num, num1))

    return cProduct

# Testing the cartesian_product function
print ("Cartesian Product Function")
print ("[1] x B =", cartesian_product([1], B))
print ("[1, 2] x B =", cartesian_product([1, 2], B))
print ("[] x B =", cartesian_product([], B))
print("")
# Expected:
# [1] x B =  [(1, 3), (1, 5), (1, 7), (1, 8), (1, 11)]
# [1, 2] x B =  [(1, 3), (1, 5), (1, 7), (1, 8), (1, 11), (2, 3), (2, 5), (2, 7), (2, 8), (2, 11)]
# [] x B =  []

print

