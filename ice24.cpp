#include <iostream>
#include <stdlib.h>
#include <math.h>

double evaluateIntegral(int N)
{
        double dx = 1.0/N;
        double integral = 0.0;
        for( int i =0; i < N; i++) {
                double x = (i+0.5)*dx;
                for( int j =0; j < N; j++) {
                        double y = (j+0.5)*dx;
                        for( int k =0; k < N; k++) {
                                double z = (k+0.5)*dx;
                                integral += std::exp(x*y*z) * dx*dx*dx;
                        }
                }
        }
        return integral;
}

int main(int argc, char *argv[])
{
        int n = atoi(argv[1]);
        std::cout.precision(14);
        std::cout << "integral (with n = " << n << ") = "
                << evaluateIntegral(n) << std::endl;
        return 0;
}