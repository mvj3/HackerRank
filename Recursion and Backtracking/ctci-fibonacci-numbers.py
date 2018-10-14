"""
Recursion: Fibonacci Numbers
Your Recursion: Fibonacci Numbers submission got 15.00 points.  
Try the next challenge
ProblemSubmissionsLeaderboardDiscussionsEditorial
Check out the resources on the page's right side to learn more about recursion. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

The Fibonacci Sequence

The Fibonacci sequence appears in nature all around us, in the arrangement of seeds in a sunflower and the spiral of a nautilus for example.

The Fibonacci sequence begins with  and  as its first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements.

Programmatically:

Given , return the  number in the sequence.

As an example, . The Fibonacci sequence to  is . With zero-based indexing, .

Function Description

Complete the recursive function  in the editor below. It must return the  element in the Fibonacci sequence.

fibonacci has the following parameter(s):

n: the integer index of the sequence to return
Input Format

The input line contains a single integer, .

Constraints

Output Format

Locked stub code in the editor prints the integer value returned by the  function.

Sample Input

3  
Sample Output

2
Explanation

The Fibonacci sequence begins as follows:

 
 
 
 
 
 
 
...

We want to know the value of . In the sequence above,  evaluates to .


"""


def fibonacci_recursion(n):
    """
    Pay attention to how to change a and b variables.
    """
    def f(a, b, n):
        if n <= 0:
            return a
        else:
            return f(b, a+b, n-1)
    return f(0, 1, n)

def fibonacci_cache(n):
    """
    Pay attention to cache every result.
    """
    def f(n, cache={}):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        else:
            result = f(n-1, cache) + f(n-2, cache)
            cache[n] = result
            return result
    return f(n, {})

def fibonacci_iterative(n):
    """
    how to change a and b variables.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
fibonacci = fibonacci_iterative
    
n = int(input())
print(fibonacci(n))
