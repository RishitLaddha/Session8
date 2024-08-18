from faker import Faker
from collections import namedtuple, Counter
from datetime import datetime
from statistics import mean
import time
import random
# Initialize Faker
fake = Faker()

# Define the namedtuple for storing profile data
ProfileData = namedtuple('ProfileData', ['blood_group', 'current_location', 'birthdate'])

def generate_profiles(n):
    """Generate n profiles using Faker and store relevant data in a namedtuple."""
    profiles = []
    for _ in range(n):
        profile = fake.profile()
        profiles.append(ProfileData(
            blood_group=profile['blood_group'],
            current_location=profile['current_location'],
            birthdate=profile['birthdate']
        ))
    return profiles

def calculate_most_common_blood_group(profiles):
    """Calculate the most common blood group from the list of profiles."""
    blood_groups = [profile.blood_group for profile in profiles]
    most_common_blood_group = Counter(blood_groups).most_common(1)[0]
    return most_common_blood_group

def calculate_mean_current_location(profiles):
    """Calculate the mean current location (latitude and longitude) from the list of profiles."""
    mean_latitude = float(mean([float(profile.current_location[0]) for profile in profiles]))
    mean_longitude = float(mean([float(profile.current_location[1]) for profile in profiles]))
    return mean_latitude, mean_longitude

def calculate_oldest_and_average_age(profiles):
    """Calculate the oldest person's age and the average age from the list of profiles."""
    current_year = datetime.now().year
    ages = [(current_year - profile.birthdate.year) for profile in profiles]
    oldest_age = max(ages)
    average_age = mean(ages)
    return oldest_age, average_age

def main_namedtuple():
    # Generate 10,000 profiles
    profiles = generate_profiles(10000)

    # Calculate results
    most_common_blood_group = calculate_most_common_blood_group(profiles)
    mean_latitude, mean_longitude = calculate_mean_current_location(profiles)
    oldest_age, average_age = calculate_oldest_and_average_age(profiles)

    # Output the results
    print(f"Most Common Blood Group: {most_common_blood_group[0]} with {most_common_blood_group[1]} occurrences")
    print(f"Mean Current Location: Latitude {mean_latitude:.4f}, Longitude {mean_longitude:.4f}")
    print(f"Oldest Person's Age: {oldest_age} years")
    print(f"Average Age: {average_age:.2f} years")

def generate_profiles_dict(n):
    """Generate n profiles using Faker and store relevant data in a dictionary."""
    profiles = []
    for _ in range(n):
        profile = fake.profile()
        profiles.append({
            'blood_group': profile['blood_group'],
            'current_location': profile['current_location'],
            'birthdate': profile['birthdate']
        })
    return profiles

def calculate_most_common_blood_group_dict(profiles):
    """Calculate the most common blood group from the list of dictionary profiles."""
    blood_groups = [profile['blood_group'] for profile in profiles]
    most_common_blood_group = Counter(blood_groups).most_common(1)[0]
    return most_common_blood_group

def calculate_mean_current_location_dict(profiles):
    """Calculate the mean current location (latitude and longitude) from the list of dictionary profiles."""
    mean_latitude = float(mean([float(profile['current_location'][0]) for profile in profiles]))
    mean_longitude = float(mean([float(profile['current_location'][1]) for profile in profiles]))
    return mean_latitude, mean_longitude

def calculate_oldest_and_average_age_dict(profiles):
    """Calculate the oldest person's age and the average age from the list of dictionary profiles."""
    current_year = datetime.now().year
    ages = [(current_year - profile['birthdate'].year) for profile in profiles]
    oldest_age = max(ages)
    average_age = mean(ages)
    return oldest_age, average_age

def main_dict():
    # Generate 10,000 profiles
    profiles = generate_profiles_dict(10000)

    # Calculate results
    most_common_blood_group = calculate_most_common_blood_group_dict(profiles)
    mean_latitude, mean_longitude = calculate_mean_current_location_dict(profiles)
    oldest_age, average_age = calculate_oldest_and_average_age_dict(profiles)

    # Output the results
    print(f"Most Common Blood Group (Dict): {most_common_blood_group[0]} with {most_common_blood_group[1]} occurrences")
    print(f"Mean Current Location (Dict): Latitude {mean_latitude:.4f}, Longitude {mean_longitude:.4f}")
    print(f"Oldest Person's Age (Dict): {oldest_age} years")
    print(f"Average Age (Dict): {average_age:.2f} years")

# Time the performance
if __name__ == "__main__":
    # Timing namedtuple version
    start_namedtuple = time.time()
    main_namedtuple()
    end_namedtuple = time.time()

    # Timing dict version
    start_dict = time.time()
    main_dict()
    end_dict = time.time()

    # Print timing results
    print(f"Namedtuple Time: {end_namedtuple - start_namedtuple:.4f} seconds")
    print(f"Dict Time: {end_dict - start_dict:.4f} seconds")

################################################################################
# Generate 100 company names
company_names = [fake.company() for _ in range(100)]

# Define the CompanyStock namedtuple
CompanyStock = namedtuple('CompanyStock', ['name', 'symbol', 'open', 'high', 'close'])

# Function to generate a random stock symbol
def generate_symbol(company_name):
    """
    Generates a stock symbol from a company name.

    This function creates a stock symbol by taking the first letter of each of the 
    first two words in the company name and converting them to uppercase. For example, 
    "International Business Machines" will result in the symbol "IB".

    Args:
        company_name (str): The name of the company from which to generate the symbol.

    Returns:
        str: The generated stock symbol.
    """
    return ''.join(word[0].upper() for word in company_name.split()[:2])

# Function to create stocks with generated data
def create_stocks(company_names):
    """
    Creates a list of `CompanyStock` objects with random stock data.

    This function generates a list of `CompanyStock` objects for the given company names. 
    Each stock has a random opening price between 100 and 500, a high price that is 
    equal to or higher than the opening price, and a closing price that is between 95% 
    of the opening price and the high price.

    Args:
        company_names (list of str): List of company names for which to create stocks.

    Returns:
        list of CompanyStock: A list of `CompanyStock` objects with randomly generated data.
    """
    stocks = []
    for company_name in company_names:
        symbol = generate_symbol(company_name)
        open_price = round(random.uniform(100, 500), 2)  # Random opening price between 100 and 500
        high_price = round(random.uniform(open_price, open_price * 1.1), 2)  # High should be equal to or higher than open
        close_price = round(random.uniform(open_price * 0.95, high_price), 2)  # Close can be less, equal to, or higher than open
        stocks.append(CompanyStock(company_name, symbol, open_price, high_price, close_price))
    return stocks

# Function to calculate the market value based on stock data
def calculate_market_value(stocks):
    """
    Calculates the market value based on the list of `CompanyStock` objects and random weights.

    This function computes the weighted average of the opening, high, and closing prices of 
    the stocks. The weights are randomly generated and normalized to sum up to 1.

    Args:
        stocks (list of CompanyStock): List of `CompanyStock` objects for which to calculate market values.

    Returns:
        tuple: A tuple containing three floats representing the market opening, high, and closing values.
    """
    weights = [random.random() for _ in range(len(stocks))]
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]
    market_open = sum(stock.open * weight for stock, weight in zip(stocks, normalized_weights))
    market_high = sum(stock.high * weight for stock, weight in zip(stocks, normalized_weights))
    market_close = sum(stock.close * weight for stock, weight in zip(stocks, normalized_weights))
    return market_open, market_high, market_close

# Generate stock data
stocks = create_stocks(company_names)

# Calculate market values
market_open, market_high, market_close = calculate_market_value(stocks)

# Display the results
print(f"Stock Market Opening Value: {market_open:.2f}")
print(f"Stock Market Highest Value During the Day: {market_high:.2f}")
print(f"Stock Market Closing Value: {market_close:.2f}")
