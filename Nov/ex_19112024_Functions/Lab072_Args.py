def print_mul_arguments(*args):
    # *args -> List
    for i in args:
        print(i)


print_mul_arguments("pramod")
print_mul_arguments("pramod", "amit", "lucky")
print_mul_arguments("amit", 10, True, False, "PRAMOD")