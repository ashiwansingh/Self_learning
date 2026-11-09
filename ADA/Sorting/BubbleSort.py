# So we are learning bubble sorting and we will learn bubble sort today 


# right wallee see compare karo asc karnaa hain yaa desc krnaa hain uss hisab see swap kroo and lessgo 



def BubbleSort(arr):
    for i in range(len(arr)):

        for j in range(len(arr)-1):
            if arr[j]> arr[j+1]:
                arr[j] ,  arr[j+1] = arr[j+1] ,  arr[j]

    return arr


arr = [3, 5, 8, 2, 1]
print(BubbleSort(arr))




#Optimistaion :-

# Jab hamm upper alla code run krte hain tab hamme doo baar pura arr travel krnaa pdta hain but hamraa jo last term hain woo proper apni postion main ajataa hain 
# So small changes in the iteration we will do 

def BubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = [3, 5, 8, 2, 1]
print(BubbleSort(arr))