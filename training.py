import csv
import matplotlib.pyplot as plt


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
    mileages = []
    prices = []
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


def training_model():
    theta0 = 0
    theta1 = 0
    learning_rate = 0.01
    
def normalize_data(mileages):
    min_mileage = min(mileages)
    max_mileage = max(mileages)
    
    #normalized_miles = (miles - min_mileage) / (max_mileage - min_mileage)
    print(f"{max_mileage} - {min_mileage}")


def main():
    mileages, prices = load_data("data.csv")
    m = len(mileages)
    normalize_data(mileages)

if __name__ == "__main__":
    main()