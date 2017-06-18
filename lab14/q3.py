#HELPER CODE# 
import re
import string
REGEX = re.compile('[%s]' % re.escape(string.punctuation))

MIN_OCCURENCES = 1000

def avg(iterable):
    total = 0.0
    count = 0
    for val in iterable:
        total += val
        count += 1
    if count > 0:
        return total/count


#QUESTION CODE#
def mapper(review):
    words = set(REGEX.sub(' ', review.text.lower()).split())
    "*** YOUR CODE HERE ***"
    return [(word, review.stars) for word in words] # REPLACE THIS LINE
  
def reducer(values):
    "*** YOUR CODE HERE ***"
    return avg(values) # REPLACE THIS LINE

def filterer(kv_pair):
  key, values = kv_pair
  return len(values) > MIN_OCCURENCES

if "mnt/" not in [x.name for x in dbutils.fs.ls("/")] or 'cs61a/' not in [x.name for x in dbutils.fs.ls("/mnt")]: 
  dbutils.fs.mount('s3n://AKIAJUIYIBOAUUTJ3G5A:SU%2FsifB7wuzeWexDJCMTBVxG7MLIbZkk4ZcB+qzd@berkeley-cs61a','/mnt/cs61a/')
reviews_dataset = '/mnt/cs61a/yelp_reviews_dataset_small.json'
reviews = sqlContext.read.json(path=reviews_dataset).rdd
counts = (reviews.flatMap(mapper)
                  .groupByKey()
                  .filter(filterer)
                  .mapValues(reducer)
                  .sortBy(lambda x: x[1]))

worst_words = counts.take(20)
best_words = counts.top(20,lambda x: x[1])  
