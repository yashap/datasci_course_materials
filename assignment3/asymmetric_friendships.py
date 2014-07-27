import MapReduce
import sys

# Word Count Example in the Simple Python MapReduce Framework

# Run it like this:
# python asymmetric_friendships.py data/friends.json
# And it will print the final result to stdout

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  mr.emit_intermediate(record[0], record[1])
  mr.emit_intermediate(record[1], record[0])

def reducer(person, friends):
  seen = {}
  for friend in friends:
    if friend not in seen:
      seen[friend] = 1
    else:
      seen[friend] += 1
  for friend in seen:
    if seen[friend] == 1:
      mr.emit((person, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
