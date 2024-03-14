def calculate_simple_interest(p, t, r):
    """
    Calculate simple interest.

    Args:
        p (float): Principal amount.
        t (float): Time period in years.
        r (float): Annual rate of interest.

    Returns:
        float: Simple interest.
    """
    simple_interest = p * t * r
    return simple_interest

def main():
    # Input
    p = float(input("Enter principal amount: "))
    t = float(input("Enter time period in years: "))
    r = float(input("Enter annual rate of interest: "))

    # Calculate simple interest
    si = calculate_simple_interest(p, t, r)

    # Output
    print("Simple Interest:", si)

if __name__ == "__main__":
    main()
