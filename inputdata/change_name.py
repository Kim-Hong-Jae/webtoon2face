import os

output_path = os.path.join(os.getcwd(), "output")
output_list = os.listdir(output_path)
lst = []

for num in output_list:
    num = int(num.split(".")[0])
    lst.append(num)

lst.sort()
lst_name = []

for name in lst:
    lst_name.append(str(name)+".png")

itr = 0
for filename in lst_name:
    print(os.path.join(output_path, filename))
    print(os.path.join(output_path, f"{itr}.png"))
    os.rename(os.path.join(output_path, filename), os.path.join(output_path, f"{itr}.png"))
    itr += 1
