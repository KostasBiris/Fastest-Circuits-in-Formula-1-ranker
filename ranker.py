import csv

# Read in the cleaned data
with open('cleaned_data.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Create a dictionary to store the top speed and average speed for each circuit
circuits = {}
for row in data:
    circuit_name = row['circuit name']
    fastest_lap_speed = row['fastest lap speed']
    latitude = row['latitude']
    longitude = row['longitude']
    if r'\N' in fastest_lap_speed:
        # Skip rows with missing data
        continue
    fastest_lap_speed = float(fastest_lap_speed)
    if circuit_name not in circuits:
        circuits[circuit_name] = {'top_speed': fastest_lap_speed, 'num_laps': 1, 'total_speed': fastest_lap_speed}
    else:
        circuits[circuit_name]['top_speed'] = round(max(circuits[circuit_name]['top_speed'], fastest_lap_speed),2)
        circuits[circuit_name]['num_laps'] += 1
        circuits[circuit_name]['total_speed'] += fastest_lap_speed

    circuits[circuit_name]['latitude'] = latitude
    circuits[circuit_name]['longitude'] = longitude


# Calculate the average speed for each circuit
for circuit_name in circuits:
    circuits[circuit_name]['average_speed'] = round(circuits[circuit_name]['total_speed'] / circuits[circuit_name]['num_laps'],2)

# Sort the circuits by their top speed in descending order
circuits_sorted = sorted(circuits.items(), key=lambda x: x[1]['top_speed'], reverse=True)

# Write the results to a new csv file
with open('fastestCircuits.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['rank', 'circuit name', 'latitude', 'longitude', 'top speed', 'average speed'])
    for i, (circuit_name, circuit_data) in enumerate(circuits_sorted):
        latitude = circuit_data['latitude']
        longitude = circuit_data['longitude']
        top_speed = circuit_data['top_speed']
        average_speed = circuit_data['average_speed']
        writer.writerow([i+1, circuit_name, latitude, longitude, top_speed, average_speed])