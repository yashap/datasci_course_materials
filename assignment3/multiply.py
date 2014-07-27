import MapReduce
import sys

# Word Count Example in the Simple Python MapReduce Framework

# Run it like this:
# python multiply.py data/matrix.json
# And it will print the final result to stdout

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


# if x(row, column) is the product, i.e. x(3, 2)
# we want all A with the same row as x, and all b with the same column as x
# i.e. A(3, all), B(all, 2)
# Then the variant parts match up
# i.e. A(3, 1) * B(1, 2) + A(3, 2) * B(2, 2) = x(3, 2)
# I need to end up with x values in the format (row, column, value)
# A has 4 rows, 4 columns
# B has 4 rows, 4 columns
# Every row of A actually has to match up with all values of B, so I should group by row A, column B?
# 
# The "answer" gets row from A, column from B

def mapper(record):
  matrix = record[0]
  if matrix == "a":
    mr.emit_intermediate(record[1], record)
  if matrix == "b":
    for row in range(5):
      mr.emit_intermediate(row, record)

def reducer(solution_row, relevant_records):
  a = {}
  b = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}
  for record in relevant_records:
    matrix, row, column, value = record
    if matrix == "a":
      a[column] = value
    else:
      b[column][row] = value
  for solution_column in range(5):
    b_col = b[solution_column]
    solution_value = 0
    for y in range(5):
      a_val = a.get(y) if a.get(y) else 0
      b_val = b_col.get(y) if b_col.get(y) else 0
      solution_value += a_val * b_val
    mr.emit((solution_row, solution_column, solution_value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
