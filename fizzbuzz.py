def generate(upto):
  num_list = list(range(1, upto + 1))
  output_list = []

  for i in num_list:
    if i % 3 == 0:
      output_list.append("fizz")
    else:
      output_list.append(str(i))

  return ", ".join(output_list)