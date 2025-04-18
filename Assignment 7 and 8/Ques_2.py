class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"{data} enqueued to queue")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def display(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Queue:", " -> ".join(map(str, self.queue)))

q = Queue()
while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter value to enqueue: "))
        q.enqueue(data)
    elif choice == 2:
        dequeued = q.dequeue()
        if dequeued is not None:
            print(f"Dequeued: {dequeued}")
    elif choice == 3:
        q.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")
