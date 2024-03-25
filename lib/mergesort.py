def mergesort(array, cmp=lambda x, y: x <= y):
    if len(array) <= 1:
        return array

    left = array[: len(array) // 2]
    right = array[len(array) // 2 :]

    left = mergesort(left, cmp)
    right = mergesort(right, cmp)

    result = []
    leftI = 0
    rightI = 0

    while leftI < len(left) and rightI < len(right):
        if cmp(left[leftI], right[rightI]):
            result.append(left[leftI])
            leftI += 1
        else:
            result.append(right[rightI])
            rightI += 1

    while leftI < len(left):
        result.append(left[leftI])
        leftI += 1

    while rightI < len(right):
        result.append(right[rightI])
        rightI += 1

    return result
