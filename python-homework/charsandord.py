
start = ord("a")
end = ord("z")
i = 1

while start <= end:
    print (f"{chr(start)} {start} ", end =''),
    if i % 3 == 0:
        print("\n")
    i += 1
    start += 1
