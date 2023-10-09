import numpy as np

# This is the whole function implementation
def gradient_descent(A,d, current_point, alpha):

    new_point = current_point - alpha * (A@current_point + d)
    while not np.allclose(current_point, new_point):
        current_point = new_point
        new_point = current_point - alpha * (A@current_point + d)
    return new_point

# now, I am running the function
current_point = np.zeros(2)
A = np.array([[6,-2],[-2,6]])
d = np.array([-1,-1])
alpha = 0.1
print(f"The minimum is {gradient_descent(A,d,current_point, alpha)}\nThis result agrees with what we found numerically")
