def getDiscs():
    while True:
        try:
            n = int(input("How many discs in the tower? "))
            return n
        except ValueError:
            print("There must be an integer number of discs")

def choice(n):
    global a, b, c
    a = [i+1 for i in range(n)][::-1]
    b = []
    c = []

    solveType = input("Would you like to solve this using recursion [Y/N]? ")

    if solveType.lower() == "y":
        recursionSolve(n, a, c, b)

def recursionSolve(n, start, end, spare):
    # ----------------------------------------------------------------------
    # Recursion solves this by moving n-1 discs to the spare tower, then
    # moving the biggest disc to the end tower. Now it must move (n-2) discs
    # from the previously spare tower to the new spare tower, (the starting 
    # tower). Then the (n-1)th disc will be moved to the end tower. This 
    # continues until n == 0, which means the problem is solved
    # ----------------------------------------------------------------------

    if n > 0:
        # Moves (n-1) discs from start to the spare tower
        # other and end are switched
        recursionSolve(n - 1, start, spare, end)

        # Move the biggest disc from start to end
        end.append(start.pop())

        # Display our progress
        print(a, b, c, '------------', sep='\n')

        # Move the n - 1 disks that we left on the spare tower onto end tower
        recursionSolve(n - 1, spare, end, start)

"""
def iterativeSolve(n):
    # --------------------------------------------------------------------
    # This type of solve uses a formulaic approach to moving the discs
    # properly by following certain constraints that result in no 
    # backtracking. This can also be the optimal solution.
    # --------------------------------------------------------------------
    x = [3, 2, 1]
    y = []
    z = []



    if n % 2 == 0: #even
        z.append(x.pop())
    else:
        y.append(x.pop())
    while len(z) != n and not y and not x:
        print(x, y, z, '------------', sep='\n')
        
        s, e = move(x, y, z)
        print(s, e)

        if s == 0:
            if e == 1 and y:
                y.append(x.pop())
            elif e == 2 and z:
                z.append(x.pop())
        elif s == 1:
            if e == 2 and z:
                z.append(y.pop())
            elif e == 0 and x:
                x.append(y.pop())
        else:
            if e == 0 and x:
                x.append(z.pop())
            elif e == 1 and y:
                y.append(z.pop()) 

def move(a, b, c):
    ls = [a, b, c]
    ends = []
    for i in ls:
        if not i:
            ends.append(0)
        else:
            ends.append(i[-1])

    biggest = max(ends)

    for i in range(3):
        if ends[i] != biggest:
            if i == 0:
                moves = [1, 2]
            elif i == 1:
                moves = [0, 2]
            else:
                moves = [0, 1]

            possibles = []
            for j in moves:
                if ends[j] > ends[i]:
                    if ends[i] % 2 == 0:
                        if ends[j] % 2 != 0 or ends[j] == 0:
                            possibles.append(j)
                    elif ends[i] % 2 != 0:
                        if ends[j] % 2 == 0 or ends[j] == 0:
                            possibles.append(j)
                
            if len(possibles) == 1:
                return i, j
            else:
                for value in possibles:
                    if ends[value] == 0:
                        if value == 0:
                            return i, value + 1
                        else:
                            return i, value - 1

"""

def main():
    n = getDiscs()
    choice(n)

main()
