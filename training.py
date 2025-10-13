import sys
import csv
import matplotlib.pyplot as plt

mileages = []
prices = []
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_system_header():

    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║            CAR PRICE PREDICTION SYSTEM                   ║")
    print("║              AI-Powered Price Estimator                  ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}\n")

def print_training_summary(theta0, theta1):
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("╔════════════════════════════════════════════╗")
    print("║             ✅ Training Complete!          ║")
    print("╠════════════════════════════════════════════╣")
    print(f"║  Final θ₀ : {theta0:12.6f}                   ║")
    print(f"║  Final θ₁ : {theta1:12.6f}                   ║")
    print("╚════════════════════════════════════════════╝")
    print(f"{Colors.END}")

def load_data(path:str):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            if 'km' not in reader.fieldnames or 'price' not in reader.fieldnames:
                print(f"{Colors.RED}Error: Missing 'km' or 'price' column in {path}{Colors.END}")
                return [], []
            for row in reader:
                try:
                    mileages.append(float(row['km']))
                    prices.append(float(row['price']))
                except ValueError:
                    print(f"{Colors.YELLOW}⚠ Skipping invalid row: {row}{Colors.END}")
        if not mileages:
            print(f"{Colors.RED}Error: No valid data found in {path}{Colors.END}")
            return [], []
        print(f"{Colors.GREEN}✅ Loaded {len(mileages)} entries from {path}{Colors.END}")
        return mileages, prices
    except FileNotFoundError:
        print(f"{Colors.RED}✖ Error: The file {path} was not found.{Colors.END}")
        return [], []
    except PermissionError:
        print(f"{Colors.RED}✖ Error: No permission to read the file {path}.{Colors.END}")
        return [], []
    except Exception as e:
        print(f"{Colors.RED}✖ Unexpected error while loading data: {e}{Colors.END}")
        return [], []


def export_thetas(theta0, theta1, filename="thetas.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['theta0', 'theta1'])
        writer.writerow([theta0, theta1])

def denormalize_data(theta0, theta1, mileages, prices):
    if not mileages or not prices:
        print(f"{Colors.RED}✖ Error: Cannot denormalize empty data.{Colors.END}")
        return 0, 0

    min_mileage, max_mileage = min(mileages), max(mileages)
    min_price, max_price = min(prices), max(prices)

    if max_mileage == min_mileage:
        print(f"{Colors.RED}✖ Error: Invalid mileage data — cannot denormalize.{Colors.END}")
        return 0, 0

    real_theta1 = theta1 * (max_price - min_price) / (max_mileage - min_mileage)
    real_theta0 = (theta0 * (max_price - min_price)) + min_price - (real_theta1 * min_mileage)
    print_training_summary(real_theta0, real_theta1)
    return real_theta0, real_theta1

    
def normalize_data(mileages, prices):
    if len(mileages) < 2 or len(prices) < 2:
        print(f"{Colors.RED}✖ Error: Not enough data points to normalize.{Colors.END}")
        return [], []

    min_mileage, max_mileage = min(mileages), max(mileages)
    min_price, max_price = min(prices), max(prices)

    if max_mileage == min_mileage or max_price == min_price:
        print(f"{Colors.RED}✖ Error: Cannot normalize — all values are identical.{Colors.END}")
        return [], []

    norm_mileages = [(m - min_mileage) / (max_mileage - min_mileage) for m in mileages]
    norm_prices = [(p - min_price) / (max_price - min_price) for p in prices]

    return norm_mileages, norm_prices


def train_model(norm_mileages, norm_prices):
    print_system_header()
    theta0 = 0
    theta1 = 0
    iter = 1000
    learning_rate = 0.1
    m = len(norm_mileages)

    for i in range(iter):
        sum_theta0 = 0
        for j in range(m):
            estimation = theta0 + (theta1 * norm_mileages[j])
            error = estimation - norm_prices[j]
            sum_theta0 = sum_theta0 + error
        tmp_theta0 = learning_rate * (sum_theta0 / m)
        
        sum_theta1 = 0
        for j in range(m):
            estimation = theta0 + (theta1 * norm_mileages[j])
            error = estimation - norm_prices[j]
            sum_theta1 = sum_theta1 + (error * norm_mileages[j])
        tmp_theta1 = learning_rate * (sum_theta1 / m)

        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1
        if i % 100 == 0:
            print(f"Itération {i}: {Colors.BLUE}θ₀={theta0:.6f}{Colors.END}, {Colors.RED}θ₁={theta1:.6f}{Colors.END}")
    theta0, theta1 = denormalize_data(theta0, theta1, mileages, prices)
    return theta0, theta1

def data_graph(theta0=None, theta1=None):
    plt.figure(figsize=(7, 5))
    plt.scatter(mileages, prices, color='blue', label='Training Data', alpha=0.6)

    if theta0 is not None and theta1 is not None:
        x_line = [min(mileages), max(mileages)]
        y_line = [theta0 + theta1 * x for x in x_line]
        plt.plot(x_line, y_line, color='red', label='Regression Line', linewidth=2)

    plt.title("Linear Regression — Mileage vs Price", fontsize=14, fontweight='bold')
    plt.xlabel("Mileage (km)", fontsize=12)
    plt.ylabel("Price (€)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


import sys

def main():
    show_graph = "-b" in sys.argv

    mileages, prices = load_data("data.csv")

    if not mileages or not prices:
        print(f"{Colors.RED}{Colors.BOLD}✖ Training aborted: No valid data loaded.{Colors.END}")
        return

    if show_graph:
        print(f"{Colors.CYAN}📊 Displaying data graph before training...{Colors.END}")
        data_graph()

    norm_mileages, norm_prices = normalize_data(mileages, prices)
    theta0, theta1 = train_model(norm_mileages, norm_prices)
    export_thetas(theta0, theta1)

    if show_graph:
        print(f"{Colors.GREEN}📈 Displaying regression result...{Colors.END}")
        data_graph(theta0, theta1)

if __name__ == "__main__":
    main()