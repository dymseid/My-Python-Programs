def TOH(numbers,start,aux,end):
    if numbers == 1:
        print("Move disc 1 from rod {} to rod {}".format(start,end))
        return
    TOH (numbers-1,start,end,aux)
    print("Move disc {} from rod {} to rod {}".format(numbers,start,end))
    TOH (numbers-1,aux,start,end)

disc = 3
TOH(disc,"A","B","C")


# def TOH (numbers,start,aux,end):
#     if numbers == 1:
#         print("Move disc 1 from rod {} to rod {}".format(start,end))
#         return
#     TOH(numbers-1,start,end,aux)
#     print("Move disc {} from rod {} to rod {}".format(numbers,start,end))
#     TOH(numbers-1,aux,start,end)

# disc = 3
# TOH(disc,"A","B","C")




# def find_repeating_numbers (arr):
#     n = len(arr)
#     repeating_numbers = []

#     for i in range (n):
#         index = arr[i] % n
#         arr[index] += n

#     for i in range (n):
#         if arr[i] // n > 1:
#             repeating_numbers.append(i)

#     return repeating_numbers



# def find_missing_numbers (arr):
#     n = len(arr)+1
#     expected_sum = n*(n+1) // 2
#     actual_sum = sum(arr)
#     missing_number = expected_sum - actual_sum
#     return missing_number

# def find_missing_numbers (arr):
#     n = len(arr) + 1
#     expected_sum = n*(n+1) // 2
#     actual_sum = sum(arr)
#     missing_numbers = expected_sum - actual_sum
#     return missing_numbers