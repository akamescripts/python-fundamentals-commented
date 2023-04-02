def binary_search(arr, target):
    # define the left and right indices of the search range
    left = 0
    right = len(arr) - 1

    while left <= right:
        # calculate the midpoint of the search range
        mid = (left + right) // 2

        # check if the target is in the middle of the search range
        if arr[mid] == target:
            return mid
        # if the target is smaller than the middle element, search in the left half
        elif arr[mid] > target:
            right = mid - 1
        # if the target is larger than the middle element, search in the right half
        else:
            left = mid + 1

    # if the target is not found, return -1
    return -1
