import os

list=os.listdir("data")
print(os.getcwd())
os.chdir("/python")
print(os.getcwd())
# for i in list:
#     print(i)
#     print(os.listdir(f"data/{i}"))