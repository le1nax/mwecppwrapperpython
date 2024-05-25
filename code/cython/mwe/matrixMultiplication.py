import numpy as np

def multiply3DmatricesNumpy(arr1, arr2):
    # Iterate through third dimension and perform matrix multiplication
    returnArray = np.empty([arr1.shape[0], arr2.shape[1], arr1.shape[2]])
    # print(arr1.shape)
    # print(arr2.shape)
    # print(returnArray.shape)
    for rgbIter in range(arr1.shape[2]):
        returnArray[:,:,rgbIter] = np.matmul(arr1[:,:,rgbIter], arr2[:,:,rgbIter])
    return returnArray
    
def multiply3DmatricesPython(arr1, arr2):

    # print("arr1.shape[0]" + str(arr1.shape[0]))
    # print("arr1.shape[1]" + str(arr1.shape[1]))
    # print("arr1.shape[2]" + str(arr1.shape[2]))

    # Iterate through third dimension and perform matrix multiplication
    numOfRowsArr1 = arr1.shape[0]
    numOfColumnsArr1 = arr1.shape[1]
    numOfColumnsArr2 = arr2.shape[1]
    # print(numOfRowsArr1)
    # print(numOfColumnsArr1)
    # print(numOfColumnsArr2)
    returnArray = np.empty([arr1.shape[0], arr2.shape[1], arr1.shape[2]])
    for rgbIter in range(arr1.shape[2]):
        for rowArr1 in range(numOfRowsArr1):
            for columnArr2 in range(numOfColumnsArr2):
                currentEntry = 0
                for columnArr1 in range(numOfColumnsArr1):
                    # print("arr1[rowArr1, columnArr1, rgbIter]=" + str(arr1[rowArr1, columnArr1, rgbIter]))
                    # print("arr2[columnArr1, columnArr2, rgbIter]=" + str(arr2[columnArr1, columnArr2, rgbIter]))
                    currentEntry += arr1[rowArr1, columnArr1, rgbIter] * arr2[columnArr1, columnArr2, rgbIter]
                # print(str(currentEntry) + str(type(currentEntry)))
                returnArray[rowArr1, columnArr2, rgbIter] = currentEntry
        
    return returnArray