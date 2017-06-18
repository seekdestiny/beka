def sql_query():
    "*** YOUR CODE HERE ***"
    return 'SELECT stars, count(*) FROM reviews group by stars'

if "mnt/" not in [x.name for x in dbutils.fs.ls("/")] or 'cs61a/' not in [x.name for x in dbutils.fs.ls("/mnt")]: 
  dbutils.fs.mount('s3n://AKIAJUIYIBOAUUTJ3G5A:SU%2FsifB7wuzeWexDJCMTBVxG7MLIbZkk4ZcB+qzd@berkeley-cs61a','/mnt/cs61a/')
reviews_dataset = '/mnt/cs61a/yelp_reviews_dataset_small.json'
reviews = sqlContext.read.json(path=reviews_dataset)
reviews.registerTempTable('reviews')
counts = sqlContext.sql(sql_query())
output = counts.rdd.collectAsMap()
print(output)
