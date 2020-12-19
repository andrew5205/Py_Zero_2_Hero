
# time elapsed
# timeit




def function1(n):
    return [str(num) for num in range(n)]

# print(function1(10))

def function2(n):
    return list(map(str, range(n)))

# print(function2(10))




import time
# # Method ONE
# # Current time before 
# start_time = time.time()
# # Run code 
# result = function1(1000000)
# # after running code
# end_time = time.time()
# # elapsed time 
# elapsed_time = end_time - start_time
# print(elapsed_time)




import timeit

# stmt => function name 
# setup => def function()


stmt = """
function1(100)
"""

setup = """
def function1(n):
    return [str(num) for num in range(n)]
"""

print(timeit.timeit(stmt, setup, number=10000))



