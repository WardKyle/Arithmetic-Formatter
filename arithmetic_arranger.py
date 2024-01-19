def arithmetic_arranger(problems, solutions = False):
if len(problems) > 5:
  return "Error: Too many problems."
top_row, bottom_row, len_arr, solved = [],[],[],[]
arranged_problems = []
for el in problems:
  top,operator,bottom = el.split(" ")
  if operator != "+" and operator != "-":
    return "Error: Operator must be '+' or '-'."
  if top.isdigit() is False or bottom.isdigit() is False:
    return "Error: Numbers must only contain digits."
  leng = len(top) + 2 if len(top) >= len(bottom) else len(bottom) + 2
  if leng > 6:
    return "Error: Numbers cannot be more than four digits."
  this_solution = str(int(top)+int(bottom)) if operator == "+" else str(int(top)-int(bottom))
  while len(this_solution) < leng:
    this_solution = f' {this_solution}'
  solved.append(this_solution)
  while len(top) < leng:
    top = f' {top}'
  while len(bottom) < leng -1:
    bottom = f' {bottom}'
  bottom = f'{operator}{bottom}'
  top_row.append(top)
  bottom_row.append(bottom)
  len_arr.append('-'*leng)
for i in range(len(top_row)):
  if i == 0:
    arranged_problems = f'{top_row[i]}'
  elif i == len(top_row) - 1:
    arranged_problems += f'    {top_row[i]}\n'
  else:
    arranged_problems += f'    {top_row[i]}'
for i in range(len(top_row)):
  if i == 0:
    arranged_problems += f'{bottom_row[i]}'
  elif i == len(top_row) - 1:
    arranged_problems += f'    {bottom_row[i]}\n'
  else:
    arranged_problems += f'    {bottom_row[i]}'
for i in range(len(top_row)):
    if i == 0:
      arranged_problems += f'{len_arr[i]}'
    elif i == len(top_row) - 1:
      arranged_problems += f'    {len_arr[i]}'
      if solutions:
        arranged_problems += '\n'
    else:
      arranged_problems += f'    {len_arr[i]}'
if solutions:
  for i in range(len(top_row)):
    if i == 0:
      arranged_problems += f'{solved[i]}'
    elif i == len(top_row) - 1:
      arranged_problems += f'    {solved[i]}'
    else:
      arranged_problems += f'    {solved[i]}'
return arranged_problems