import sys
import os
import cv2

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))
# Append the relative path to the build module
sys.path.append(os.path.join(script_dir, "build", "module"))

import module_name
from module_name import *

result = module_name.addFloat(3.5, 2.5)
print("Result of addFloat:", result)

testClass = TestClass(5)

print(testClass.multiply_list([1, 3, 10]))

print(testClass.multiply(2))

print(testClass.image)

print(testClass.image.shape)

cv2.imwrite("/tmp/test.png", testClass.image)