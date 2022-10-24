file1 = open(r"Task5_file1.txt","r")
file2 = open(r"Task5_file2.txt","r")
result_file = open(r"Task5_resultfile.txt","w")

first_polynomial = file1.readline().split(" + ")
second_polynomial = file2.readline().split(" + ")

first_polynomial_coeffs = []
second_polynomial_coeffs = []
result_polynomial_coeffs = []

for i in first_polynomial:
    first_polynomial_coeffs.append(int(i[0]))

for i in second_polynomial:
    second_polynomial_coeffs.append(int(i[0]))

if (len(first_polynomial_coeffs) > len(second_polynomial_coeffs)):
    while (len(first_polynomial_coeffs) > len(second_polynomial_coeffs)):
        second_polynomial_coeffs.append(0)
else:
    if (len(first_polynomial_coeffs) < len(second_polynomial_coeffs)):
        while (len(first_polynomial_coeffs) < len(second_polynomial_coeffs)):
            first_polynomial_coeffs.append(0)

for i in range(len(first_polynomial_coeffs)):
    result_polynomial_coeffs.append(first_polynomial_coeffs[i] + second_polynomial_coeffs[i])


for i in range(len(result_polynomial_coeffs) - 1, -1, -1):
    result_file.write(f"{result_polynomial_coeffs[i]}x^{i} + ")
