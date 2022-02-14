lst = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

print(lst[1:5])# -> ['World', 'Huston', 'we', 'are']
print(lst[0:2])# -> ['Hello', 'World']
print(lst[4:6])# -> ['are', 'here']
print(lst[4:5])# -> ['are']
print(lst[0:6:2])# -> ['Hello', 'Huston', 'are']
print(lst[::-1])# -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
print(lst[1:5])# -> ['World', 'Huston', 'we', 'are']
print(lst[1]+" "+lst[2]+" "+lst[3])# -> 'World Huston we