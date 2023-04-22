import ast
import matplotlib.pyplot as plt
import numpy as np

file = open("train_loss.txt","r")
lines = file.readlines()
num_list = []
for line in lines:
    num = line.split(":")[1]
    num = num.split(" ")[1]
    num = ast.literal_eval(num)
    num_list.append(num)

num_array = np.array(num_list)
x_list = []
for x in range(1,62):
    x_list.append(x)
x_array = np.array(x_list)

plt.subplot(2,1,1)
plt.plot(x_array,num_array)
plt.xlabel("Epoch")
plt.ylabel("Training loss(CTC)")

file = open("valid_loss.txt","r")
lines = file.readlines()
num_list = []
for line in lines:
    num = line.split(":")[1]
    num = num.split(" ")[1]
    num = ast.literal_eval(num)
    num_list.append(num)

num_array = np.array(num_list)
x_list = []
for x in range(1,62):
    x_list.append(x)
x_array = np.array(x_list)

plt.subplot(2,1,2)
plt.plot(x_array,num_array)

plt.xlabel("Epoch")
plt.ylabel("Validation loss(CTC)")
plt.show()