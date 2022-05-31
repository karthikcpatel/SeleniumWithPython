kp_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List having duplicate elements ", kp_list)
temp_list = []

for i in kp_list:
    if i not in temp_list:
        temp_list.append(i)

kp_list = temp_list

print("List after removing duplicate elements ", kp_list)