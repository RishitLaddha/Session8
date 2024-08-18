# Session8

# S8.py

### Generating and Analyzing Profiles

1. **`generate_profiles(n)`**
   - **Purpose:** This function generates `n` fake profiles using the Faker library.
   - **Parameters:** `n` - an integer specifying the number of profiles to generate.
   - **Returns:** A list of `ProfileData` namedtuples, each containing `blood_group`, `current_location`, and `birthdate`.

2. **`calculate_most_common_blood_group(profiles)`**
   - **Purpose:** Determines the most frequently occurring blood group in the list of profiles.
   - **Parameters:** `profiles` - a list of `ProfileData` namedtuples.
   - **Returns:** A tuple where the first element is the most common blood group and the second element is its count.

3. **`calculate_mean_current_location(profiles)`**
   - **Purpose:** Computes the average latitude and longitude from the profiles' current locations.
   - **Parameters:** `profiles` - a list of `ProfileData` namedtuples.
   - **Returns:** A tuple containing the mean latitude and mean longitude.

4. **`calculate_oldest_and_average_age(profiles)`**
   - **Purpose:** Calculates the oldest age and the average age of individuals in the profiles.
   - **Parameters:** `profiles` - a list of `ProfileData` namedtuples.
   - **Returns:** A tuple where the first element is the oldest age, and the second element is the average age.

5. **`main_namedtuple()`**
   - **Purpose:** This is the main function for the namedtuple approach. It generates profiles, calculates various statistics, and prints the results.
   - **No Parameters.**
   - **Returns:** None (outputs results to the console).

6. **`generate_profiles_dict(n)`**
   - **Purpose:** Generates `n` fake profiles and stores them in dictionaries instead of namedtuples.
   - **Parameters:** `n` - an integer specifying the number of profiles.
   - **Returns:** A list of dictionaries where each dictionary contains `blood_group`, `current_location`, and `birthdate`.

7. **`calculate_most_common_blood_group_dict(profiles)`**
   - **Purpose:** Determines the most frequently occurring blood group from a list of dictionary profiles.
   - **Parameters:** `profiles` - a list of dictionaries containing profile data.
   - **Returns:** A tuple where the first element is the most common blood group, and the second element is its count.

8. **`calculate_mean_current_location_dict(profiles)`**
   - **Purpose:** Computes the average latitude and longitude from the dictionary profiles' current locations.
   - **Parameters:** `profiles` - a list of dictionaries containing profile data.
   - **Returns:** A tuple containing the mean latitude and mean longitude.

9. **`calculate_oldest_and_average_age_dict(profiles)`**
   - **Purpose:** Calculates the oldest age and the average age from the dictionary profiles.
   - **Parameters:** `profiles` - a list of dictionaries containing profile data.
   - **Returns:** A tuple where the first element is the oldest age, and the second element is the average age.

10. **`main_dict()`**
    - **Purpose:** This is the main function for the dictionary approach. It generates profiles, calculates various statistics, and prints the results.
    - **No Parameters.**
    - **Returns:** None (outputs results to the console).

### Timing the Performance

11. **Performance Timing**
    - **Purpose:** Measures and compares the time taken by `main_namedtuple()` and `main_dict()` to execute.
    - **No Parameters.**
    - **Returns:** Prints the execution time for both approaches.

### Generating and Analyzing Stock Data

12. **`generate_symbol(company_name)`**
    - **Purpose:** Generates a stock symbol based on the company name by using the first letters of the first two words.
    - **Parameters:** `company_name` - a string representing the name of the company.
    - **Returns:** A string representing the generated stock symbol.

13. **`create_stocks(company_names)`**
    - **Purpose:** Creates a list of `CompanyStock` namedtuples with random stock data for a list of company names.
    - **Parameters:** `company_names` - a list of company names.
    - **Returns:** A list of `CompanyStock` namedtuples, each containing `name`, `symbol`, `open`, `high`, and `close` prices.

14. **`calculate_market_value(stocks)`**
    - **Purpose:** Calculates the weighted average of the opening, high, and closing prices for the list of stocks.
    - **Parameters:** `stocks` - a list of `CompanyStock` namedtuples.
    - **Returns:** A tuple with three floats representing the market opening, high, and closing values.

# test8.py    

### Tests for Profile Generation Using Namedtuples

1. **`test_generate_profiles`**:
   - **Purpose**: To verify that the `generate_profiles` function produces the correct number of profiles and that each profile is a namedtuple.
   - **Assertions**:
     - Checks that the length of the generated profiles is 100.
     - Ensures that each profile in the list is a namedtuple.

2. **`test_calculate_most_common_blood_group`**:
   - **Purpose**: To test the `calculate_most_common_blood_group` function which calculates the most frequent blood group from the profiles.
   - **Assertions**:
     - Verifies that the result is a tuple.
     - Ensures that the first element of the tuple is a string (the blood group) and the second element is an integer (the count).

3. **`test_calculate_mean_current_location`**:
   - **Purpose**: To check the `calculate_mean_current_location` function which calculates the average latitude and longitude from the profiles.
   - **Assertions**:
     - Ensures that the latitude and longitude are floats.
     - Verifies that the latitude is within the range -90 to 90 and longitude within -180 to 180.

4. **`test_calculate_oldest_and_average_age`**:
   - **Purpose**: To test the `calculate_oldest_and_average_age` function which calculates the oldest age and average age from the profiles.
   - **Assertions**:
     - Checks that the oldest age is an integer and greater than 0.
     - Ensures that the average age is a float within a realistic range (18 to 90).

5. **`test_integration`**:
   - **Purpose**: To perform an integration test of all profile-related functions using namedtuples.
   - **Assertions**:
     - Validates the type of the results from multiple functions including `calculate_most_common_blood_group`, `calculate_mean_current_location`, and `calculate_oldest_and_average_age`.

### Tests for Profile Generation Using Dictionaries

6. **`test_generate_profiles_dict`**:
   - **Purpose**: To verify that the `generate_profiles_dict` function generates the correct number of profiles and that each profile is a dictionary.
   - **Assertions**:
     - Checks that the length of the profiles is 100.
     - Ensures that each profile is a dictionary.

7. **`test_calculate_most_common_blood_group_dict`**:
   - **Purpose**: To test the `calculate_most_common_blood_group_dict` function which calculates the most frequent blood group from profiles in dictionary format.
   - **Assertions**:
     - Verifies that the result is a tuple.
     - Ensures the tuple contains a string and an integer.

8. **`test_calculate_mean_current_location_dict`**:
   - **Purpose**: To validate the `calculate_mean_current_location_dict` function which calculates the mean latitude and longitude from profiles in dictionary format.
   - **Assertions**:
     - Ensures latitude and longitude are floats.
     - Checks that latitude and longitude are within valid geographical ranges.

9. **`test_calculate_oldest_and_average_age_dict`**:
   - **Purpose**: To test the `calculate_oldest_and_average_age_dict` function which calculates the oldest age and average age from dictionary profiles.
   - **Assertions**:
     - Verifies that the oldest age is an integer and greater than 0.
     - Ensures that the average age is a float within a realistic range.

10. **`test_integration_dict`**:
    - **Purpose**: To perform an integration test of all functions using dictionary profiles.
    - **Assertions**:
      - Validates the type and correctness of results from `calculate_most_common_blood_group_dict`, `calculate_mean_current_location_dict`, and `calculate_oldest_and_average_age_dict`.

### Performance and Edge Case Tests

11. **`test_namedtuple_vs_dict_time`**:
    - **Purpose**: To compare the performance of namedtuple-based and dictionary-based implementations.
    - **Assertions**:
      - Measures and compares the time taken by `S8.main_namedtuple` and `S8.main_dict` functions.
      - Ensures that namedtuple implementation is not slower than the dictionary-based implementation.

### Stock Tests

12. **`test_basic_functionality`**:
    - **Purpose**: To verify the basic functionality of `create_stocks` and `calculate_market_value` functions.
    - **Assertions**:
      - Checks that market opening, high, and closing values are floats.

13. **`test_symbol_generation`**:
    - **Purpose**: To test the `generate_symbol` function which generates stock symbols from company names.
    - **Assertions**:
      - Verifies that the generated symbol matches the expected value for a given company name.

14. **`test_price_range`**:
    - **Purpose**: To ensure that the prices of a `CompanyStock` object fall within expected ranges.
    - **Assertions**:
      - Checks that the high and closing prices fall within specified ranges.

15. **`test_weight_distribution`**:
    - **Purpose**: To test the normalization of weights used in market value calculations.
    - **Assertions**:
      - Ensures that the sum of normalized weights is approximately 1.

16. **`test_market_value_calculation`**:
    - **Purpose**: To validate the calculation of market values based on stock prices and weights.
    - **Assertions**:
      - Checks that the calculated market values match expected rounded results.

17. **`test_edge_case_prices`**:
    - **Purpose**: To handle edge cases where all stock prices are the same.
    - **Assertions**:
      - Verifies that market values are correctly calculated and match the identical stock prices.

18. **`test_large_dataset`**:
    - **Purpose**: To test performance and correctness with a large dataset of stocks.
    - **Assertions**:
      - Ensures market values are of type float and that the functions handle large datasets properly.

19. **`test_empty_dataset`**:
    - **Purpose**: To check how `calculate_market_value` handles an empty dataset.
    - **Assertions**:
      - Verifies that market values are zero and handles empty datasets without crashing.

20. **`test_consistency`**:
    - **Purpose**: To ensure reproducibility of market values with fixed random seed.
    - **Assertions**:
      - Checks that market values are consistent when using the same random seed.

21. **`test_randomness`**:
    - **Purpose**: To verify the randomness of market values with different random seeds.
    - **Assertions**:
      - Ensures that market values differ when using different random seeds.
