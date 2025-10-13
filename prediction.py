import csv
import os

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

def load_thetas(filename='thetas.csv'):
    if not os.path.exists(filename):
        print(f"{Colors.RED}{Colors.BOLD}⚠️  Thetas file '{filename}' not found.{Colors.END}")
        print(f"{Colors.YELLOW}Tip:{Colors.END} Train your model first using:")
        print(f"   {Colors.CYAN}python3 training.py{Colors.END}\n")
        return 0.0, 0.0  
    
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                theta0 = float(row['theta0'])
                theta1 = float(row['theta1'])
                print(f"{Colors.GREEN}✔ Thetas loaded successfully!{Colors.END}\n")
                return theta0, theta1
    except Exception as e:
        print(f"{Colors.RED}✖ Error while reading {filename}: {e}{Colors.END}")
        return 0.0, 0.0

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def print_prediction_result(mileage, price):
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("╔══════════════════════════════════════╗")
    print("║           💰 PRICE ESTIMATION        ║")
    print("╠══════════════════════════════════════╣")
    print(f"║  Mileage : {mileage:10.2f} km             ║")
    print(f"║  Estimated price : {price:10.2f} €      ║")
    print("╚══════════════════════════════════════╝")
    print(f"{Colors.END}")

def main():
    print_system_header()

    theta0, theta1 = load_thetas()
    print(f"{Colors.YELLOW}θ₀ = {theta0:.6f}, θ₁ = {theta1:.6f}{Colors.END}\n")

    try:
        mileage = float(input(f"{Colors.BLUE}Enter the car mileage (km): {Colors.END}"))

        if mileage < 0:
            print(f"{Colors.RED}✖ Error: Mileage cannot be negative.{Colors.END}")
            return
        if mileage > 1e7:
            print(f"{Colors.RED}✖ Error: Mileage value is unrealistically high!{Colors.END}")
            print(f"{Colors.YELLOW}⚠ Please enter a realistic value (e.g., below 1,000,000 km).{Colors.END}")
            return

        price = estimate_price(mileage, theta0, theta1)

        if price > 1e8 or price < 0 or price == float('inf') or price != price:
            print(f"{Colors.RED}✖ Error: Computed price is out of range or invalid.{Colors.END}")
            print(f"{Colors.YELLOW}⚠ Check your model or input value.{Colors.END}")
            return

        print_prediction_result(mileage, price)

    except ValueError:
        print(f"{Colors.RED}✖ Please enter a valid numeric mileage.{Colors.END}")
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️ Operation cancelled by user.{Colors.END}")


if __name__ == "__main__":
    main()
