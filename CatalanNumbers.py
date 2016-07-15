__author__ = 'Danylo'


# http://www.geeksforgeeks.org/program-nth-catalan-number/
# Program for nth Catalan Number
# Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

# 1) Count the number of expressions containing n pairs of parentheses which are correctly matched.
# For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
# 2) Count the number of possible Binary Search Trees with n keys (See this)
# 3) Count the number of full binary trees
# (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.


# The static cache of previously computed values.
cache = [1, 1]


def catalan_number_dynamic(n):
    if len(cache) > n:
        return cache[n]

    current = 0
    for i in range(0, n):
        current += catalan_number_dynamic(i) * catalan_number_dynamic(n - i - 1)

    cache.append(current)
    return current


# Returns value of Binomial Coefficient C(n, k)
def binomial_coefficient(n, k):
    res = 1

    # Since C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k

    # Calculate value of [n*(n-1)*---*(n-k+1)] / [k*(k-1)*---*1]
    for i in range(0, k):
        res *= (n - i)
        res /= (i + 1)

    return res


def catalan_number_binomial_coefficients(n):
    return binomial_coefficient(2 * n, n) / (n + 1)


for i in range(0, 10):
    print(catalan_number_dynamic(i))
    print(catalan_number_binomial_coefficients(i))
