with open('input.txt', 'r') as f:
    lines = f.readlines()

calibration_values = []

for line in lines:
    digit = [i for i in line if i.isdigit()]
    calibration_value = int(f'{digit[0]}{digit[-1]}')
    calibration_values.append(calibration_value)

print(sum(calibration_values))