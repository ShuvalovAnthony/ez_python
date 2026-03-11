s = list("λλλ" + bin(800)[2:] + "λλλ")

state = "q0"
index = 13

while True:
    if state == "q0":
        if s[index] == "λ":
            index -= 1
            state = "q1"

    elif state == "q1":
        if s[index] == "λ":
            index += 1
            state = "q2"
        elif s[index] == "0":
            index -= 1
        elif s[index] == "1":
            index -= 1

    elif state == "q2":
        if s[index] == "0":
            index += 1
        elif s[index] == "1":
            index += 1
            state = "q3"

    elif state == "q3":
        if s[index] == "λ":
            index += 1
            state = "q4"
        elif s[index] == "0":
            index += 1
        elif s[index] == "1":
            s[index] = "0"
            index += 1
            state = "q4"
    
    elif state == "q4":
        if s[index] == "λ":
            break
        elif s[index] == "0":
            index += 1
        elif s[index] == "1":
            index += 1

print(s)