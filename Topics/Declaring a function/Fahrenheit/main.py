def fahrenheit_to_celsius(fahrenheit):
    step_1 = 32
    step_2 = 5 / 9
    celsius = (fahrenheit - step_1) * (step_2)
    return '%.3f' % celsius
