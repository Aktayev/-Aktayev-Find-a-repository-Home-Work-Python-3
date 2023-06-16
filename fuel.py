
def main():
    fraction = input("Fraction: ")
    con_fr = convert(fraction)
    percent = gauge(con_fr)
    print(percent)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x_f = int(x)
            y_f = int(y)
            f_xy = x_f/y_f
            if f_xy<=1:
                p = int(f_xy*100)
                return p
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            raise
def gauge(percentage):
    if percentage<=1:
        return ("E")
    elif percentage>=99:
        return ("F")
    else:
        return (f"{percentage}%")


if __name__=="__main__":
    main()

