f = open("Vladimir/24/113804/24_2__6anzj.txt").read()

valid_nums = []

temp_num = ''

# '123' + *
# '4234*'

for i in range(len(f)):
    if not temp_num:
        if f[i] in "01234567":
            temp_num += f[i]
    else:
        if temp_num[-1] in '1234567':
            if f[i] in '01234567+*':
                temp_num += f[i]
            else:
                if temp_num[-1] in '*+':
                    valid_nums.append(temp_num[:-1])
                    # print(temp_num[:-1])
                else:
                    valid_nums.append(temp_num)
                    # print(temp_num)
                temp_num = ''
        elif temp_num[-1] == '0':
            if len(temp_num) == 1:
                temp_num = ''
            elif temp_num[-2] in "+*":
                if f[i] in "+*":
                    temp_num += f[i]
                else:
                    valid_nums.append(temp_num)
                    # print(temp_num)
                    temp_num = ''
            else:
                if f[i] in '01234567+*':
                    temp_num += f[i]
                else:
                    valid_nums.append(temp_num)
                    # print(temp_num)
                    temp_num = ''

        elif temp_num[-1] in '*+':
            if f[i] in "*+":
                valid_nums.append(temp_num[:-1])
                # print(temp_num[:-1])
                temp_num = ''
            elif f[i] in "01234567":
                temp_num += f[i]
            else:
                valid_nums.append(temp_num[:-1])
                # print(temp_num[:-1])
                temp_num = ''


print(
    max(
        len(i) for i in valid_nums
    )
)