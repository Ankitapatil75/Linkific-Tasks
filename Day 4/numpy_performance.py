import time
import numpy as np

size = 1000000

# Python List
python_list = list(range(size))

start = time.time()

result = [x * 2 for x in python_list]

end = time.time()

python_time = end - start


# NumPy Array
numpy_array = np.arange(size)

start = time.time()

result = numpy_array * 2

end = time.time()

numpy_time = end - start


print("Python List Time :", python_time)

print("NumPy Time :", numpy_time)