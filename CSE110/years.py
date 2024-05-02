import csv

# Load the dataset
with open('life_expectancy_dataset.csv', newline='') as csvfile:
    dataset = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    # Find the year and country with the lowest and highest life expectancy
    min_life_exp = float('inf')
    max_life_exp = float('-inf')
    min_year = ''
    min_country = ''
    max_year = ''
    max_country = ''
    for row in dataset:
        if row[3] != '':
            life_exp = float(row[3])
            if life_exp < min_life_exp:
                min_life_exp = life_exp
                min_year = row[0]
                min_country = row[1]
            if life_exp > max_life_exp:
                max_life_exp = life_exp
                max_year = row[0]
                max_country = row[1]
                
    # Print the year and country with the lowest and highest life expectancy
    print(f'The year and country with the lowest life expectancy is {min_year} in {min_country} with a life expectancy of {min_life_exp:.2f}.')
    print(f'The year and country with the highest life expectancy is {max_year} in {max_country} with a life expectancy of {max_life_exp:.2f}.')
    
    # Allow the user to type in a year, then find the average life expectancy for that year and the country with the minimum and maximum life expectancies for that year
    year = input('Enter a year: ')
    avg_life_exp = 0
    count = 0
    min_life_exp = float('inf')
    min_country = ''
    max_life_exp = float('-inf')
    max_country = ''
    for row in dataset:
        if row[0] == year and row[3] != '':
            life_exp = float(row[3])
            avg_life_exp += life_exp
            count += 1
            if life_exp < min_life_exp:
                min_life_exp = life_exp
                min_country = row[1]
            if life_exp > max_life_exp:
                max_life_exp = life_exp
                max_country = row[1]
    if count == 0:
        print('No data for that year.')
    else:
        avg_life_exp /= count
        print(f'The average life expectancy for {year} is {avg_life_exp:.2f}.')
        print(f'The country with the minimum life expectancy for {year} is {min_country} with a life expectancy of {min_life_exp:.2f}.')
        print(f'The country with the maximum life expectancy for {year} is {max_country} with a life expectancy of {max_life_exp:.2f}.')
    
    # Look for interesting anomalies or patterns in the data.
    # This can be done by analyzing the data visually using charts or graphs or by performing statistical analysis.
