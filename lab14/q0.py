import sys
from pyspark import sqlContext
from pyspark import SparkContext

if __name__ == "__main__":
    reviews_dataset = './reviews.json'
    reviews = sqlContext.read.json(path=reviews_dataset).rdd
    counts = reviews.flatMap(mapper).groupByKey().mapValues(reducer)
    counts.coalesce(1).top(10, key=lambda x: x[1])

def mapper(review):
    return [(review.business_id, 1)]

def reducer(vals):
    return sum(vals)
