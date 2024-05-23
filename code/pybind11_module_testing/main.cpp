#ifdef _WIN64
#define _hypot hypot
#include <cmath>
#endif

#include <iostream>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <Eigen/CXX11/Tensor>

namespace py = pybind11;

float addFloat(float arg1, float arg2)
{
    return arg1 + arg2;
}



py::array_t<float> 
multiply_3d_arrays_using_eigenlibs(py::array_t<float, py::array::c_style | py::array::forcecast> arr1,
                                       py::array_t<float, py::array::c_style | py::array::forcecast> arr2) {
    auto buf1 = arr1.request();
    auto buf2 = arr2.request();
    auto ptr1 = static_cast<float *>(buf1.ptr);
    auto ptr2 = static_cast<float *>(buf2.ptr);

    int dim1 = buf1.shape[0];
    int dim2 = buf1.shape[1];
    int dim3 = buf1.shape[2];

    Eigen::TensorMap<Eigen::Tensor<float, 3>> tensor1(ptr1, dim1, dim2, dim3);
    Eigen::TensorMap<Eigen::Tensor<float, 3>> tensor2(ptr2, dim1, dim2, dim3);

    Eigen::Tensor<float, 3> result = tensor1 * tensor2;

    py::array_t<float> result_arr({dim1, dim2, dim3});
    auto result_buf = result_arr.request();
    auto result_ptr = static_cast<float *>(result_buf.ptr);

    std::memcpy(result_ptr, result.data(), dim1 * dim2 * dim3 * sizeof(float));

    return result_arr;
}

py::array_t<float> 
multiply_3d_arrays_using_stdvector(py::array_t<float, py::array::c_style | py::array::forcecast> arr1,
                                      py::array_t<float, py::array::c_style | py::array::forcecast> arr2) {
    auto buf1 = arr1.request();
    auto buf2 = arr2.request();
    auto ptr1 = static_cast<float *>(buf1.ptr);
    auto ptr2 = static_cast<float *>(buf2.ptr);

    std::vector<std::vector<std::vector<float>>> vec1(buf1.shape[0], std::vector<std::vector<float>>(buf1.shape[1], std::vector<float>(buf1.shape[2])));
    std::vector<std::vector<std::vector<float>>> vec2(buf2.shape[0], std::vector<std::vector<float>>(buf2.shape[1], std::vector<float>(buf2.shape[2])));

    //arr1 to vector
    for (size_t i = 0; i < buf1.shape[0]; ++i) {
        for (size_t j = 0; j < buf1.shape[1]; ++j) {
            for (size_t k = 0; k < buf1.shape[2]; ++k) {
                vec1[i][j][k] = *ptr1++;
            }
        }
    }

    //arr2 to vector
    for (size_t i = 0; i < buf2.shape[0]; ++i) {
        for (size_t j = 0; j < buf2.shape[1]; ++j) {
            for (size_t k = 0; k < buf2.shape[2]; ++k) {
                vec2[i][j][k] = *ptr2++;
            }
        }
    }

    //matrix mul
    std::vector<std::vector<std::vector<float>>> result(vec1.size(), std::vector<std::vector<float>>(vec2[0].size(), std::vector<float>(vec2[0][0].size(), 0)));

    for (size_t i = 0; i < vec1.size(); ++i) {
        for (size_t j = 0; j < vec2[0].size(); ++j) {
            for (size_t k = 0; k < vec2[0][0].size(); ++k) {
                for (size_t m = 0; m < vec1[0].size(); ++m) {
                    result[i][j][k] += vec1[i][m][k] * vec2[m][j][k];
                }
            }
        }
    }

    //result to numpy array
    py::array_t<float> result_arr({result.size(), result[0].size(), result[0][0].size()});
    auto result_buf = result_arr.request();
    auto result_ptr = static_cast<float *>(result_buf.ptr);

    for (size_t i = 0; i < result.size(); ++i) {
        for (size_t j = 0; j < result[0].size(); ++j) {
            for (size_t k = 0; k < result[0][0].size(); ++k) {
                *result_ptr++ = result[i][j][k];
            }
        }
    }

    return result_arr;
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
    handle.def("multiply_3d_arrays_using_stdvector", &multiply_3d_arrays_using_stdvector);
    handle.def("multiply_3d_arrays_using_eigenlibs", &multiply_3d_arrays_using_eigenlibs);

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