list = ['faiz', 'rohan', 'rez', 'nish']

def crowd_test(list):
    if(len(list) > 3):
        print("This room is wayyyyy to crowded")
    else:
        print("It's comfy in here")

crowd_test(list)
list.pop()
list.pop()
crowd_test(list)
