def main():
    while True:
        fraction = input("Fraction: ")

        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            # Check for zero division here
            if y == 0:
                raise ZeroDivisionError

            print(fuel(x, y))
            break

        except ValueError:
            print("Value Error: Provide integers like 3/4")
            continue

        except ZeroDivisionError:
            print("Zero Division Error: Denominator cannot be zero.")
            continue


def fuel(x, y):
    guage = x / y
    percent_guage = guage * 100

    if percent_guage <= 1:
        return "E"
    elif percent_guage >= 99:
        return "F"
    else:
        return f"{round(percent_guage)}%"


if __name__ == "__main__":
    main()
