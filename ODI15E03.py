def main():
    # a, b = [int(x) for x in "7 -21".split()]
    a, b = [int(x) for x in input().split()]

    gcd = lambda a, b: a if not b else gcd(b, a % b)
    result = abs(gcd(a, b))
    
    print(result)


main()
