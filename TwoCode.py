def TwoSum():
    text = input("Input a string here: \n")
    vals = dict()
    size = len(text)
    if size < 2:
        return "String should be longer than 2 characters."
    for i in range(0, size - 1):
        sub = text[i:i+2]
        vals[sub] = vals.get(sub, 0) + 1
    print(vals)
    return max(vals, key=vals.get)


if __name__ == "__main__":
    ans = TwoSum()
    print(ans)