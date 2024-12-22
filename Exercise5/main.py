def runner(i):
    print(f"Runner{i}:")
    name = input("Name: ")
    time = int(input("Time (in seconds): "))
    return (name, time)

runner1 = runner(1)
runner2 = runner(2)

if runner1[1] == runner2[1]:
    print(f"{runner1[0]} and {runner2[0]} have the same time")
elif runner1[1] > runner2[1]:
    print(f"The faster runner is {runner2[0]}")
else:
    print(f"The faster runner is {runner1[0]}")

