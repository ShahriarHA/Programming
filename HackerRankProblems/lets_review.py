t = int(input().strip())
for _ in range(0,t):
    s = input().strip()
    s1 = s2 = ""
    for j in range(len(s)):
        if j%2 == 0:
            s1 = s1 + s[j]
            # print(s[j])
        else:
            s2 = s2 + s[j]
            # print(s[j])
    print(f"{s1} {s2}")

