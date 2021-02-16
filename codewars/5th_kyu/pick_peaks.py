'''
In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

# https://medium.com/@dineshjoshi/solution-to-pick-peak-problem-on-codewars-d3f04a08fa19
'''

# if the nubmers to the left and right of a given number are less than the number you're on, you're at a peak

def pick_peaks(arr):
    # setting the previous and current values of the list
    previous, current = 0, 0
    pos = []
    peaks = []

    # starting at index 1 and going to the length of the array
    # the variable next is the same as using i, it will be an integer
    for next in range(1, len(arr)):
        if arr[next] > arr[current]:
            previous = current
            current = next
        else:
          if arr[next] < arr[current]:
              if arr[previous] < arr[current]:
                  pos.append(current)
                  peaks.append(arr[current])
              previous = current
              current = next

    print ({"pos": pos, "peaks": peaks})
    return {"pos": pos, "peaks": peaks}
    # my_dict = {
    #     'pos': [],
    #     'peaks': []
    # }
    # counter = 1
    # print(arr)
    # left_number = arr[0]
    # start = arr[1]
    # right_number = arr[2]
    # print(left_number, start, right_number)
    # for i in range(len(arr)-1):
    #     print('left, start, right', arr[i-1], arr[i], arr[i+1])
    #     if arr[i] > arr[i - 1] and arr[i] > arr [i + 1]:
    #         my_dict['pos'].append(i + 1)
    #         my_dict['peaks'].append(arr[i+1])
    #     elif arr[i] == arr[i-1] and arr[i] == arr[i+1]:
            
    #         while arr[i] == arr[i+counter]:
    #             counter += 1
    #             print(arr[i+counter])
    #             break
    # print(my_dict)






    # my_dict = {
    #     'pos': [],
    #     'peaks': []
    # }
    # plateau = []
    # plateau_index = []
    # print(arr)
    # counter = 0
    # for i in range(len(arr) - 2):
    #     left_number = arr[i]
    #     start = arr[i + 1]
    #     right_number = arr[i + 2]
    #     print(left_number, start, right_number)
    #     while left_number == start and right_number == start:
    #         print('i', i)
    #         counter += 1
    #         left_number = start
    #         start = right_number
    #         right_number = arr[i + 2 + counter]
    #         print('LRS: ', left_number, start, right_number)
    #         if left_number not in plateau:
    #             plateau.append(arr[i])
    #             plateau_index.append(i)
    #             if right_number not in plateau:
    #                 my_dict['pos'].append(plateau[0])
    #                 my_dict['peaks'].append([plateau_index[0]])
    #     if start > left_number and start > right_number:
    #         my_dict['pos'].append(i + 1)
    #         my_dict['peaks'].append(arr[i+1])
    
    # print (my_dict)
    # return my_dict
    

    

if __name__ == "__main__":
    # pick_peaks([1,2,3,6,4,1,2,3,2,1])
    pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1])
    # {'pos': [3, 7, 10], 'peaks': [6, 3, 2]}
    pick_peaks([2, 1, 3, 1, 2, 2, 2, 2])
    # {'pos': [2], 'peaks': [3]}
