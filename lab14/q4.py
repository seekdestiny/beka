import re
import string

### Helper Code 

REGEX = re.compile('[%s]' % re.escape(string.punctuation))

MIN_OCCURENCES = 4000

def avg(iterable):
    total = 0.0
    count = 0
    for val in iterable:
        total += val
        count += 1
    if count > 0:
        return total/count

### Question Code Below

def mapper(review):
    words = set(REGEX.sub(' ', review.text.lower()).split())
    "*** YOUR CODE HERE ***"
    return [(word, review.stars) for word in words] # COPY FROM PREVIOUS QUESTION
  
def reducer(values):
    "*** YOUR CODE HERE ***"
    return avg(values) # COPY FROM PREVIOUS QUESTION

def make_predictor(positivities):
    def predictor(review):
        words = set(REGEX.sub(' ', review.text.lower()).split())
        "*** YOUR CODE HERE ***"
        total = 0.0
        count = 0
        predstar = 0.0
        for word in words:
          if word in positivities:
            total += positivities[word]
            count += 1
        if count > 0:
          predstar = total / count        
        return (review.text, review.stars, predstar)
    return predictor

def filterer(kv_pair):
    key, values = kv_pair
    return len(values) > MIN_OCCURENCES

  
def analyze_positivity(reviews):
    counts = (reviews.flatMap(mapper)
                     .groupByKey()
                     .filter(filterer)
                     .mapValues(reducer))
    return counts.collectAsMap()

def filter_words(word_positivities):
    avg_pos = avg(word_positivities.values())
    filtered_words = {}
    for word in word_positivities.keys():
        if abs(word_positivities[word] - avg_pos) > 0.2*avg_pos:
            filtered_words[word] = word_positivities[word]
    return filtered_words

def predict_ratings(reviews, positivities):
    predicted_ratings = reviews.map(make_predictor(positivities)).filter(
            lambda kv_pair: kv_pair[-1] is not None)
    return predicted_ratings

if "mnt/" not in [x.name for x in dbutils.fs.ls("/")] or 'cs61a/' not in [x.name for x in dbutils.fs.ls("/mnt")]: 
  dbutils.fs.mount('s3n://AKIAJUIYIBOAUUTJ3G5A:SU%2FsifB7wuzeWexDJCMTBVxG7MLIbZkk4ZcB+qzd@berkeley-cs61a','/mnt/cs61a/')
training_dataset = '/mnt/cs61a/yelp_reviews_dataset_large.json'
testing_dataset = '/mnt/cs61a/yelp_reviews_dataset_small.json'
trainingRDD = sqlContext.read.json(training_dataset).rdd
testingRDD = sqlContext.read.json(testing_dataset).rdd
word_positivities = analyze_positivity(trainingRDD)
filtered_positivities = filter_words(word_positivities)


ratings = predict_ratings(testingRDD, filtered_positivities)
mean_percent_difference = lambda x: 2*abs(x[1] - x[2])/(x[1] + x[2])
ratings.sortBy(mean_percent_difference).take(10)
