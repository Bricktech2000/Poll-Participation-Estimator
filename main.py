print('This program estimates the number of people who participate on a poll based on the percentages changing over time.')
print('It can be used on Instagram polls, for instance. The estimated number of people who participate on the poll will be')
print('more accurate as more values are inputted. The actual number of people participating is guaranteed to be greater or')
print('equal to the estimated count, and is likely an integer multiple of it. However, due to the limited amount of')
print('information available, this cannot be guaranteed.')
print('Assumptions:')
print('- Poll values are inputted chronologically.')
print('- Participants may not change their vote.')
print('- Poll values are rounded to the nearest whole number.')
print('')


def float_input(query, multiple=False):
  while True:
    number = input(query)

    if number == '':
      print('Number inputted is empty. Exiting.')
      return None

    try:
      if not multiple: return float(number)
      return [float(x) for x in number.split()]
    except ValueError:
      print('Please enter a valid number.')

def main():
  denom = float_input('Denominator (100 for percentages): ')
  if denom is None: return

  participant_count = 0
  vote_counts = None
  print('')

  while True:
    values = float_input(f'Current values (out of {denom}, separated by whitespace): ', multiple=True)
    if values is None: return
    if vote_counts is None: vote_counts = [0] * len(values)
    if len(values) != len(vote_counts):
      print('Please enter the same number of values as in the previous input.')
      continue

    # loop through possible participant counts
    while True:
      participant_count += 1
      next_vote_counts = []

      # loop through the values inputted to find the next participant count to fit them all
      for (current_value, current_vote_count) in zip(values, vote_counts):
        # calculate the required vote count based on the denominator and participant count
        vote_count = round(current_value / denom * participant_count)

        # check whether the required vote count/participant count would yield the right percentage
        # and make sure the new vote count is greater than the previous vote count
        if round(vote_count / participant_count * denom) == current_value and vote_count >= current_vote_count:
          next_vote_counts.append(vote_count)

      # if all vote counts can be represented using the current participant count, set this as
      # the new estimation and stop checking for other participant counts
      if len(next_vote_counts) == len(values):
        vote_counts = next_vote_counts
        break

    print(f'Estimated poll participation count: {participant_count}')

if __name__ == '__main__':
  main()
