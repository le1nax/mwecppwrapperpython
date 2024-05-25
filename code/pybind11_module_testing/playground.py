# import numpy as np

# # Example 2x2x3 array
# catImg = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=np.int32)
# catImg = np.ascontiguousarray(catImg)

# print("The catImg contiguous data when np.ascontiguousarray(catImg)")

# # Number of elements and size of each element in bytes
# nelements = catImg.size
# bsize = catImg.itemsize

# # Iterate over each element
# for i in range(nelements):
#     bnum = bytes(catImg.data[i*bsize : (i+1)*bsize])  # Convert to bytes
#     print(np.frombuffer(bnum, dtype=catImg.dtype)[0])  # Convert to number

# import numpy as np

# # Example 2x2x3 array
# catImg = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=np.int32)
# catImg = np.ascontiguousarray(catImg)

# print("The catImg contiguous data when np.ascontiguousarray(catImg)")

# # Total number of elements and size of each element in bytes
# nelements = catImg.size
# bsize = catImg.itemsize

# # Iterate over each element
# for i in range(nelements):
#     # Slice the memoryview object correctly and convert it to bytes
#     bnum = catImg.data[i*bsize : (i+1)*bsize].tobytes()
#     # Convert bytes to number
#     print(np.frombuffer(bnum, dtype=catImg.dtype)[0])

# import numpy as np

# # Example 2x2x3 array
# catImg = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=np.int32)
# catImg = np.ascontiguousarray(catImg)

# print("The catImg contiguous data when np.ascontiguousarray(catImg)")

# # Total number of elements and size of each element in bytes
# nelements = catImg.size
# bsize = catImg.itemsize

# # Print the memory layout for debugging
# print("Memory layout of the array (in bytes):")
# print(catImg.tobytes())

# # Iterate over each element
# for i in range(nelements):
#     # Correctly slice the memoryview object and convert it to bytes
#     bnum = catImg.data[i*bsize : (i+1)*bsize].tobytes()
#     # Check if the slice is empty for debugging
#     if not bnum:
#         print(f"Slice {i} is empty")
#     else:
#         # Convert bytes to number
#         print(np.frombuffer(bnum, dtype=catImg.dtype)[0])

import numpy as np

# Example 2x2x3 array
catImg = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=np.int32)
catImg = np.ascontiguousarray(catImg)
print("catImg_1=" + str(catImg[:,:,0]))
print("catImg_2=" + str(catImg[:,:,1]))
print("catImg_3=" + str(catImg[:,:,2]))

catImg = catImg.transpose()

# catImg = catImg.reshape(3,2,2, order="C")
# catImg = catImg.reshape(3,2,2, order="F")
# catImg = catImg.reshape(2,3,2, order="C")
# catImg = catImg.reshape(2,3,2, order="F")

# print("catImg_1=" + str(catImg[:,:,0]))
# print("catImg_2=" + str(catImg[:,:,1]))
# print("catImg_3=" + str(catImg[:,:,2]))

print("The catImg contiguous data when np.ascontiguousarray(catImg)")

# Total number of elements and size of each element in bytes
nelements = catImg.size
bsize = catImg.itemsize

# Flatten the array to ensure correct iteration over each element
flat_catImg_order_C = catImg.flatten(order='C')
print("flat_catImg_order_C" + str(flat_catImg_order_C))
flat_catImg_order_F = catImg.flatten(order='F')
print("flat_catImg_order_F" + str(flat_catImg_order_F))
flat_catImg_order_A = catImg.flatten(order='A')
print("flat_catImg_order_A" + str(flat_catImg_order_A))
flat_catImg_order_K = catImg.flatten(order='K')
print("flat_catImg_order_K" + str(flat_catImg_order_K))

# # Iterate over each element in the flattened array
# for i in range(nelements):
#     # Get the byte representation of the current element
#     bnum = flat_catImg.data[i*bsize : (i+1)*bsize].tobytes()
#     # Convert bytes to number and print
#     print(np.frombuffer(bnum, dtype=catImg.dtype)[0])