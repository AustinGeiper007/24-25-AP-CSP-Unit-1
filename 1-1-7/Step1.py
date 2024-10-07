new_list = ["dog", "cat", "mouse", "bird", "monkey"]

print("Before Append")
for id in range(5):
    print(new_list[id])

print("After Append")
new_list.append("lion")
for id2 in range(5):
    print(new_list[id2])