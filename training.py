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

def load_data(path:str):
    try: 
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                mileages.append(float(row['km']))
                prices.append(float(row['price']))
        print(f"{Colors.GREEN}Loaded {len(mileages)} entries from {path}{Colors.END}")
        return mileages, prices
    except FileNotFoundError:
        print(f"{Colors.RED}Error: The file {path} was not found.{Colors.END}")
        return [], []
    except Exception as e:
        print(f"{Colors.RED}An error occurred: {e}{Colors.END}")
        return [], []

def export_thetas(theta0, theta1, filename="thetas.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['theta0', 'theta1'])
        writer.writerow([theta0, theta1])

def denormalize_data(theta0, theta1, mileages, prices):
    min_mileage = min(mileages)
    max_mileage = max(mileages)
    min_price = min(prices)
    max_price = max(prices)

    real_theta1 = theta1 * (max_price - min_price) / (max_mileage - min_mileage)
    real_theta0 = (theta0 * (max_price - min_price)) + min_price - (real_theta1 * min_mileage)
    return real_theta0, real_theta1
    
def normalize_data(mileages, prices):
    min_mileage = min(mileages)
    max_mileage = max(mileages)
    min_price = min(prices)
    max_price = max(prices)
    
    norm_mileages = [(m - min_mileage) / (max_mileage - min_mileage) for m in mileages]
    norm_prices = [(p - min_price) / (max_price - min_price) for p in prices]
    
    return norm_mileages, norm_prices

def train_model(norm_mileages, norm_prices):
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
            print(f"Itération {i}: θ₀={theta0:.6f}, θ₁={theta1:.6f}")
    print(f"theatas finaux Theta0 = {theta0} --- Theta1 = {theta1}")
    theta0, theta1 = denormalize_data(theta0, theta1, mileages, prices)
    return theta0, theta1


def main():
    load_data("data.csv")
    m = len(mileages)
    norm_mileages, norm_prices = normalize_data(mileages, prices)
    theta0, theta1 = train_model(norm_mileages, norm_prices)
    export_thetas(theta0, theta1)
    print(theta0, theta1)

if __name__ == "__main__":
    main()