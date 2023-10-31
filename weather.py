import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # parse the input iso date string
    parsed_date = datetime.fromisoformat(iso_string)

    # format the parsed date as Weekday Date Month Year
    formatted_date = parsed_date.strftime('%A %d %B %Y')
    return formatted_date

    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # parse the farenheit float
    parsed_temp = float(temp_in_farenheit)

    # convert to celsius and round result to 1 dp
    celsius = round((parsed_temp - 32)*(5/9), 1)

    return celsius

    pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # Initialize sum and count variables
    total_sum = 0
    count = 0

    # Loop to convert each data point to a float and append in a new list
    for item in weather_data:
        total_sum += float(item)
        # Increase the count
        count += 1

    # Calculate the mean
    mean_value = total_sum / count

    return mean_value

    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # Initialise an empty list
    data = []

    # Using a context manager to open the file
    with open(csv_file, 'r', newline='') as csv_file:

        # creating a csv.reader object to grab the data
        reader = csv.reader(csv_file)

        # Skip the header row
        next(reader)

        # loop to convert data in each row into a list
        for item in reader:
            # skip empty lines
            if not item:
                continue

            # Convert min and max values to integers and store each list row in a variable
            row_list = [item[0], int(item[1]), int(item[2])]

            # Create a list of lists
            data.append(row_list)

        return data

    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list.
    """
    # Handle empty list cases
    if not weather_data:
        return ()

    # find the minimum value and store in a variable
    min_value = min(weather_data)

    # initialize last index as None
    last_index = None

    # Iterate the list from right to left, in decreasing increments of 1
    for i in range(len(weather_data) - 1, -1, -1):
        if weather_data[i] == min_value:
            last_index = i
            break  # exit the loop after finding the last occurence

    return float(min_value), last_index

    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

    if not weather_data:
        # Handle empty list cases
        return ()

    # find the maximum value
    max_value = max(weather_data)

    # initialize last index as None
    last_index = None

    # Iterate the list from right to left
    for i in range(len(weather_data) - 1, -1, -1):
        if weather_data[i] == max_value:
            last_index = i
            break  # exit the loop after finding the last occurence

    return float(max_value), last_index

    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    rows_num = 0
    converted_list = []

    for sublist in (weather_data):
        rows_num += 1  # increment the row count
        iso_date_daily, min_temp, max_temp = sublist  # unpack the sublist
        # convert date to human-readable format
        human_readable_date = convert_date(iso_date_daily)

        # convert temperatures from Fahrenheit to Celsius
        min_temp_celcius = convert_f_to_c(min_temp)
        max_temp_celcius = convert_f_to_c(max_temp)

        # create a new sublist with converted data
        coverted_sublist = [human_readable_date,
                            min_temp_celcius, max_temp_celcius]

        # Append the converted sublist to the converted_list
        converted_list.append(coverted_sublist)

        # break  # exit the loop after finding the last occurence

    # Calculate lowest and highest temperatures
    lowest_temp = min([day[1] for day in converted_list])
    highest_temp = max([day[2] for day in converted_list])

    # Find dates for lowest and highest temperatures
    lowest_date = next(day[0]
                       for day in converted_list if day[1] == lowest_temp)
    highest_date = next(day[0]
                        for day in converted_list if day[2] == highest_temp)

    # Calculate average low and average high
    total_low = sum([day[1] for day in converted_list])
    total_high = sum([day[2] for day in converted_list])
    ave_low = round(total_low / rows_num, 1)
    ave_high = round(total_high / rows_num, 1)

    summary += f"{rows_num} Day Overview\n"
    summary += f"  The lowest temperature will be {lowest_temp}{DEGREE_SYBMOL}, and will occur on {lowest_date}.\n"
    summary += f"  The highest temperature will be {highest_temp}{DEGREE_SYBMOL}, and will occur on {highest_date}.\n"
    summary += f"  The average low this week is {ave_low}{DEGREE_SYBMOL}.\n"
    summary += f"  The average high this week is {ave_high}{DEGREE_SYBMOL}.\n"

    return summary

    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for sublist in (weather_data):
        iso_date_daily, min_temp, max_temp = sublist
        human_readable_date = convert_date(iso_date_daily)
        min_temp_celcius = convert_f_to_c(min_temp)
        max_temp_celcius = convert_f_to_c(max_temp)
        summary += f"---- {human_readable_date} ----\n"
        summary += f"  Minimum Temperature: {min_temp_celcius}{DEGREE_SYBMOL}\n"
        summary += f"  Maximum Temperature: {max_temp_celcius}{DEGREE_SYBMOL}\n\n"

    return summary

    pass
