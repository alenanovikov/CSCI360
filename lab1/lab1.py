# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque
from lab1_utils import TextbookStack

def breadth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    # total number of books
    n = stack.num_books
    # add an array of predecessors
    p = {}
    # initialize deque
    dq = deque()
    # initialize visited
    visited = deque()
    # append the first element from the stack
    cnt = 1
    dq.append([cnt, stack])
    cnt += 1
    visited.append(stack)
    # initalize the predecessor of the initial stack as null
    p[1] = [None, None]
    # other helper variables
    solution = None
    flag = 0

    while(len(dq)):
        # if solution was found, terminate the main loop
        if(flag == 1):
            break
        # dequeue the node to explore
        node = dq.popleft()

        # Add all possible outgoing states from this node to the queue
        for book in range(1, n+1):
            child = node[1].copy()
            child.flip_stack(book)

            # if one of the children matches the correct sequence, terminate
            if(child.check_ordered()):
                solution = [cnt, book]
                p[cnt] = [node[0], book]
                flag = 1
                break
            
            # if the child hasn't been visited
            if(child not in visited):
                # add to the queue
                dq.append([cnt, child])
                # mark as visited
                visited.append(child)
                # update predecessor
                p[cnt] = [node[0], book]
                cnt += 1

    curr = solution[0]
    #seq = p[curr][1]
    seq = solution[1]
    while(p[curr][0] != None):
        flip_sequence.append(seq)
        curr = p[curr][0]
        seq = p[curr][1]
    flip_sequence.reverse()
    return flip_sequence
    # ---------------------------- #


def depth_first_search(stack):
    flip_sequence = []

    # # --- v ADD YOUR CODE HERE v --- #
    # total number of books
    n = stack.num_books
    # add an array of predecessors
    p = {}
    # initialize deque
    dq = deque()
    # initialize visited
    visited = deque()
    # append the first element from the stack and initialze the counter
    cnt = 1
    dq.append([cnt, stack])
    cnt += 1
    # iniitialize predecessors
    p[1] = [None, None]
    # helper variable
    solution = None

    while(len(dq)):
        # dequeue the most recently added node to explore
        node = dq.pop()

        # if solution found, terminate
        if(node[1].check_ordered()):
            solution = node
            break

        # if the node hasn't been explored
        if(node[1] not in visited):
            # add all possible outgoing states from this node to the queue
            for book in range(1, n+1):
                child = node[1].copy()
                child.flip_stack(book)
                # append child to the frontier
                dq.append([cnt, child])
                # update predecessor
                p[cnt] = [node[0], book]
                cnt += 1
            # mark node as visited
            visited.append(node[1])

    curr = solution[0]
    seq = p[curr][1]
    # restore the sequence of flips
    while(p[curr][0] != None):
        flip_sequence.append(seq)
        curr = p[curr][0]
        seq = p[curr][1]
    flip_sequence.reverse()
    return flip_sequence
    # ---------------------------- #
