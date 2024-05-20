def calculate_min_cost(seats, car_types):
    # Initialize dp array where dp[i] is the minimum cost for i seats
    max_seats = seats + max(car['seats'] for car in car_types)
    dp = [float('inf')] * (max_seats + 1)
    dp[0] = 0  # No cost for 0 seats

    # Track which car combination was used for each dp value
    combination = [None] * (max_seats + 1)

    for i in range(1, max_seats + 1):
        for car in car_types:
            if i >= car['seats']:
                if dp[i - car['seats']] + car['cost'] < dp[i]:
                    dp[i] = dp[i - car['seats']] + car['cost']
                    combination[i] = car['name']

    # Retrieve the optimal combination from the dp array
    result = []
    n = seats
    while n > 0:
        for car in car_types:
            if combination[n] == car['name']:
                result.append(car['name'])
                n -= car['seats']
                break

    # Count each type of car used
    from collections import Counter
    result_count = Counter(result)

    # Output the result
    for car, count in result_count.items():
        print(f"{car} x {count}")
    print(f"Total = PHP {dp[seats]}")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python car_rental.py <number_of_seats>")
        return

    seats = int(sys.argv[1])
    
    car_types = [
        {'name': 'S', 'seats': 5, 'cost': 5000},
        {'name': 'M', 'seats': 10, 'cost': 8000},
        {'name': 'L', 'seats': 15, 'cost': 12000}
    ]

    calculate_min_cost(seats, car_types)

if __name__ == "__main__":
    main()
