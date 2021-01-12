"""Restaurant rating lister."""
def restaurant_ratings(text_file):
    """Returns alphabetized restaurant ratings"""
# read rating from file
    restaurants = open(text_file)
    new_rest = input('give me a restaurant name')
    new_rating = input('what is your rating?')
    alpha_rests = {new_rest:new_rating}

# loop over each line
    for line in restaurants:
        line = line.rstrip().split(':')
        key = line[0]
        value = line[1]
        alpha_rests[key] = value
        print(alpha_rests)
        final_list = sorted(alpha_rests)
# loop through final list then get values by key from alpha_rests
    for rest in final_list:
        print(f'{rest} is rated at {alpha_rests[rest]}.') 
              
restaurant_ratings('scores.txt')
# store in dictionary
# return rating in alphabetical order (fstring)
# 

# put your code here
