from aocd import get_data
import regex

lines = get_data(day=1, year=2023).splitlines()

calibration_values = []

for line in lines:
    digit = [i for i in line if i.isdigit()]
    calibration_value = int(f'{digit[0]}{digit[-1]}')
    calibration_values.append(calibration_value)

print(f'First Half: {sum(calibration_values)}')

# second half

calibration_values = []

str_to_digit = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9",
}

for line in lines:
    nums = regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    digit = [str_to_digit.get(item, item) for item in nums]
    if digit:
        calibration_value = int(f'{digit[0]}{digit[-1]}')
        calibration_values.append(calibration_value)
    
print(f'Second Half: {sum(calibration_values)}')