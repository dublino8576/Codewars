'''
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false 
'''

#My solution
def is_triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False
a = 2
b = 2
c = 2
print(is_triangle(a, b, c))
