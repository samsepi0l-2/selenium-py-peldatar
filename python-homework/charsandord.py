
start = ord("a")
end = ord("z")
code_matrix = ""

for i in range(start, end):
    if i < start + 10 and i+20 < end+1:
        code_matrix = code_matrix + chr(i) + " " + str(i) + " " + chr(i + 10) + " " + str(i + 10) + " " + chr(i + 20) + " " + str(i + 20) + "\n"
    else:
        code_matrix = code_matrix + chr(i) + " " + str(i) + " " + chr(i + 10) + " " + str(i + 10) + " \n"
    if i == start + 9:
        break

print(code_matrix)