output_a = "{:d}".format(52)

output_b = "{:5d}".format(52)
output_c = "{:10}".format(52)

output_d = "{:05}".format(52)
output_e = "{:05}".format(-52)

print("# 기본")
print(output_a)

print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)

print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

print()
