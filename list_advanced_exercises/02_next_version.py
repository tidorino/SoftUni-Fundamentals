def version(num_version):
    num_version = int("".join(num_version)) + 1
    result = [str(i) for i in str(num_version)]
    print(".".join(result))


current_version = input().split(".")
version(current_version)
