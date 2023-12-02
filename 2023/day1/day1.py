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

total = 0

word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

total = 0

for line in lines:
    nums = regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    digits = [word_to_digit.get(num, num) for num in nums]
    if digits:
        calibration_value = int(digits[0] + digits[-1])
        total += calibration_value

print(f'Second Half 1: {total}')

total = 0

for line in lines: # getting the first and last digit then converting
    nums = regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    first_digit = word_to_digit.get(nums[0], nums[0])
    last_digit = word_to_digit.get(nums[-1], nums[-1])
    calibration_value = int(first_digit + last_digit)
    total += calibration_value

print(f'Second Half 2: {total}')