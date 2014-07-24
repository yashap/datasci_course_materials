import MapReduce
import sys

# Word Count Example in the Simple Python MapReduce Framework

# Run it like this:
# python friend_count.py data/friends.json
# And it will print the final result to stdout

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  person = record[0]
  mr.emit_intermediate(person, 1)

def reducer(person, friends):
  mr.emit((person, sum(friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
