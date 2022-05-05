def repeatedString(s, n):
    # Write your code here
    x,y = divmod(n,len(s))
    return s[:y].count("a")*(x+1) + s[y:].count("a")*x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
