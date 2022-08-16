def generate(upto):
  num_list = list(range(1, upto + 1))
  output_list = []

  for i in num_list:
    if i % 15 == 0:
      output_list.append("fizzbuzz")
    elif i % 3 == 0:
      output_list.append("fizz")
    elif i % 5 == 0:
      output_list.append("buzz")
    else:
      output_list.append(str(i))

  return ", ".join(output_list)
