output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print()

print("# 테스트")
test_a = "{:=+05d}".format(52)
print(test_a)
test_b = "{:=0+5d}".format(52)
print(test_b)
print()
