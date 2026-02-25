# 1a) Dictionary
# 1b) List of Tuple
# 1c) Numpy Array

# 2a) 7 2b)7 2c) 33 2d) 4

# Question 3

from numpy import float32, sqrt, float64, cos, arange, sin
import numpy as np
import warnings
import matplotlib.pyplot as plt
import random

warnings.filterwarnings('error', category=RuntimeWarning)

def function3(x):
    try:
        output = 1/((sqrt(pow(x,2)+1))-x)
    
    except (RuntimeWarning, Exception):
        return None
    
    return output

    
def solution3a():
    largest_n = 0
    for n in range(20):
        input = float32(pow(10, n))
        
        if function3(input) == None:
            return largest_n
        else:
            largest_n = n
            
def solution3b():
    largest_n = 0
    for n in range(20):
        input = float64(pow(10,n))
        
        if function3(input) == None:
            return largest_n
        else:
            largest_n = n
            
            
# For question 4, a) e ,b) 2e, c) 2e ,d)2e

# For question 5, a) O(n), b) O(n**2) c) O(n) d) O(n**2)

def integral(f, a, b, xi, wi):
    sum_terms = 0
    val = 0
    
    for n in range(len(xi)):
        for s in range(len(f)):
            val += f[s]*xi[n]**s
            
        sum_terms += wi[n] * val
        val = 0
        
    return (b-a)*sum_terms
        
def solution6():
    f = [0, 0, 1, 1]
    
    a = 0
    b = 10
    
    sixa = integral(f, a, b, [a, b], [1/2, 1/2])
    sixb = integral(f, a, b,[a,(a+b)/2, b], [1/6, 2/3, 1/6])
    sixc = integral(f, a, b,[(a+b+(b-a)/sqrt(3))/2 ,(a+b-(b-a)/sqrt(3))/2], [1/2, 1/2])
    print("solution 6a:", sixa)
    print("solution 6b:", sixb)
    print("solution 6c:", sixc)
    
    # Compare with exact
    
    exact = 8500/3
    
    print("difference 6a:", sixa -exact)
    print("difference 6b:", sixb -exact)
    print("difference 6c:", sixc -exact)


def friction(v):
    if v < 0:
        return 0.025
    elif v > 0:
        return -0.025
    else:
        return 0
    
def solve7(t1, t2, deltat, m, k, f, x0, x1):
    
    x_list = []
    for _ in range(int((t2-t1)/deltat)):
        x2 = (f*deltat**2)/m - x1*k*deltat**2 + 2*x1 - x0   
        v = (x1 - x0)/deltat
        f = friction(v)
        x_list.append(x2)
        x0 = x1
        x1 = x2
        
    return x_list

def solution7():
    t1 = 0
    t2 = 20
    deltat = 0.01
    m = 1
    k = 40
    f = 0.025
    x0 = 0.01
    x1 = 0.01
    x = solve7(t1, t2, deltat, m, k , f, x0 ,x1)
    
    
    time = arange(0, 20.00, 0.01)       
    analytical_x = 0.01*cos(sqrt(k/m)*time)
    plt.plot(time, x)
    plt.plot(time, analytical_x)
    plt.xlabel("time")
    plt.ylabel("x")
    plt.savefig("sol7.png")
    
    
def monte_carlo_integration(f, n, x, y, a, b):
    
    mean_height = 0
    
    for iter in range(n):
        mean_height += f(x[iter], y[iter])
        
    integral_f = mean_height*4*a*b/n
    
    return integral_f

def monte_carlo_integration_circle(f, n, x, a, b):
    
    mean_height = 0
    x = np.array(x)
    y = x
    
    for iter in range(n):
        mean_height += f(x[iter], y[iter])
        
    integral_f = mean_height*4*a*b/n
    
    return integral_f

def fx(x,y):
    return ((cos(y))**2)*(sin(x**2))*np.exp(x*y)

def circle(x, y):
    return x**2 + y**2

def solution8():
    b = 1
    a = 1
    n = 1000000
    x = [random.uniform(-a, a) for _ in range(n)]
    y = [random.uniform(-b, b) for _ in range(n)] # Why should I use random.uniform 
                                                    # and not linspace?
                                                    
    print(monte_carlo_integration_circle(circle, n, x, a, b))
    return monte_carlo_integration(fx, n, x, y, a, b)
     
    
if __name__ == "__main__":
    print(solution8())