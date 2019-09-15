
from flask import Flask, render_template,request,url_for,jsonify
from flask_bootstrap import Bootstrap; 
from textblob import TextBlob,Word;

import random

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello world"

@app.route('/reviews_ml',methods=['POST'])
def reviews():
    gotData = request.json
    course = gotData['course']

    if(course == 'course1'):
        data = { 'reviews':,
            'name':''
        }
    elif (course == 'course2'):
        data = { 'reviews':[,
            'name':''
        }
    else:    
        data = { 'reviews':,
            'name':''
        }
    
    return data



@app.route('/reviews_android',methods=['POST'])
def reviews():
    gotData = request.json
    course = gotData['course']
    if(course == 'course1'):
        data = { 'reviews':,
            'name':''
        }
    elif (course == 'course2'):
        data = { 'reviews':,
            'name':''
        }
    else:    
        data = { 'reviews':,
            'name':''
        }
    

    return data



@app.route('/reviews_web',methods=['POST'])
def reviews():
    gotData = request.json
    course = gotData['course']

    if(course == 'course1'):
        data = { 'reviews':[
            "Yeah! I was fairly new to the world of Web Development, but Colt taught a lot and very well also. Ian and Zarko were also very helpful and saved me a lot of time . Thanks for making such an informative course. Thanks a lot!",
            "Wonderful course! Colt is an awesome teacher! He is very clear and detailed and his examples are spot on. This is actually one of the best of the courses I've taken on Udemy so far and Colt is definitely the best teacher. I like that his assistants answer questions in a timely manner. The only thing I find a little unfortunate about this course is that the JavaScript section only has JavaScript basics, I would have liked it if it was extended to an intermediate level and updated to ES6. But all in all its a great course. Great job Colt!",
            "Even thou English is not my native language, that wasn´t an impediment for me to learn these wonderful skils, ´cause the way the instructor designed the course, and explain it´s topics. I really encorage you to add this course and the skills that offers to your life!",
            "What frustrated me was all of the notes. It seems like a lot of these videos needed to be updated because of changes to languages, libraries, APIs', hell even the terminal(s) changed to VScode. I understand that technology will continue to change and that means you will need to make updates and notes are an inexpensive way of doing that but it just comes off as cheap and lazy. I paid money for this I expect it to run smoothly and not link me all over the place to comments of people who ALSO paid for the course and had to come up wit their own solution to a problem that should have been discussed in one of the videos, All that being said, this course answered a lot of questions I had when I was attempting to build my first JavaScript project earlier this year. Who knew a website required so many moving parts ( libraries, API's etc...) . I cannot stress enough how helpful the JavaScript the hard parts section was in understanding __proto__ property and closures."
            "This course is amazing. just don't give up and go on with it. Colt is an amazing teacher and he will teach you an amazing things as time passes."
            ],
            'name':'the-web-developer-bootcamp'
        }
    elif (course == 'course2'):
        data = { 'reviews':[
                "Bad Course, the instructor is very vague in his instructions during the javascript portion. In addition, he never responded to my question. He is a very bad instructor!",
                "Bad Course, the instructor is very vague in his instructions during the javascript portion. In addition, he never responded to my question. He is a very bad instructor!",
                "The teaching and explanation style is great, the only thing that is average about this course is that it is a based on the little older versions, other than that it is a great course.",
                "There are some codes he never showed in his video when he was teaching how to make a google chrome extension, you just turn out to see them, there are so many complicated code he didn't take time to explain",
                "There are some codes he never showed in his video when he was teaching how to make a google chrome extension, you just turn out to see them, there are so many complicated code he didn't take time to explain"
            ],
            'name':'front-end-web-development'
        }
    else:    
        data = { 'reviews':[
                "Has mostly been a good review up to this point with a few new techniques that are very exciting. But now as I get to the more advanced tutorials, js, PHP, etc learning much more.",
                "I love this course and Brad is a very experienced and easy to follow instruc,tor :) This course teaches all the building blocks of web development. It's highly recommended",
                "This course is well explained like friends discussing over a football match, its so simple that it doused my apprehension about this course.",
                "Very Well Explained as per what a Beginner for the role of Web Designer look out for also on Intermediate learner.",
                "It's good so far, I like the way Brad teaches."
            ],
            'name':'web-developer-course'
        }
    return data


@app.route('/reviews_ds',methods=['POST'])
def reviews():
    gotData = request.json
    course = gotData['course']
    if(course == 'course1'):
        data = { 'reviews':,
            'name':''
        }
    elif (course == 'course2'):
        data = { 'reviews':,
            'name':''
        }
    else:    
        data = { 'reviews':,
            'name':''
        }
    
    return data




#We are getting the result of analysis.
@app.route('/analyze',methods=['POST'])
def analyze():
    reviewData = request.json
    review = reviewData['review']
    blob = TextBlob(review)
    received_text2 = blob
    blob_sentiment_pos,blob_subjectivity = blob.sentiment.polarity,blob.sentiment.subjectivity

    num_tokens = len(list(blob.words))
    adjective = list()
    for word,tag in blob.tags:
        if tag == 'JJ':
            adjective.append(word.lemmatize())
            len_of_words = len(adjective)
            rand_words = random.sample(adjective,len(adjective))
            final_word = list()
            for item in rand_words:
                word = Word(item).pluralize()
                final_word.append(word)
                adjectiveSummary = final_word

    data = {
        "nounSummary":adjectiveSummary,
        "positivity_analysis":blob_sentiment_pos,
        "subjectivity":blob_subjectivity,
        "review":review
    }
    return data


if __name__ == '__main__':
    app.run(debug=True)