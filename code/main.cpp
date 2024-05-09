#ifdef _WIN64
#define _hypot hypot
#include <cmath>
#endif

#include <pybind11/pybind11.h>
namespace py = pybind11;

float addFloat(float arg1, float arg2)
{
    return arg1 + arg2;
}

PYBIND11_MODULE(module_name, handle){
    handle.doc() = "This is the module docs.";
    handle.def("addFloat", &addFloat); 
}