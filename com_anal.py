import matplotlib.pyplot as plt
import json
import numpy as np
from scipy.optimize import curve_fit

def plot_from_time(time):
    # Convert time values to milliseconds
    time_ms = {k: v * 1000 for k, v in time.items()}

    # Extract input sizes and times
    input_sizes = np.array(list(time_ms.keys()), dtype=float)
    times = np.array(list(time_ms.values()), dtype=float)

    # Perform regression to estimate Big-O
    def linear(x, a, b):
        return a * x + b

    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

    def cubic(x, a, b, c, d):
        return a * x**3 + b * x**2 + c * x + d

    # Fit the data to different models
    popt_linear, _ = curve_fit(linear, input_sizes, times)
    popt_quadratic, _ = curve_fit(quadratic, input_sizes, times)
    popt_cubic, _ = curve_fit(cubic, input_sizes, times)

    # Calculate R-squared for each model
    def r_squared(y, y_pred):
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - (ss_res / ss_tot)

    r2_linear = r_squared(times, linear(input_sizes, *popt_linear))
    r2_quadratic = r_squared(times, quadratic(input_sizes, *popt_quadratic))
    r2_cubic = r_squared(times, cubic(input_sizes, *popt_cubic))

    # Determine the best fit
    print("R-squared values:")
    print(f"Linear: {r2_linear:.4f}")
    print(f"Quadratic: {r2_quadratic:.4f}")
    print(f"Cubic: {r2_cubic:.4f}")

    if r2_cubic > r2_quadratic and r2_cubic > r2_linear:
        print("Best fit: O(n^3) (Cubic)")
    elif r2_quadratic > r2_linear:
        print("Best fit: O(n^2) (Quadratic)")
    else:
        print("Best fit: O(n) (Linear)")

    # Plot the data and the regression curves
    plt.figure(figsize=(10, 6))
    plt.scatter(input_sizes, times, label="Data", color="blue")
    plt.plot(input_sizes, linear(input_sizes, *popt_linear), label="Linear Fit (O(n))", color="green")
    plt.plot(input_sizes, quadratic(input_sizes, *popt_quadratic), label="Quadratic Fit (O(n^2))", color="orange")
    plt.plot(input_sizes, cubic(input_sizes, *popt_cubic), label="Cubic Fit (O(n^3))", color="red")
    plt.title('Input Size vs Time with Regression')
    plt.xlabel('Input Size')
    plt.ylabel('Time (ms)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Load the times dictionary from the JSON file
    with open("times.json", "r") as f:
        time = json.load(f)

    plot_from_time(time)