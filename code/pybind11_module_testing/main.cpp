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



// py::array_t<float> 
// multiply_3d_arrays_using_eigenlibs(py::array_t<float, py::array::c_style | py::array::forcecast> arr1,
//                                        py::array_t<float, py::array::c_style | py::array::forcecast> arr2) {
//     auto buf1 = arr1.request();
//     auto buf2 = arr2.request();
//     auto ptr1 = static_cast<float *>(buf1.ptr);
//     auto ptr2 = static_cast<float *>(buf2.ptr);

//     int dim1 = buf1.shape[0];
//     int dim2 = buf1.shape[1];
//     int dim3 = buf1.shape[2];

//     std::cout << "dim1: " << dim1 << std::endl;
//     std::cout << "dim2: " << dim2 << std::endl;
//     std::cout << "dim3: " << dim3 << std::endl;

//     Eigen::TensorMap<Eigen::Tensor<float, 3>> tensor1(ptr1, dim1, dim2, dim3);
//     Eigen::TensorMap<Eigen::Tensor<float, 3>> tensor2(ptr2, dim1, dim2, dim3);

//     Eigen::Tensor<float, 3> result = tensor1 * tensor2;

//     py::array_t<float> result_arr({dim1, dim2, dim3});
//     auto result_buf = result_arr.request();
//     auto result_ptr = static_cast<float *>(result_buf.ptr);

//     std::memcpy(result_ptr, result.data(), dim1 * dim2 * dim3 * sizeof(float));

//     return result_arr;
// }

void
test_ordering(py::array_t<float, py::array::c_style | py::array::forcecast> arr1)
{
    py::buffer_info buf1 = arr1.request();
    float *ptr1 = static_cast<float*>(buf1.ptr);

    // Print strides for debugging
    std::cout << "Strides: ";
    for (auto stride : buf1.strides) 
    {
        std::cout << stride << " ";
    }
    std::cout << std::endl;

    std::cout << "First matrix on third dimension: " << *ptr1 << ", " << *(ptr1 + 1) << ", " << *(ptr1 + 2) << ", " << *(ptr1 + 3) << std::endl;
    std::cout << "Second matrix on third dimesion: " << *(ptr1 + 4) << ", " << *(ptr1 + 5) << ", " << *(ptr1 + 6) << ", " << *(ptr1 + 7) << std::endl;
    std::cout << "Third matrix on third dimesion: " << *(ptr1 + 8) << ", " << *(ptr1 + 9) << ", " << *(ptr1 + 10) << ", " << *(ptr1 + 11) << std::endl;
}

void
test_ordering2(py::array_t<float, py::array::c_style | py::array::forcecast> arr1,
               py::array_t<float, py::array::c_style | py::array::forcecast> arr2) 
{
    py::buffer_info buf1 = arr1.request();
    py::buffer_info buf2 = arr2.request();
    float *ptr1 = static_cast<float*>(buf1.ptr);
    float *ptr2 = static_cast<float*>(buf2.ptr);

    // Print the matrices correctly interpreting C_CONTIGUOUS order
    std::cout << "First matrix on third dimension: " 
              << ptr1[0] << ", " << ptr1[2] << ", " << ptr1[4] << ", " << ptr1[6] << std::endl;
    std::cout << "Second matrix on third dimension: " 
              << ptr1[1] << ", " << ptr1[3] << ", " << ptr1[5] << ", " << ptr1[7] << std::endl;
    std::cout << "Third matrix on third dimension: " 
              << ptr1[8] << ", " << ptr1[10] << ", " << ptr1[9] << ", " << ptr1[11] << std::endl;
}

// TODO: Eigen::Tensor should be a better fit for higher order matrix manipulations
py::array_t<float> 
multiply_3d_arrays_using_eigenlibs(py::array_t<float, py::array::c_style | py::array::forcecast> arr1,
                                   py::array_t<float, py::array::c_style | py::array::forcecast> arr2) 
{
    py::buffer_info buf1 = arr1.request();// contains information on the array: Shape and Strides, a pointer, size and data type
    py::buffer_info buf2 = arr2.request();
    float *ptr1 = static_cast<float*>(buf1.ptr);// buf1.ptr is of type void*, so cast to float*
    float *ptr2 = static_cast<float*>(buf2.ptr);

    int arr1_dim1 = buf1.shape[0]; // Rows of the 2D matrices
    int arr1_dim2 = buf1.shape[1]; // Columns of the 2D matrices
    int arr1_dim3 = buf1.shape[2]; // Number of 2D matrices in the 3rd dimension

    int arr2_dim1 = buf2.shape[0]; // Rows of the 2D matrices
    int arr2_dim2 = buf2.shape[1]; // Columns of the 2D matrices
    int arr2_dim3 = buf2.shape[2]; // Number of 2D matrices in the 3rd dimension

    // std::cout << "arr1_dim1=" << arr1_dim1 << ", arr1_dim2=" << arr1_dim2 << ", arr1_dim3=" << arr1_dim3 << std::endl;
    // std::cout << "arr2_dim1=" << arr2_dim1 << ", arr2_dim2=" << arr2_dim2 << ", arr1_dim3=" << arr2_dim3 << std::endl;

    // std::cout << "First matrix on third dimension: " << *ptr1 << ", " << *(ptr1 + 1) << ", " << *(ptr1 + 2) << ", " << *(ptr1 + 3) << std::endl;
    // std::cout << "Second matrix on third dimesion: " << *(ptr1 + 4) << ", " << *(ptr1 + 5) << ", " << *(ptr1 + 6) << ", " << *(ptr1 + 7) << std::endl;
    // std::cout << "Third matrix on third dimesion: " << *(ptr1 + 8) << ", " << *(ptr1 + 9) << ", " << *(ptr1 + 10) << ", " << *(ptr1 + 11) << std::endl;

    // std::cout << arr1 << std::endl;

    // // Ensure that the input arrays have the correct shapes
    // if (arr1_dim2 != arr2_dim1 || arr1_dim3 != arr2_dim3) 
    // {
    //     throw std::runtime_error("Shapes of arr1 and arr2 are not compatible for matrix multiplication.");
    // }

    int result_rows = arr1_dim1;
    int result_cols = arr2_dim2; // Columns of the second array's 2D matrices

    py::array_t<float> result_arr({result_rows, result_cols, arr1_dim3});
    py::buffer_info result_buf = result_arr.request();
    float *result_ptr = static_cast<float *>(result_buf.ptr);

    for (int i = 0; i < arr1_dim1; ++i) 
    {
        Eigen::Map<Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>> mat1(ptr1 + i * arr1_dim2 * arr1_dim3, arr1_dim2, arr1_dim3);
        // std::cout << mat1 << std::endl;
        // std::cout << std::endl;
        Eigen::Map<Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>> mat2(ptr2 + i * arr2_dim2 * arr2_dim3, arr2_dim2, arr2_dim3);
        // std::cout << mat2 << std::endl;
        // std::cout << std::endl;
        Eigen::Map<Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>> mat_result(result_ptr + i * result_cols * arr1_dim3, result_cols, arr1_dim3);
        // std::cout << mat_result << std::endl;
        // std::cout << std::endl;

        mat_result.noalias() = mat1 * mat2; // Matrix multiplication
        // std::cout << mat_result << std::endl;
        // std::cout << std::endl;
        // Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor> mat_result_rowMajor = mat_result;
        // mat_result = mat1 * mat2; // Matrix multiplication
    }

    // std::cout << "First matrix on third dimension: " << *ptr1 << ", " << *(ptr1 + 1) << ", " << *(ptr1 + 2) << ", " << *(ptr1 + 3) << std::endl;
    // std::cout << "Second matrix on third dimesion: " << *(ptr1 + 4) << ", " << *(ptr1 + 5) << ", " << *(ptr1 + 6) << ", " << *(ptr1 + 7) << std::endl;
    // std::cout << "Third matrix on third dimesion: " << *(ptr1 + 8) << ", " << *(ptr1 + 9) << ", " << *(ptr1 + 10) << ", " << *(ptr1 + 11) << std::endl;

    return result_arr;
}

template <typename T>
py::array_t<T>
multiply_3d_arrays_using_eigenlibs_template(py::array_t<T, py::array::c_style | py::array::forcecast> arr1,
                                            py::array_t<T, py::array::c_style | py::array::forcecast> arr2)
{
    py::buffer_info buf1 = arr1.request();// contains information on the array: Shape and Strides, a pointer, size and data type
    py::buffer_info buf2 = arr2.request();
    T *ptr1 = static_cast<T*>(buf1.ptr);// buf1.ptr is of type void*, so cast to float*
    T *ptr2 = static_cast<T*>(buf2.ptr);

    const int arr1_dim1 = buf1.shape[0]; // Rows of the 2D matrices
    const int arr1_dim2 = buf1.shape[1]; // Columns of the 2D matrices
    const int arr1_dim3 = buf1.shape[2]; // Number of 2D matrices in the 3rd dimension

    const int arr2_dim1 = buf2.shape[0]; // Rows of the 2D matrices
    const int arr2_dim2 = buf2.shape[1]; // Columns of the 2D matrices
    const int arr2_dim3 = buf2.shape[2]; // Number of 2D matrices in the 3rd dimension

    const int result_rows = arr1_dim1;
    const int result_cols = arr2_dim2; // Columns of the second array's 2D matrices

    py::array_t<T> result_arr({result_rows, result_cols, arr1_dim3});
    py::buffer_info result_buf = result_arr.request();
    T *result_ptr = static_cast<T *>(result_buf.ptr);

    for (int i = 0; i < arr1_dim1; ++i) 
    {
        Eigen::Map<Eigen::Matrix<T, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>> mat1(ptr1 + i * arr1_dim2 * arr1_dim3, arr1_dim2, arr1_dim3);
        Eigen::Map<Eigen::Matrix<T, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>> mat2(ptr2 + i * arr2_dim2 * arr2_dim3, arr2_dim2, arr2_dim3);
        Eigen::Map<Eigen::Matrix<T, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>> mat_result(result_ptr + i * result_cols * arr1_dim3, result_cols, arr1_dim3);

        mat_result.noalias() = mat1 * mat2; // Matrix multiplication
    }

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
    handle.def("multiply_3d_arrays_using_eigenlibs_template", &multiply_3d_arrays_using_eigenlibs_template<float>, "Multiply 3D arrays (float)");
    handle.def("multiply_3d_arrays_using_eigenlibs_template", &multiply_3d_arrays_using_eigenlibs_template<double>, "Multiply 3D arrays (double)");
    handle.def("multiply_3d_arrays_using_eigenlibs_template", &multiply_3d_arrays_using_eigenlibs_template<int>, "Multiply 3D arrays (int)");
    handle.def("test_ordering", &test_ordering);
    handle.def("test_ordering2", &test_ordering2);

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