def miles_per_gallon(start, end, fuel):
    return (end - start) / fuel

def lp100k_from_mpg(mpg):
    return 235.215 / mpg

def main():
    start = float(input("Enter first odometer value in miles: "))
    end = float(input("Enter second odometer value in miles: "))
    fuel = float(input("Enter amount of fuel in gallons: "))

    mpg = miles_per_gallon(start, end, fuel)
    lp100k = lp100k_from_mpg(mpg)

    print("Fuel efficiency: {:.2f} miles per gallon".format(mpg))
    print("Fuel efficiency: {:.2f} liters per 100 kilometers".format(lp100k))

if __name__ == "__main__":
    main()
