import MapReduce
import sys

# Word Count Example in the Simple Python MapReduce Framework

# Run it like this:
# python join.py data/records.json
# And it will print the final result to stdout

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  mr.emit_intermediate(record[1], record)

def reducer(id, records):
  for record in records:
    if record[0] == "order":
      order = record
  for record in records:
    if record[0] == "line_item":
      mr.emit((order + record))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
