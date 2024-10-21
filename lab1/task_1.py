numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum=0
non_element=0
for i in range(len(numbers)):
    if numbers[i] == None:
        non_element=i
    else:
        sum += numbers[i]
numbers[non_element] = sum/len(numbers)
print("Измененный список:", numbers)
