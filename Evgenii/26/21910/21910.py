f = open("Evgenii/26/21910/26_21910.txt")

n = int(f.readline())

boxes = sorted(set([int(i) for i in f]), reverse=True)


aprroved_boxes = [boxes[0]]


for box in boxes[1:]:
    if box + 9 <= aprroved_boxes[-1]:
        aprroved_boxes.append(box)


print(len(aprroved_boxes), aprroved_boxes[-1])

