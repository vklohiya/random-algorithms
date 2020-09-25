import statistics
import math


def one_dimentional(data, m1,m2):
    k1, k2 = [], []
    print(f"M1={m1}")
    print(f"M2={m2}")
    for d in data:
        if abs(d - m1) < abs(d -m2):
            k1.append(d)
        else:
            k2.append(d)
    print(f"K1={k1}")
    print(f"K2={k2}")
    return statistics.mean(k1), statistics.mean(k2)


def cal_distance(x, y, type="euclidean"):
    if type == "euclidean":
        distance = round(math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)])),2)
        print(f"Euclidean distance from {x} to {y}: ",distance)
        return distance
    elif type == "manhattan":
        distance = sum([abs(a-b) for a, b in zip(x,y)])
        print(f"Manhattan distance from {x} to {y}: ", distance)
        return distance
    else:
        print("No supported Method")


def cal_centroid(cluster):
    print(f"New Centroid for cluster: {cluster}")
    x,y = [], []
    for (a, b) in cluster:
        x.append(a)
        y.append(b)
    cx, cy = statistics.mean(x), statistics.mean(y)
    return (cx, cy)


def two_dimenstional(X,Y, c1,c2):
    k1, k2 = [], []
    for a,b in zip(X,Y):
        d1 = cal_distance((a,b), c1)
        d2 = cal_distance((a,b), c2)
        if d1 < d2 :
            k1.append((a,b))
            print(f"K1={k1}")
            c1 = cal_centroid(k1)
            print(f"C1={c1}")
        else:
            k2.append((a,b))
            print(f"K2={k2}")
            c2 = cal_centroid(k2)
            print(f"C2={c2}")
    print(f"Final Assignment:")
    print(f"K1={k1}")
    print(f"K2={k2}")

def two_mediod(X,Y, c1,c2):
    k1, k2 = [], []
    for a,b in zip(X,Y):
        d1 = cal_distance((a,b), c1, type="manhattan")
        d2 = cal_distance((a,b), c2, type="manhattan")
        if d1 < d2 :
            k1.append((a,b))
            print(f"K1={k1}")
        else:
            k2.append((a,b))
            print(f"K2={k2}")
    print(f"Final Assignment:")
    print(f"K1={k1}")
    print(f"K2={k2}")


def call_one():
    data = [6,7,8,9,10,11,23,24,21,32]
    k = 2
    m1 = 5
    m2 = 16
    for i in range(0, 5):
        print(f"For Step-{i+1}")
        m1, m2 = one_dimentional(data, m1, m2)


def call_two():
    X = [185, 170, 168, 179, 182, 188, 180, 180, 183, 180, 180, 177]
    Y = [72, 56, 60, 68, 72, 77, 71, 70, 84, 88, 67, 76]
    if len(X) != len(Y):
        print("Invalid data")
        exit(1)
    c1 = (185, 72)
    c2 = (170, 56)
    two_dimenstional(X,Y, c1,c2)

def call_mediod():
    X = [2,3,3,4,6,6,7,7,8,7]
    Y = [6,4,8,7,2,4,3,4,5,6]
    if len(X) != len(Y):
        print("Invalid data")
        exit(1)
    c1 = (3, 4)
    c2 = (7, 4)
    two_mediod(X, Y, c1, c2)

def cal_distance_matrix(type="euclidean"):
    X = [0.4, 0.22, 0.35, 0.26, 0.08, 0.45]
    Y = [0.53, 0.38, 0.32, 0.19, 0.41, 0.30]
    if len(X) != len(Y):
        print("Invalid data")
        exit(1)
    matrix = []
    for (x, y) in zip(X,Y):
        row = []
        for (a,b) in zip(X, Y):
            row.append(cal_distance((a, b), (x,y), type=type))
        matrix.append(row)
    print("Distance matrix:")
    for row in matrix:
        print(row)

call_one()

