def mapper(review):
    "*** YOUR CODE HERE ***"
    return [(review.stars, 1)]# REPLACE THIS LINE

def reducer(vals):
    "*** YOUR CODE HERE ***"
    return sum(vals) # REPLACE THIS LINE

if "mnt/" not in [x.name for x in dbutils.fs.ls("/")] or 'cs61a/' not in [x.name for x in dbutils.fs.ls("/mnt")]: 
  dbutils.fs.mount('s3n://AKIAJUIYIBOAUUTJ3G5A:SU%2FsifB7wuzeWexDJCMTBVxG7MLIbZkk4ZcB+qzd@berkeley-cs61a','/mnt/cs61a/')
reviews_dataset = '/mnt/cs61a/yelp_reviews_dataset_small.json'
reviews = sqlContext.read.json(path=reviews_dataset).rdd
counts = reviews.flatMap(mapper).groupByKey().mapValues(reducer)
output = counts.collectAsMap()
print(output)
