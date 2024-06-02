#pragma once

#include <iostream>
#include <eigen/Eigen/Dense>

// using namespace std;

void 
printEigenMatrix(const Eigen::Map<Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic>> &mat) 
{
    std::cout << mat << "\n";
}