#ifdef _WIN64
#define _hypot hypot
#include <cmath>
#endif

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
namespace py = pybind11;

float addFloat(float arg1, float arg2)
{
    return arg1 + arg2;
}

class TestClass{
    public:
        TestClass(float mul){
            multiplier = mul;
        }
    private:

        float multiplier;

    public:
        float multiply(float input_mul){
            return input_mul*multiplier;
        }
        std::vector<float> multiply_list(std::vector<float> items){
            for(auto i = 0; i < items.size() ; ++i){
                items[i] = multiply(items.at(i)); 
            }
            return items;
        }
        std::vector<std::vector<uint8_t>> make_image() {
        auto out = std::vector<std::vector<uint8_t>>();
        for (auto i = 0; i < 128; i++) {
            out.push_back(std::vector<uint8_t>(64));
        }
        for (auto i = 0; i < 30; i++) { 
            for (auto j = 0; j < 30; j++) {
                out[i][j] = 255;
                }
            }
    return out;
  }

};

PYBIND11_MODULE(module_name, handle){
    handle.doc() = "This is the module docs.";
    handle.def("addFloat", &addFloat); 

    py::class_<TestClass>(handle, "TestClass")
        .def(py::init<float>())
        .def("multiply", &TestClass::multiply)
        .def("multiply_list", &TestClass::multiply_list)
        .def("make_image", [](TestClass &self){
                            py::array out = py::cast(self.make_image());
                            return out;
                            })
        .def_property_readonly("image", [](TestClass &self) {
				      py::array out = py::cast(self.make_image());
				      return out;
				    })
        ;
}