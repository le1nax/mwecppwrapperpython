cmake_minimum_required(VERSION 3.4)
set(PYTHON_EXECUTABLE "C:/Users/danie/AppData/Local/Programs/Python/Python37/python.exe")
project(PyC++)
add_subdirectory(pybind11)
pybind11_add_module(module_name main.cpp)

# Specify the location of the Python script
set(PYTHON_SCRIPT test_module.py)

# Set the output directory for the Python module
set(MODULE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/module")


# Create the output directory
file(MAKE_DIRECTORY ${MODULE_OUTPUT_DIRECTORY})

# Set the location of the compiled module
set_target_properties(module_name PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${MODULE_OUTPUT_DIRECTORY})