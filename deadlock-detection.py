# Python3 program to illustrate
# Banker's Algorithm

processes = [0, 1, 2, 3, 4]

# Available instances of resources
avail = [0,0,0]

# Maximum R that can be allocated
# to processes
allot = [[0,1,0], [2,0,0],
        [3,0,3], [2,1,1],
        [0,0,2]]

# Resources allocated to processes
request = [[0, 0, 0], [2, 0, 1],
         [0, 0, 1], [1, 0, 0],
         [0, 0, 2]]

P = len(processes)
R = len(avail)


# Function to find the need of each process
def calculateNeed(need, request, allot):
    # Calculating Need of each P
    print("Need Matrix:")
    for i in range(P):
        for j in range(R):
            # Need of instance = request instance -
            # allocated instance
            need[i][j] = request[i][j] - allot[i][j]
        print(need[i])


# Dead lock or not
def isDeadLock(processes, avail, request, allot):

    # Mark all processes as infinish
    finish = [0] * P
    for i in range(P):
        if allot[i] != [0, 0, 0]:
            finish[i] = 0
        else:
            finish[i] = 1
    step_count = 1
    print(f"Step-{step_count}: Initializing finish table: {finish}")

    # To store safe sequence
    safeSeq = [0] * P

    # Make a copy of available resources
    work = [0] * R
    for i in range(R):
        work[i] = avail[i]

    # While all processes are not finished
    # or system is not in Dead lock.
    count = 0
    while (count < P):

        # Find a process which is not finish
        # and whose needs can be satisfied
        # with current work[] resources.
        found = False
        for p in range(P):

            # First check if a process is finished,
            # if no, go for next condition
            if (finish[p] == 0):

                # Check if for all resources
                # of current P need is less
                # than work
                for j in range(R):
                    flag = True
                    if (request[p][j] > work[j]):
                        step_count +=1
                        print(f"Step-{step_count}: Process-{p} request {request[p]} is greater than work {work}, Going to next process.")
                        flag = False
                        break

                # If all needs of p were satisfied.
                if flag:
                    step_count += 1
                    print(f"Step-{step_count}: Process-{p} request {request[p]} is less than equal to work {work}, Hence completeing the process-{p}.")
                    # Add the allocated resources of
                    # current P to the available/work
                    # resources i.e.free the resources
                    step_count += 1
                    print(f"Step-{step_count}: New work = {work} + {allot[p]}")
                    for k in range(R):
                        work[k] += allot[p][k]
                    print(f"New work = {work}")
                    # Add this process to safe sequence.
                    safeSeq[count] = p
                    count += 1

                    # Mark this p as finished
                    finish[p] = 1
                    step_count += 1
                    print(f"Step-{step_count}: New finish table : {finish}")
                    found = True

        # If we could not find a next process
        # in safe sequence.
        if (found == False):
            print(f"As no more process can be completed with available resources {work}, System is in Dead lock.")
            deadlock = []
            for i in range(0, len(finish)):
                if finish[i] == 0:
                    deadlock.append(i)
            print(f"Following process are in deadlock state:{deadlock}")
            return False

    # If system is in Dead lock then
    # safe sequence will be as below
    print("System is not in Dead lock state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    return True

# Check system is in Dead lock or not
isDeadLock(processes, avail, request, allot)


