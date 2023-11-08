numbers=[2,5,13,7,6,4]
size=6
index=0
max_idx=0
max=numbers[max_idx]
while index<size:
   if numbers[index]>max:
     max_idx=index
     max=numbers[index]
   index=index+1
print(numbers)
numbers[max_idx]=numbers[0]
numbers[0]=max
print(numbers)