import time
import basic_arithmetic as cymath


add_result = cymath.add(2,3)
print(str(add_result) + str(type(add_result)))

sub_result = cymath.sub(2,3)
print(str(sub_result) + str(type(sub_result)))

mul_result = cymath.mul(2,3)
print(str(mul_result) + str(type(mul_result)))

div_result = cymath.div(2,3)
print(str(div_result) + str(type(div_result)))




start_time_cythonSyntax = time.time()
sum_of_first_n_numbers_cythonSyntax = cymath.sum_of_first_n_numbers_cythonSyntax(100000000000)
end_time_cythonSyntax = time.time()
elapsed_time_cythonSyntax = end_time_cythonSyntax - start_time_cythonSyntax
print("sum_of_first_n_numbers_cythonSyntax=" + str(sum_of_first_n_numbers_cythonSyntax) + ", elapsed_time=" + str(elapsed_time_cythonSyntax))

start_time_purepythonSyntax = time.time()
sum_of_first_n_numbers_purepythonSyntax = cymath.sum_of_first_n_numbers_purepythonSyntax(100000000000)
end_time_purepythonSyntax = time.time()
elapsed_time_purepythonSyntax = end_time_purepythonSyntax - start_time_purepythonSyntax
print("sum_of_first_n_numbers_purepythonSyntax=" + str(sum_of_first_n_numbers_purepythonSyntax) + ", elapsed_time=" + str(elapsed_time_purepythonSyntax))

start_time_cythonCdef = time.time()
sum_of_first_n_numbers_cythonCdef = cymath.sum_of_first_n_numbers_cythonCdef(100)
end_time_cythonCdef = time.time()
elapsed_time_cythonCdef = end_time_cythonCdef - start_time_cythonCdef
print("sum_of_first_n_numbers_cythonCdef=" + str(sum_of_first_n_numbers_cythonCdef) + ", elapsed_time=" + str(elapsed_time_cythonCdef))