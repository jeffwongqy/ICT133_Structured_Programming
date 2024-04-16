bid_list_copy = [['S9342594D', 96000], ['S1286294F', 120000], ['T0234567F', 70000000]]

for i in range(len(bid_list_copy) - 1):
    for j in range(len(bid_list_copy) - i - 1):
        if bid_list_copy[j][1] < bid_list_copy[j+1][1]:
            bid_list_copy[j], bid_list_copy[j+1] = bid_list_copy[j+1], bid_list_copy[j]
print(bid_list_copy)

print(len(bid_list_copy[:2]))