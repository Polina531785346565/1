numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим


f_index=numbers.index(None)
k=len(numbers)
m=sum(numbers[:f_index])+sum(numbers[f_index+1:])
numbers[f_index]=m/k

print("Измененный список:", numbers)