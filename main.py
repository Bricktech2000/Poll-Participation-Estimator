print('This program estimates the number of people who participate on a poll based on the changing percentages over time.')
print('It can be used on Instagram polls, for instance. The estimated number of people who participate on the poll will be')
print('more accurate as more values are inputted.')
print('Assumptions:')
print('- Poll values are inputted chronologically.')
print('- Participants may not change their vote.')
print('- Poll values are rounded to the nearest whole number.')
print('')


def float_input(query):
  while True:
    number = input(query)
    if number == '':
      print('Number inputted is empty. Exiting.')
      return None
    try:
      return float(number)
    except ValueError:
      print('Please enter a valid number.')

def run():
  denom = float_input('Denominator (100 for percentages): ')
  if denom is None: return

  denominator_test = 0
  numerator_test = 0
  print('')

  while True:
    value = float_input(f'Current value (out of {denom}): ')
    if value is None: return

    while True:
      denominator_test += 1
      num = round(value / denom * denominator_test)

      if round(num / denominator_test * denom) == value and num >= numerator_test:
        numerator_test = num 
        print(f'Estimated poll participation count: {denominator_test}')

        break

run()
