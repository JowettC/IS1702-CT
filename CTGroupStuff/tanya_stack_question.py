def enqueue(item):
    for i in range(len(stack1)):
        stack2.push(stack1.pop())
    stack2.push(item)
    for i in range(len(stack2)):
        stack1.push(stack2.pop())
    