
#pragma once

#include <vector>

namespace math
{
    class Multiply 
    {
        public:
            Multiply();
            Multiply(double factor1, double factor2);
            ~Multiply();

        private:
            double factor1;
            double factor2;

        public:
            double getFactor1();
            double getFactor2();
            void setFactors(double factor1, double factor2);
            // std::vector<double> getFactors();
            double multiply(double factor1, double factor2);//TODO const einbauen
            double multiply();
    };
}
/*some more TODOs
- pointer

*/ 
