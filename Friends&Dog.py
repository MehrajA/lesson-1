count=0
distance=10000
FirstFriendSpeed=1
SecondFriendSpeed=2
DogSpeed=5
Friend=2
while distance>10:
    if Friend==1:
        time=distance/(DogSpeed-FirstFriendSpeed)
        Friend=2
    else:
        time=distance/(SecondFriendSpeed+DogSpeed)
        Friend=1
    distance=distance-(SecondFriendSpeed-FirstFriendSpeed)*time
    count=count+1
print(count)