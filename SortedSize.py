Numbers=[77,46,11,89,48,14,67,73,22,26]
SortedSize=0
size=len=10
while SortedSize<size-1:
    index=0
    while index<(size-1-SortedSize):
        if Numbers[index]>Numbers[index+1]:
            Temp=Numbers[index]
            Numbers[index]=Numbers[index+1]
            Numbers[index+1]=Temp
        index=index+1
    SortedSize=SortedSize+1
print(Numbers)