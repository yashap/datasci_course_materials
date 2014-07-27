import MapReduce
import sys

# Word Count Example in the Simple Python MapReduce Framework

# Run it like this:
# python unique_trims.py data/dna.json
# And it will print the final result to stdout

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  trimmed = record[1][:-10]
  mr.emit_intermediate(trimmed, 1)

def reducer(key, value):
  mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
