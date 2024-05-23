cmake_minimum_required(VERSION 3.4)
# set(PYTHON_EXECUTABLE "C:/Users/danie/AppData/Local/Programs/Python/Python37/python.exe")
# set(PYTHON_EXECUTABLE "/opt/homebrew/bin/python3")

# Set the C++ standard to C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)  # Ensure the standard is respected
set(CMAKE_CXX_EXTENSIONS False)  # Avoid compiler-specific extensions

project(PyC++)
add_subdirectory(pybind11)
pybind11_add_module(module_name main.cpp)

# Specify the location of the Python script
# set(PYTHON_SCRIPT test_pybind11.py)# TODO not needed?

# Set the output directory for the Python module
set(MODULE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/module")

# Set path to Eigen directory
set(EIGEN_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/eigen/unsupported)

# Add Eigen to include directories
include_directories(${EIGEN_INCLUDE_DIR})

# Create the output directory
file(MAKE_DIRECTORY ${MODULE_OUTPUT_DIRECTORY})

# Set the location of the compiled module
set_target_properties(module_name PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${MODULE_OUTPUT_DIRECTORY})

