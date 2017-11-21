def identity_print(x):      # "identity with side-effect"
    print(x)
    return x

echo_FP = lambda: identity_print(input("FP --> "))=='q' or echo_FP()
echo_FP()