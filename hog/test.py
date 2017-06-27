from hog import *
def fail_15_20(score, opponent_score):
    if score == 15 and opponent_score == 20:
        return 100
    return 5

strategy = fail_15_20
score = 0
opponent_score = 0
name = strategy.__name__
name = name.split('_')
if name[0] == 'fail':
    score = int(name[1])
    opponent_score = int(name[2])

print(score)
print(opponent_score)

print(strategy(score, opponent_score))

#check_strategy(fail_15_20) == None
