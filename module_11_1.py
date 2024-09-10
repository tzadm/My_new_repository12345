import requests
import pprint
import numpy as np
import random
import matplotlib.pyplot as plt


url = "https://urban-university.ru"
res = requests.get(url)
print(res.status_code)
url_ = "https://api.github.com/"
res_ = requests.get(url_)
print(res_.headers)
print(res_.status_code)
print(res_.text)
res_json = res_.json()
pprint.pprint(res_json)
pprint.pprint(res_.content)
#
# ##################################################################################################

array_0 = np.full((5, 5), 9)
print(array_0)
print(array_0.shape, array_0.dtype)
print()
other_array = np.empty((10, 10))
other_array.fill(2)
print(other_array)
print(other_array.shape, other_array.dtype)
other_array_2 = other_array.astype(int)
print(other_array_2)
print(other_array_2.shape, other_array_2.dtype, other_array_2.size)

array_1 = np.array([i for i in range(40)])
array_2 = array_1.reshape((5, 8))
array_3 = array_1.reshape((5, 4, 2))
print(array_2)
print(array_3)

##################################################################################################################
random_array_np = np.random.randint(1, 100, size=(10, 10))
x_list = list(range(0, 10))
y1_list = random_array_np[2]
y2_list = random_array_np[1]
y3_list = random_array_np[3]
y4_list = random_array_np[4]
graf_1 = plt.subplot(1, 4, 1)
plt.plot(x_list, y1_list)
plt.grid()
graf_2 = plt.subplot(1, 4, 2)
plt.plot(x_list, y2_list)
graf_3 = plt.subplot(1, 4, 3)
plt.plot(x_list, y3_list)
graf_4 = plt.subplot(1, 4, 4)
plt.plot(x_list, y4_list)
graf_1.grid()
graf_2.grid()
graf_3.grid()
graf_4.grid()
plt.show()
