#include "Multiply.hpp"

namespace math
{

Multiply::Multiply(){}
Multiply::Multiply(double factor1, double factor2) : factor1(factor1), factor2(factor2) {}
Multiply::~Multiply(){}

double Multiply::getFactor1()
{
    return this->factor1;
}

double Multiply::getFactor2()
{
    return this->factor2;
}

void Multiply::setFactors(double factor1, double factor2)
{
    factor1 = this->factor1;
    factor2 = this->factor2;
}
// std::vector<double> Multiply::getFactors(double factor1, double factor2)
// {
//     return ;
// }
double Multiply::multiply(double factor1, double factor2)
{
    return factor1*factor2;
}

double Multiply::multiply()
{
    return factor1*factor2;
}

}//namespace math
