templist_1 = [25, 50, 100, 150, 200, 250, 300, 33]
print(sorted(templist_1, key=int))
templist_2 = [4, 34, 350, 90]
print(sorted(templist_2, key=int))
merge_list = templist_1 + templist_2
print(sorted(merge_list, key=int))

