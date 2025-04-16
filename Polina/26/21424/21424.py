f = open("Polina/26/21424/26_21424.txt")


n = int(f.readline())

boxes = sorted([int(i) for i in f], reverse=True)


approved_boxes = [boxes[0]]


for box in boxes[1:]:
    if box + 9 <= approved_boxes[-1]:
        approved_boxes.append(box)

print(len(approved_boxes), approved_boxes[-1])