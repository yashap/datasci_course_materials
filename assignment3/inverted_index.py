import MapReduce
import sys

# Word Count Example in the Simple Python MapReduce Framework

# Run it like this:
# python inverted_index.py data/books.json
# And it will print the final result to stdout

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  doc_name = record[0]
  text = record[1]
  words = text.split()
  for word in words:
    mr.emit_intermediate(word, doc_name)

def reducer(word, list_of_docs):
  mr.emit((word, dedupe(list_of_docs)))

def dedupe(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
