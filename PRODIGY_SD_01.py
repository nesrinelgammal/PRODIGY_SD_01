# conversion function
def convert_temperature(value, input_scale, output_scale):
    # convert the value to a float
    value = float(value)
    # convert the input scale to uppercase
    input_scale = input_scale.upper()
    # convert the output scale to uppercase
    output_scale = output_scale.upper()
    # check if the input and output scales are valid
    if input_scale not in ['C', 'F', 'K']:
        return 'Invalid input scale'
    if output_scale not in ['C', 'F', 'K']:
        return 'Invalid output scale'
    # convert the temperature to the desired scale
    if input_scale == output_scale:
        return value
    elif input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67

# prompt the user for the input temperature value
value = input('Enter the temperature value: ')
# check if the value is a number
if not value.isdigit():
    print('Invalid temperature value')
else:
    # prompt the user for the input temperature scale
    input_scale = input('Enter the input temperature scale (C, F, or K): ')
    # prompt the user for the output temperature scale
    output_scale = input('Enter the output temperature scale (C, F, or K): ')
    # call the conversion function and print the result
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale.upper()} = {result:.2f} {output_scale.upper()}')
