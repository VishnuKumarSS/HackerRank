queries = int(input())

queue = []

while queries != 0:
    queries = queries -1
    query = str(input())
    action = int(query.split(" ")[0])
    
    if action == 1:
        number = int(query.split(" ")[1])
        queue.append(number)
    elif action == 2:
        queue.pop(0)
    elif action == 3:
        print(queue[0])
    else:
        continue
    
      
