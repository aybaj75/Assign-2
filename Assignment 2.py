#Assignment 2 
#Ayaan Bajwa
#100864399

#Playsound Import to allow sound to implement
from playsound import playsound

def Sort(arr):
    if len(arr) > 1:  # Base case: if array length is 1 or less, it's already sorted
        
        mid = len(arr) // 2
        lH = arr[:mid]
        RH = arr[mid:]
        
        Sort(lH)  # Recursiveley sort left half of the array and product id
        Sort(RH)  # Recursively sort the right half of the array or product id
        
        # Merge sort begins 
        
        i = j = k = 0
        
        #While loops for the merge sorts 
        
        while i < len(lH) and j < len(RH):
            if lH[i] < RH[j]:
                arr[k] = lH[i]
                i += 1
                
            else:
                arr[k] = RH[j]
                j += 1
            k += 1
            playsound("beat.mp3.mp3")
            #Playsound implemntation in while loop
            
        # Check if any elements were left
        while i < len(lH):
            arr[k] = lH[i]
            i += 1
            k += 1
            playsound("beat.mp3.mp3")
            #Playsound implemntation in while loop
            
        while j < len(RH):
            arr[k] = RH[j]
            j += 1
            k += 1
            playsound("beat.mp3.mp3")
            #Playsound implemntation in while loop
            
#Display function           
def printlist(arr):
    print(' '.join(str(x) for x in arr))

# Program Initiater 

if __name__ == '__main__':
    arr = [0, 1, 3, 5, 7, 9, 2, 4, 6, 8]
    Sort(arr)
    print(" The Sorted array for the following is: ")
    printlist(arr)
