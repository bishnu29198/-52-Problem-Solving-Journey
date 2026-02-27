t=int(input().strip())
for i in range(t):
    n = input().strip()# number as string
    last_digit = n[-1] # last character
    if int(last_digit)%2==0:
        print("even")
    else:
        print("odd")
