# Python3 program to illustrate
# Banker's Algorithm

processes = [0, 1, 2, 3, 4]

# Available instances of resources
avail = [3,3,2]

# Maximum R that can be allocated
# to processes
maxm = [[7, 5, 3], [3, 2, 2],
        [9, 0, 2], [2, 2,2],
        [4,3,3]]

# Resources allocated to processes
allot = [[0, 1, 0], [2, 0, 0],
         [3, 0, 2], [2, 1, 1],
         [0, 0, 2]]
req = [1,0,2]
process_no = 1

P = len(processes)
R = len(avail)


# Function to find the need of each process
def calculateNeed(need, maxm, allot):
    # Calculating Need of each P
    print("Need Matrix:")
    for i in range(P):
        for j in range(R):
            # Need of instance = maxm instance -
            # allocated instance
            need[i][j] = maxm[i][j] - allot[i][j]
        print(need[i])


# safe state or not
def isSafe(processes, avail, maxm, allot):
    need = []
    for i in range(P):
        l = []
        for j in range(R):
            l.append(0)
        need.append(l)

    # Function to calculate need matrix
    calculateNeed(need, maxm, allot)

    # Mark all processes as infinish
    finish = [0] * P
    step_count = 1
    print(f"Step-{step_count}: Initializing finish table: {finish}")

    # To store safe sequence
    safeSeq = [0] * P

    # Make a copy of available resources
    work = [0] * R
    for i in range(R):
        work[i] = avail[i]

    # While all processes are not finished
    # or system is not in safe state.
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
                    if (need[p][j] > work[j]):
                        step_count +=1
                        print(f"Step-{step_count}: Process-{p} need {need[p]} is greater than work {work}, Going to next process.")
                        break

                # If all needs of p were satisfied.
                if (j == R - 1):
                    step_count += 1
                    print(f"Step-{step_count}: Process-{p} need {need[p]} is less than equal to work {work}, Hence completeing the process-{p}.")
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
            print(f"As no more process can be completed with available resources {work}, System is not in safe state.")
            deadlock = []
            for i in range(0, len(finish)):
                if finish[i] == 0:
                    deadlock.append(i)
            print(f"Following process are in deadlock state:{deadlock}")
            return False

    # If system is in safe state then
    # safe sequence will be as below
    print("System is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    return True


# Driver code
def totalAvailable(allot, avail):
    total = avail
    for resource in allot:
        for i in range(0, len(resource)):
            total[i] += resource[i]
    print(f"Total Available Resources: {total}")


def request(process, allot, maxm, req, avail):
    need = []
    for l1, l2 in zip(maxm[process],allot[process]):
        need.append(l1-l2)
    for l1, l2 in zip(req, need):
        if l1 > l2:
            print(f"Process P{process} has requsted {req} which is greater than it's need {need} hence exceeded maximum claim.")
            return False

    for l1,l2 in zip(req, avail):
        if l1 > l2:
            print(f"Process P{process} should wait as resources not available.")
            return False

    print(f"As {req} is less than {avail}, we can allocate the resource.")
    new_avail = []
    for l1, l2 in zip(avail, req):
        new_avail.append(l1 - l2)

    new_allot = []
    for l1, l2 in zip(allot[process], req):
        new_allot.append(l1 + l2)
    return [new_avail, new_allot]


# Check system is in safe state or not
isSafe(processes, avail, maxm, allot)
result = request(process_no, allot, maxm, req, avail)
if result:
    avail = result[0]
    allot[process_no] = result[1]
    isSafe(processes, avail, maxm, allot)


#totalAvailable(allot, avail)

