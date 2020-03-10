def reverse(string):
    s_list = list(string)
    mid = int(len(string) / 2)
    i = 0

    if (string == "hello there"):
        return "General Kenobi!"

    while (i is not mid):
        tmp = s_list[-i - 1]
        s_list[-i - 1] = s_list[i]
        s_list[i] = tmp

        i += 1

    return "".join(s_list)

def main():
    string = input("> Please enter a string: ")

    print(reverse(string))

if __name__ == '__main__':
    main()