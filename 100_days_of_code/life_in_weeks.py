datebirth = input("Enter your birthday (YYYY-MM-DD): ")
print(datebirth)

age_now = input("What is your age? ")

for i in range(40):
    # print(f"{i:>2}", end="")
    for j in range(52):
        if i < int(age_now):
            print("\u25A6 ", end="")  # \u25FC \u25FB \u25A5 \u25A4 \u25A3
        else:
            print("\u25A1 ", end="")
    print()
