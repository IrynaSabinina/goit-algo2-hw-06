# task2.py
import time
import re
from hyperloglog import HyperLogLog  # Import the custom HyperLogLog class

# Load IPs from the log file
def load_ips_from_log(file_path):
    ip_addresses = set()
    with open(file_path, 'r') as file:
        for line in file:
            # Regex to extract IP addresses
            match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            if match:
                ip_addresses.add(match.group(0))
    return ip_addresses

# Exact counting of unique IPs
def exact_count(ips):
    return len(ips)

# Performance comparison between exact counting and HyperLogLog
def compare_performance(file_path):
    # Loading IPs from the log file
    print("Завантаження даних з файлу...")
    start_time = time.time()
    ips = load_ips_from_log(file_path)
    load_time = time.time() - start_time

    # Exact counting
    print("\nПідрахунок точним методом...")
    start_time = time.time()
    exact_result = exact_count(ips)
    exact_time = time.time() - start_time

    # HyperLogLog counting
    print("\nПідрахунок за допомогою HyperLogLog...")
    start_time = time.time()
    hll = HyperLogLog(p=14)
    for ip in ips:
        hll.add(ip)
    hll_result = hll.count()
    hll_time = time.time() - start_time

    # Display results in a comparative table
    print("\nРезультати порівняння:")
    print(f"{'Метод':<20}{'Унікальні елементи':<25}{'Час виконання (сек.)':<20}")
    print(f"{'Точний підрахунок':<20}{exact_result:<25}{exact_time:.6f}")
    print(f"{'HyperLogLog':<20}{hll_result:<25}{hll_time:.6f}")
    print(f"Час завантаження файлу: {load_time:.6f} сек.")

if __name__ == "__main__":
    file_path = "lms-stage-access.log"  # Path to your log file
    compare_performance(file_path)
