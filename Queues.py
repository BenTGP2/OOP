Queue = []


def enqueue(task):
    Queue.append(task)


def dequeue():
    Queue.remove(Queue[0])


while True:
    print("1. Create task")
    print("2. Remove task")
    print("3. List queue")

    Input = input("Enter selection: ")

    if Input == "1":
        task = input("Enter the name of the task you would like to add: ")
        enqueue(task)
    elif Input == "2":
        dequeue()
    elif Input == "3":
        print(Queue)
