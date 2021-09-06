
# Python3 program for the 
# above approach
 
# Function to find length of 
# the longest substring with 
# each element occurring even 
# number of times

def lenOfLongestReqSubstr(s, N):
 

    # Initialize unordered_map

    ind = {}
 

    mask = 0

    ind[0] = -1
 

    # Stores the length of the

    # longest required substring

    ans = 0
 

    # Traverse the string

    for i in range(N):
 

        # Stores the value of the

        # digit present at current

        # index

        val = ord(s[i]) - ord('0')
 

        # Bitwise XOR of the mask

        # with 1 left-shifted by val

        mask ^= (1 << val)
 

        # Check if the value of mask 

        # is already present in ind 

        # or not

        if (mask in ind):

           

            # Update the final answer

            ans = max(ans, 

                      i - ind[mask])
 

        # Otherwise

        else:

            ind[mask] = i
 

    # Return the answer

    return ans