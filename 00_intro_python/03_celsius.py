
ask_temperature = '*Enter temperature in Fahrenheit:*'

answer_temperature = input(ask_temperature)

degree_celsius = (float(answer_temperature) - 32) * 5.0/9.0

print (f"""Temperature:\033[1;3m{answer_temperature}F = {degree_celsius}C""")