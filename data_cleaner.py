import csv

# Read circuits table into a dictionary
circuits = {}
with open('circuits.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        circuits[row['circuitId']] = {'name': row['name'], 'lat': row['lat'], 'lng': row['lng']}

# Read races table into a dictionary to get circuitId for each race
races = {}
with open('races.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        races[row['raceId']] = {'circuitId': row['circuitId']}

# Write cleaned_data.csv
with open('cleaned_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['circuit name', 'latitude', 'longitude', 'fastest lap speed'])
    with open('results.csv', 'r') as results_file:
        results_reader = csv.DictReader(results_file)
        for row in results_reader:
            circuit_id = races.get(row['raceId'], {}).get('circuitId', None)
            if circuit_id:
                circuit_info = circuits.get(circuit_id, None)
                if circuit_info:
                    circuit_name = circuit_info['name']
                    circuit_lat = circuit_info['lat']
                    circuit_lng = circuit_info['lng']
                    fastest_lap_speed = row['fastestLapSpeed']

                    if r'\N' not in fastest_lap_speed:
                        writer.writerow([circuit_name, circuit_lat, circuit_lng, fastest_lap_speed])
