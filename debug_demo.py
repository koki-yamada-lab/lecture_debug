# debug_demo.py
import random


def calculate_average(numbers):
    """Return the average of the numbers in the list."""
    if not numbers:
        raise ValueError("The list is empty!")
    total = sum(numbers)
    avg = total / len(numbers)
    return avg


def find_closest_to_mean(numbers):
    """Return the value closest to the average."""
    avg = calculate_average(numbers)
    closest = None
    smallest_diff = float("inf")

    for n in numbers:
        diff = abs(n - avg)
        if diff < smallest_diff:
            closest = n
            smallest_diff = diff
    return closest


def generate_data(size=10):
    """Generate a list of random integers."""
    return [random.randint(0, 100) for _ in range(size)]


def main():
    print("Debug demo started.")
    data = generate_data(10)
    print("Generated data:", data)

    # Intentional bug: possible division by zero
    if random.random() < 0.3:
        data = []  # Introduce a bug condition

    try:
        closest = find_closest_to_mean(data)
        print(f"Value closest to the mean: {closest}")
    except Exception as e:
        print("An error occurred:", e)

    print("Demo finished.")


if __name__ == "__main__":
    main()
