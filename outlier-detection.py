import statistics
from numpy import percentile
import copy


def find_outlier_univariate(data):
    std = statistics.pstdev(data)
    mean = statistics.mean(data)
    print(f"Standard Deviation: {std}")
    print(f"Averagre: {mean}")
    for d in data:
        if d > (mean +std) or d < (mean -std):
            print(f"{d} is an outlier")


def box_plot(data):
    quartiles = percentile(data, [25, 50, 75])
    itr = quartiles[2] - quartiles[0]
    print(f"Q1 = {quartiles[0]}")
    print(f"Q3 = {quartiles[2]}")
    for d in data:
        if d < quartiles[0] - (1.5 * itr) or d > quartiles[2] + (1.5 * itr):
            print(f"{d} is an outlier")


def indices(mylist, value):
    return [i for i,x in enumerate(mylist) if x==value]


def density_based(dist_mat, N):
    dist2 = []
    for i, row in enumerate(dist_mat, start=0):
        new_row = sorted(copy.deepcopy(row))
        print(f"Dist2[{i}] = {new_row[N]}")
        dist2.append(new_row[N])
    N2 = []
    for i, row in enumerate(dist_mat, start=0):
        new_row = sorted(copy.deepcopy(row))
        neighbour = []
        j =1
        while(j<N+1):
            ne = indices(row, new_row[j])
            j +=len(ne)
            for element in ne:
                neighbour.append(element)
        N2.append(neighbour)
        print(f"N2({i}) = {neighbour}")


    def reachability(origin, destination):
        distance = max(dist2[destination], dist_mat[origin][destination])
        print(f"reachdist{N}({origin}->{destination}) = max({dist2[destination]}, {dist_mat[origin][destination]}) = {distance}")
        return distance


    def local_density(index):
        all_reachable = 0
        all_reachable_string = "0"
        for neighbour in N2[index]:
            all_reachable_string += f" + reachdist{N}({index}->{neighbour})"
        print(f"Density({index}) = ||N{N}({index})||/{all_reachable_string}")
        for neighbour in N2[index]:
            all_reachable += reachability(index, neighbour)
        density = N / all_reachable
        print(f"Density({index}) = {density}")
        return density

    densities = []
    for i in range(0, len(dist_mat)):
        densities.append(local_density(i))

    print(f"Outlier is {max(densities)}")

dist_mat = [
    [0,1,2,3],
    [1,0,1,4],
    [2,1,0,3],
    [3,4,3,0]
]

data = [24.0, 28.9, 28.9, 29.0, 29.1, 29.1, 29.2, 29.2, 29.3, 29.4]
find_outlier_univariate(data)
box_plot(data)

density_based(dist_mat=dist_mat, N=2)

