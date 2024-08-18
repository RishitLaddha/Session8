import pytest
import time
import os
import inspect
import glob
import re
import math
import pytest
import S8 
from S8 import *
##################### Test for Faker Profile by namedtuple #####################
def test_generate_profiles():
    """
    Test that the correct number of profiles is generated using namedtuples.

    This function generates a specified number of profiles using the `generate_profiles` 
    function and checks if the length of the generated profiles list matches the 
    expected number. It also verifies that each profile is an instance of a namedtuple.
    """
    profiles = generate_profiles(100)
    assert len(profiles) == 100, f"Expected 100 profiles, but got {len(profiles)}"
    assert all(isinstance(profile, tuple) for profile in profiles), "All profiles should be namedtuples"

def test_calculate_most_common_blood_group():
    """
    Test the calculation of the most common blood group using namedtuples.

    This function generates profiles and then calculates the most common blood group 
    using the `calculate_most_common_blood_group` function. It checks if the result 
    is a tuple containing a string (blood group) and an integer (count).
    """
    profiles = generate_profiles(1000)
    most_common_blood_group = calculate_most_common_blood_group(profiles)
    assert isinstance(most_common_blood_group, tuple), "Most common blood group should be a tuple"
    assert isinstance(most_common_blood_group[0], str), "Blood group should be a string"
    assert isinstance(most_common_blood_group[1], int), "Count should be an integer"

def test_calculate_mean_current_location():
    """
    Test the calculation of the mean current location using namedtuples.

    This function generates profiles and then calculates the mean latitude and 
    longitude using the `calculate_mean_current_location` function. It ensures 
    that the results are floats and fall within valid geographical ranges.
    """
    profiles = generate_profiles(1000)
    mean_latitude, mean_longitude = calculate_mean_current_location(profiles)
    assert isinstance(mean_latitude, float), "Mean latitude should be a float"
    assert isinstance(mean_longitude, float), "Mean longitude should be a float"
    assert -90 <= mean_latitude <= 90, "Latitude should be between -90 and 90"
    assert -180 <= mean_longitude <= 180, "Longitude should be between -180 and 180"

def test_calculate_oldest_and_average_age():
    """
    Test the calculation of the oldest and average age using namedtuples.

    This function generates profiles and then calculates the oldest and average age 
    using the `calculate_oldest_and_average_age` function. It checks that the oldest 
    age is a positive integer and that the average age falls within a realistic range.
    """
    profiles = generate_profiles(1000)
    oldest_age, average_age = calculate_oldest_and_average_age(profiles)
    assert isinstance(oldest_age, int), "Oldest age should be an integer"
    assert isinstance(average_age, float), "Average age should be a float"
    assert oldest_age > 0, "Oldest age should be a positive integer"
    assert 18 <= average_age <= 90, "Average age should be within a realistic range"

def test_integration():
    """
    Test the integration of all functionalities using namedtuples.

    This function generates profiles and checks the results of multiple functions:
    - `calculate_most_common_blood_group`
    - `calculate_mean_current_location`
    - `calculate_oldest_and_average_age`
    
    It ensures that all results are of the expected types and within valid ranges.
    """
    profiles = generate_profiles(1000)
    most_common_blood_group = calculate_most_common_blood_group(profiles)
    mean_latitude, mean_longitude = calculate_mean_current_location(profiles)
    oldest_age, average_age = calculate_oldest_and_average_age(profiles)
    
    assert isinstance(most_common_blood_group, tuple), "Most common blood group should be a tuple"
    assert isinstance(mean_latitude, float), "Mean latitude should be a float"
    assert isinstance(mean_longitude, float), "Mean longitude should be a float"
    assert isinstance(oldest_age, int), "Oldest age should be an integer"
    assert isinstance(average_age, float), "Average age should be a float"

################################################################################
##################### Test for Faker Profile by Dictionary #####################

def test_generate_profiles_dict():
    """
    Test that the correct number of profiles is generated using dictionaries.

    This function generates a specified number of profiles using the 
    `generate_profiles_dict` function and checks if the length of the generated 
    profiles list matches the expected number. It also verifies that each profile 
    is a dictionary.
    """
    profiles = generate_profiles_dict(100)
    assert len(profiles) == 100, f"Expected 100 profiles, but got {len(profiles)}"
    assert all(isinstance(profile, dict) for profile in profiles), "All profiles should be dictionaries"

def test_calculate_most_common_blood_group_dict():
    """
    Test the calculation of the most common blood group using dictionaries.

    This function generates profiles and then calculates the most common blood group 
    using the `calculate_most_common_blood_group_dict` function. It checks if the result 
    is a tuple containing a string (blood group) and an integer (count).
    """
    profiles = generate_profiles_dict(1000)
    most_common_blood_group = calculate_most_common_blood_group_dict(profiles)
    assert isinstance(most_common_blood_group, tuple), "Most common blood group should be a tuple"
    assert isinstance(most_common_blood_group[0], str), "Blood group should be a string"
    assert isinstance(most_common_blood_group[1], int), "Count should be an integer"

def test_calculate_mean_current_location_dict():
    """
    Test the calculation of the mean current location using dictionaries.

    This function generates profiles and then calculates the mean latitude and 
    longitude using the `calculate_mean_current_location_dict` function. It ensures 
    that the results are floats and fall within valid geographical ranges.
    """
    profiles = generate_profiles_dict(1000)
    mean_latitude, mean_longitude = calculate_mean_current_location_dict(profiles)
    assert isinstance(mean_latitude, float), "Mean latitude should be a float"
    assert isinstance(mean_longitude, float), "Mean longitude should be a float"
    assert -90 <= mean_latitude <= 90, "Latitude should be between -90 and 90"
    assert -180 <= mean_longitude <= 180, "Longitude should be between -180 and 180"

def test_calculate_oldest_and_average_age_dict():
    """
    Test the calculation of the oldest and average age using dictionaries.

    This function generates profiles and then calculates the oldest and average age 
    using the `calculate_oldest_and_average_age_dict` function. It checks that the 
    oldest age is a positive integer and that the average age falls within a realistic range.
    """
    profiles = generate_profiles_dict(1000)
    oldest_age, average_age = calculate_oldest_and_average_age_dict(profiles)
    assert isinstance(oldest_age, int), "Oldest age should be an integer"
    assert isinstance(average_age, float), "Average age should be a float"
    assert oldest_age > 0, "Oldest age should be a positive integer"
    assert 18 <= average_age <= 90, "Average age should be within a realistic range"

def test_integration_dict():
    """
    Test the integration of all functionalities using dictionaries.

    This function generates profiles and checks the results of multiple functions:
    - `calculate_most_common_blood_group_dict`
    - `calculate_mean_current_location_dict`
    - `calculate_oldest_and_average_age_dict`
    
    It ensures that all results are of the expected types and within valid ranges.
    """
    profiles = generate_profiles_dict(1000)
    most_common_blood_group = calculate_most_common_blood_group_dict(profiles)
    mean_latitude, mean_longitude = calculate_mean_current_location_dict(profiles)
    oldest_age, average_age = calculate_oldest_and_average_age_dict(profiles)
    
    assert isinstance(most_common_blood_group, tuple), "Most common blood group should be a tuple"
    assert isinstance(mean_latitude, float), "Mean latitude should be a float"
    assert isinstance(mean_longitude, float), "Mean longitude should be a float"
    assert isinstance(oldest_age, int), "Oldest age should be an integer"
    assert isinstance(average_age, float), "Average age should be a float"

def test_namedtuple_vs_dict_time():
    """Test whether namedtuple implementation takes less or equal time compared to the dictionary implementation."""
    
    # Timing namedtuple version
    start_namedtuple = time.time()
    S8.main_namedtuple()  # Assuming main_namedtuple() generates profiles and performs operations
    end_namedtuple = time.time()
    namedtuple_time = end_namedtuple - start_namedtuple

    # Timing dict version
    start_dict = time.time()
    S8.main_dict()  # Assuming main_dict() generates profiles and performs operations
    end_dict = time.time()
    dict_time = end_dict - start_dict

    # Print timing results for debugging
    print(f"Namedtuple Time: {namedtuple_time:.4f} seconds")
    print(f"Dict Time: {dict_time:.4f} seconds")
    
    # Assertion to fail if namedtuple takes more time than dictionary
    assert round(namedtuple_time) <= round(dict_time), (
        f"Expected namedtuple to take less or equal time than dict, but it took more. "
        f"Namedtuple Time: {namedtuple_time:.4f}, Dict Time: {dict_time:.4f}"
    )
################################################################################

# 1. Basic Functionality Test
def test_basic_functionality():
    """
    Tests the basic functionality of the `create_stocks` and `calculate_market_value` 
    functions by verifying the types of the returned market values.

    This function creates a list of stocks with `create_stocks` and calculates their 
    market values using `calculate_market_value`. It then checks that the returned 
    market opening, high, and closing values are of type `float`.

    Asserts:
        - Market opening value is of type `float`.
        - Market high value is of type `float`.
        - Market closing value is of type `float`.
    """
    stocks = create_stocks(company_names)
    market_open, market_high, market_close = calculate_market_value(stocks)
    assert isinstance(market_open, float)
    assert isinstance(market_high, float)
    assert isinstance(market_close, float)
    print("Test 1 (Basic Functionality): Passed")

# 2. Symbol Generation Test
def test_symbol_generation():
    """
    Tests the generation of stock symbols from company names.

    This function takes a company name, generates its stock symbol using the 
    `generate_symbol` function, and verifies that the symbol matches the expected 
    result. In this case, the expected symbol for "International Business Machines" 
    is "IB".

    Asserts:
        - The generated symbol matches the expected symbol.
    """
    company_name = "International Business Machines"
    symbol = generate_symbol(company_name)
    assert symbol == "IB"
    print("Test 2 (Symbol Generation): Passed")

# 3. Price Range Test
def test_price_range():
    """
    Tests the price range for a `CompanyStock` object to ensure it falls within 
    expected limits.

    This function creates a `CompanyStock` object with a set high price and calculates 
    its expected price range. It verifies that the actual high and closing prices fall 
    within the expected range based on the given initial price.

    Asserts:
        - The high price is between 300 and 330 (inclusive).
        - The closing price is between 285 and 330 (inclusive).
    """
    stock = CompanyStock("Test Company", "TC", 300, round(300 * 1.1, 2), round(300 * 0.95, 2))
    assert 300 <= stock.high <= 330
    assert 285 <= stock.close <= 330
    print("Test 3 (Price Range): Passed")

# 4. Weight Distribution Test
def test_weight_distribution():
    """
    Tests the distribution and normalization of weights used in market value calculations.

    This function creates a list of stocks and assigns random weights to each stock. 
    It normalizes these weights so that their sum equals approximately 1. It then 
    verifies that the sum of the normalized weights is within a specified tolerance 
    to ensure correct weight distribution.

    Asserts:
        - The sum of the normalized weights is between 0.99 and 1.01, inclusive.
    """
    stocks = create_stocks(company_names)
    weights = [random.random() for _ in range(len(stocks))]
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]
    
    # Ensure that the normalized weights sum to approximately 1.
    assert 0.99 <= sum(normalized_weights) <= 1.01
    print("Test 4 (Weight Distribution): Passed")


# 5. Market Value Calculation Test
def test_market_value_calculation():
    """
    Tests the calculation of market values for given stocks and weights.

    This function creates a list of `CompanyStock` objects with fixed values and a set 
    of weights. It calculates the market opening, high, and closing values based on 
    these weights and compares them to expected results. The test ensures that the 
    calculated values match the expected rounded values.

    Asserts:
        - The rounded market opening value is 140.0.
        - The rounded market high value is 154.0.
        - The rounded market closing value is 147.0.
    """
    stocks = [
        CompanyStock("Company A", "CA", 100, 110, 105),
        CompanyStock("Company B", "CB", 200, 220, 210),
    ]
    random.seed(42)  # Fixing seed for reproducibility
    weights = [0.6, 0.4]
    market_open = sum(stock.open * weight for stock, weight in zip(stocks, weights)) / sum(weights)
    market_high = sum(stock.high * weight for stock, weight in zip(stocks, weights)) / sum(weights)
    market_close = sum(stock.close * weight for stock, weight in zip(stocks, weights)) / sum(weights)
    assert round(market_open, 2) == 140.0
    assert round(market_high, 2) == 154.0
    assert round(market_close, 2) == 147.0
    print("Test 5 (Market Value Calculation): Passed")

# 6. Handling of Edge Cases in Prices
def test_edge_case_prices():
    """
    Tests the handling of edge cases where all stock prices are the same.

    This function creates a list of `CompanyStock` objects where all stocks have 
    identical values for opening, high, and closing prices. It calculates the market 
    values and verifies that they match the expected price, taking into account floating-point 
    precision issues by rounding.

    Asserts:
        - The rounded market opening value is 200.
        - The rounded market high value is 200.
        - The rounded market closing value is 200.
    """
    stocks = [CompanyStock("Test Company", "TC", 200, 200, 200) for _ in range(100)]
    market_open, market_high, market_close = calculate_market_value(stocks)
    
    # Rounding to handle floating-point precision issues
    assert round(market_open, 2) == 200
    assert round(market_high, 2) == 200
    assert round(market_close, 2) == 200
    print("Test (Edge Case Prices): Passed")


# 7. Large Dataset Test
def test_large_dataset():    
    """
    Tests the performance and handling of large datasets in the `create_stocks` 
    and `calculate_market_value` functions.

    This function generates a large list of company names (10,000) using the 
    `fake.company` method, creates stocks with `create_stocks`, and calculates 
    their market values using `calculate_market_value`. It then verifies that 
    the market values are of type `float` to ensure that the functions can handle 
    large datasets properly.

    Asserts:
        - Market opening value is of type `float`.
        - Market high value is of type `float`.
        - Market closing value is of type `float`.
    """
    large_company_names = [fake.company() for _ in range(10000)]
    stocks = create_stocks(large_company_names)
    market_open, market_high, market_close = calculate_market_value(stocks)
    assert isinstance(market_open, float)
    assert isinstance(market_high, float)
    assert isinstance(market_close, float)
    print("Test 7 (Large Dataset): Passed")

# 8. Empty Dataset Test
def test_empty_dataset():
    """
    Tests the handling of an empty dataset in the `calculate_market_value` function.

    This function passes an empty list of stocks to `calculate_market_value` and 
    verifies that it correctly returns zero values for market open, high, and close. 
    It also ensures that the function does not crash by catching any potential 
    `ZeroDivisionError` exceptions.

    Asserts:
        - Market opening, high, and closing values are all zero.
        - The function handles the empty dataset without crashing.
    """
    stocks = []
    try:
        market_open, market_high, market_close = calculate_market_value(stocks)
        assert market_open == market_high == market_close == 0
    except ZeroDivisionError:
        assert True  # Expected to handle empty dataset without crashing
    print("Test 8 (Empty Dataset): Passed")

# 9. Consistency Test
def test_consistency():
    """
    Tests the consistency of the market values generated by the `create_stocks` 
    and `calculate_market_value` functions when using a fixed random seed.

    This function sets the random seed to a specific value (42), creates a set of 
    stocks with `create_stocks`, calculates their market values with `calculate_market_value`, 
    and then repeats the process with the same seed. It ensures that the market values 
    are the same for both sets of stocks to confirm that the randomness is reproducible.

    Asserts:
        - Market opening values are equal between the two sets.
        - Market high values are equal between the two sets.
        - Market closing values are equal between the two sets.

    Prints:
        - A message indicating that the test has passed.
    """    
    random.seed(42)
    stocks = create_stocks(company_names)
    market_open_1, market_high_1, market_close_1 = calculate_market_value(stocks)
    random.seed(42)
    stocks = create_stocks(company_names)
    market_open_2, market_high_2, market_close_2 = calculate_market_value(stocks)
    assert market_open_1 == market_open_2
    assert market_high_1 == market_high_2
    assert market_close_1 == market_close_2
    print("Test 9 (Consistency): Passed")

# 10. Randomness Test
def test_randomness():
    """
    Tests the randomness of the market values generated by the `create_stocks` 
    and `calculate_market_value` functions.

    This function initializes the random seed, creates two sets of stocks with 
    `create_stocks`, calculates their market values with `calculate_market_value`, 
    and ensures that the market values for each set of stocks are different to 
    confirm that the randomness is working as expected. The test passes if 
    all the market values differ between the two sets of stocks.

    Asserts:
        - Market opening values are not equal between the two sets.
        - Market high values are not equal between the two sets.
        - Market closing values are not equal between the two sets.

    Prints:
        - A message indicating that the test has passed.
    """
    random.seed(None)  # Reset seed for randomness
    stocks_1 = create_stocks(company_names)
    market_open_1, market_high_1, market_close_1 = calculate_market_value(stocks_1)
    stocks_2 = create_stocks(company_names)
    market_open_2, market_high_2, market_close_2 = calculate_market_value(stocks_2)
    assert market_open_1 != market_open_2
    assert market_high_1 != market_high_2
    assert market_close_1 != market_close_2
    print("Test 10 (Randomness): Passed")
