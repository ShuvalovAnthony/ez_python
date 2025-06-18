min_time = int(input())
max_time = int(input())
sleep_time = int(input())


if sleep_time < min_time:
    print("Недосып")
elif sleep_time > max_time:
    print("Пересып")
else:
    print("Нормально")