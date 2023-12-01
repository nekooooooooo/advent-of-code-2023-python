from aocd import get_data

lines = get_data(day=1, year=2023).splitlines()

calibration_values = []

for line in lines:
    digit = [i for i in line if i.isdigit()]
    calibration_value = int(f'{digit[0]}{digit[-1]}')
    calibration_values.append(calibration_value)

print(sum(calibration_values))