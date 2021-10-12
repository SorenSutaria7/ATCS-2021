list = ['policeman', 'fireman', 'postman', 'doctor']

index = list.index('fireman')
print(list[index])

list.append('nurse')
list.insert(0, 'chef')

for career in list:
    print(career)