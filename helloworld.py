import math

def median(input):
    size = len(input)
    if size % 2 == 0:
        value1 = size // 2 - 1
        value2 = size // 2
        return (input[value1] + input[value2]) / 2
    else:
        _value = size // 2
        return input[_value]
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)
