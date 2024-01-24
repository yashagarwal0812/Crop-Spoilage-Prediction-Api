import random
import csv
# from faker import Faker
from datetime import datetime, timedelta

# fake = Faker()


def wheatSpoilage(temperature, oxygen, moisture_content, light, pesticide):
    T = 0;
    if temperature < 0:
        T = 1;
    elif temperature < 15:
        T = 5
    elif temperature < 25:
        T = 8
    else: 
        T = 14


    P = 0;
    if pesticide == 0:
        P = 8
    L = 0;
    if light == 2:
        L = 8
    elif light == 1:
        L = 4
    else:
        L = 1


    O = 0;
    if oxygen<1:
        O = 1
    elif oxygen<5:
        O = 4
    else:
        O = 9


    M = 0;
    if moisture_content<14:
        M = 3
    elif moisture_content <16:
        M = 6
    else:
        M = 11
    
    spoilage = 10 + M + O + T + L + P 
    return spoilage



def riceSpoilage(temperature, oxygen, moisture_content, light, pesticide):
    T = 0;
    if temperature < 0:
        T = 1;
    elif temperature < 15:
        T = 5
    elif temperature < 25:
        T = 8
    elif temperature < 35:
        T = 13
    else: 
        T = 18


    P = 0;
    if pesticide == 0:
        P = 9


    L = 0;
    if light == 2:
        L = 8
    elif light == 1:
        L = 4
    else:
        L = 1


    O = 0;
    if oxygen<1:
        O = 1
    elif oxygen<1:
        O = 2
    elif oxygen<5:
        O = 5
    else:
        O = 9


    M = 0;
    if moisture_content<12:
        M = 2
    elif moisture_content <13:
        M = 3
    elif moisture_content <15:
        M = 5
    elif moisture_content <16:
        M = 6
    elif moisture_content <18:
        M = 9
    else:
        M = 14
    spoilage = 10 + M + O + T + L + P 
    return spoilage



def cornSpoilage(temperature, oxygen, moisture_content, light, pesticide):
    T = 0;
    if temperature < 0:
        T = 8
    elif temperature < 15:
        T = 3
    elif temperature < 25:
        T = 1
    elif temperature < 35:
        T = 5
    else: 
        T = 9


    P = 0;
    if pesticide == 0:
        P = 9


    L = 0;
    if light == 2:
        L = 8
    elif light == 1:
        L = 4
    else:
        L = 1


    O = 0;
    if oxygen<1:
        O = 1
    elif oxygen<1:
        O = 2
    elif oxygen<5:
        O = 5
    else:
        O = 9


    M = 0;
    if moisture_content<12:
        M = 2
    elif moisture_content <13:
        M = 3
    elif moisture_content <15:
        M = 5
    elif moisture_content <16:
        M = 6
    elif moisture_content <18:
        M = 9
    else:
        M = 14

    spoilage = 10 + M + O + T + L + P
    return spoilage




# Function to generate synthetic data for a given crop
def generate_synthetic_data(crop, num_samples=6000):
    data = []

    for _ in range(num_samples):
        # Crop Name
        crop_name = crop

        # Temperature (in Celsius)
        temperature = round(random.uniform(0, 40), 2)

        # Moisture Content (percentage)
        moisture_content = round(random.uniform(2, 20), 2)

        # Ventilation (in cubic meters per minute)
        # ventilation = round(random.uniform(1, 10), 2)


        # Oxygen Level (percentage)
        oxygen = round(random.uniform(0.5, 8), 2)

        # Harvest Time (in days from today)
        # harvest_time = random.randint(1, 30)
        # harvest_date = datetime.now() + timedelta(days=harvest_time)
        # harvest_time_str = harvest_date.strftime('%Y-%m-%d')


        #pesticide is present or not
        pesticide = random.choice([0,1])

        # sunlight Level 
        light = random.choice([0,1,2])
        # Simulated Spoilage Risk (percentage)
        if(crop=='Wheat'):
            spoilage_risk = wheatSpoilage(temperature, oxygen, moisture_content, light, pesticide)
        elif(crop=='Rice'):
            spoilage_risk = riceSpoilage(temperature, oxygen, moisture_content, light, pesticide)
        elif(crop=='Corn'):
            spoilage_risk = cornSpoilage(temperature, oxygen, moisture_content, light, pesticide)

        if(crop=='Wheat'):
            crop_name = 0
        elif(crop=='Rice'):
            crop_name = 1
        elif(crop=='Corn'):
            crop_name = 2
        
        

        data.append({
            'Crop': crop_name,
            'Temperature': temperature,
            'Moisture Content': moisture_content,
            'Pesticide': pesticide,
            'Light' : light,
            # 'Ventilation': ventilation,
            # 'Relative Humidity': relative_humidity,
            'Oxygen': oxygen,
            # 'Harvest Time': harvest_time_str,
            'Spoilage Risk': spoilage_risk
        })

    return data

# Generate synthetic data for wheat, rice, and corn
wheat_data = generate_synthetic_data('Wheat', 4000)
rice_data = generate_synthetic_data('Rice', 6000)
corn_data = generate_synthetic_data('Corn', 4447)

# Combine the data for all crops
all_data = wheat_data + rice_data + corn_data
# all_data = wheat_data

# Shuffle the data to mix crops
random.shuffle(all_data)

# Print a sample of the synthetic data
for sample in all_data[:10]:
    print(sample)


#  Specify the CSV file name
csv_file = 'synthetic_data_all.csv'

# Save data to CSV file
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ['Crop', 'Temperature', 'Moisture Content', 'Pesticide', 'Light', 'Oxygen', 'Spoilage Risk']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for sample in all_data:
        writer.writerow(sample)

print(f'Data has been saved to {csv_file}')