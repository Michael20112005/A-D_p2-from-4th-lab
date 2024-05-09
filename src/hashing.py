def find_3_numbers_sum(array, p):
    array.sort()

    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == p:
                return True
            elif current_sum < p:
                left += 1
            else:
                right -= 1

    return False
