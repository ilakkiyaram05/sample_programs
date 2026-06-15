def find_index(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1
if __name__ == "__main__":
    array1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    target1 = 10
    print("Index of 10:", find_index(array1, target1)) 
