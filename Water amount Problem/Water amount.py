

def waterVolume(T):
    """
    Function to predict the amount of water stored in the array
    Input: Array
    Output: Total amount of the water sotred
    """

    water = []          # The amount of water stored
    current = 0         # Maximum value
    i = current + 1     # To find the max value
    max = T[current]    # Initilise the maximum value

    while(i < len(T)-1):
        max = T[current]
        while T[i] < max and i < len(T)-1:
            i += 1

        # Max should be one of two : Greater than current value or the last value of the list
        max = T[i]

        # Max is greater than the current value
        if max >= T[current]:
            for j in range(current+1, i):
                water.append(T[current] - T[j])

        # Max is less than current value (last value in the list)
        else:
            # Find the maximum value between the current and last value
            for j in range(current+1, i):
                if T[j] > max:
                    max = T[j]
            i = j

            # Find the amount of water between the current and last value
            for j in range(current+1, i+1):
                water.append(max - T[j])

        # Update the current value to the new max value
        current = i
        i += 1
        
    return sum(water)



# Simple Demo
T = [1, 0, 2, 0, 0, 0, 1, 3, 4]
print(waterVolume(T))