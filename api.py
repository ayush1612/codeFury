
from flask import Flask, render_template,request,url_for,jsonify
from flask_bootstrap import Bootstrap; 
from textblob import TextBlob,Word;

import random

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello world"

@app.route('/ml',methods=['POST'])
def reviewsMl():
    gotData = request.json
    course = gotData['course']

    if(course == 'course1'):
        data = { 'reviews':['Great start to Machine Learning! I would have liked it more if it had explained more Math behind the ML models.', 'I personally feel that instructors know what you are going to face in real life what challenges you will face while working on any machine learning project , though udemy asked me to rate course very early and promoted multiple times in middle but i waited as i was enjoying course a lot and wanted to learn first and didnt want to leave a halfhearted rating i personally feeling reading references and links are very helpful , and this is a top-notch course to start .', 'Amazing! This course helped me to implement a personal project, but i have two suggestions:I would like to see the same algorithms implemented with more complex data.2° "How to get the dataset" shouldnt show up every session.', 'Could be better, content not that good', 'Not satisfied with the course content'],
            'name':'Machine Learning A-Z™: Hands-On Python & R In Data Science'
        }
    elif (course == 'course2'):
        data = { 'reviews':[ 'Very good course for beginners but should spend enough time on other topics to get familiar with all libraries and models. This course also needs to be updated with latest versions , libraries and models', 'Excellent course that teaches the fundamental skills with Python and Data Science! Recommend for people trying to learn python without much prior experience. The program is complete with open ended projects that allow you to develop in the future.', 'Jose knocks it out of the park again! My only criticism is There really needs to be more fundamental overview for math and data science to better grasp this stuff.', 'Not that good', 'It doesnt focus on beginners, its high level'],
            'name':'Python for Data Science and Machine Learning Bootcamp'
        }
    elif(course == 'course3'):    
        data = { 'reviews':[ 'Very good practical knowledge and intuitional explanations. It would be perfect to include some theoritical explanations too.', 'Good one. Actually covered almost all theorem with theory and its practical examples.Good to start especially for someone who dont know anything about ML.', 'Poor buffering speed', 'Unsatisfactory', 'Not much projects done'],
            'name':'Python for Data Science and Machine Learning Bootcamp'
        }
    
    return jsonify(data)



@app.route('/android',methods=['POST'])
def reviewsAnd():
    gotData = request.json
    course = gotData['course']
    if(course == 'course1'):
        data = { 'reviews':
            ['overall course is very good .All concept are taught properly.','Great start for Android, however, the code is a it out of date. Overall is good. Thanks!','Rob is an amazing teacher.','Explanation of the code was really best to me but It is not complete course, as there are many things left','Its better if the instructor add some video on android pie so that student can use this knowledge the latest version of android studio','This course is right for me.','Very very repetitive and a lot of java bad practices','The course was good for an introductory level, but not complete as it said in its title as the "complete android developer" course',"Not a good course","The course is good as whole."],
            'name':'theCompleteAndroidNDeveloperCourse'
        }
    elif (course == 'course2'):
        data = { 'reviews':['This course works well','Its awesome','Not a great course','works bad','getting bored lately'],
            'name':'androidJavaMasterClass'
        }
    elif(course == 'course3'):    
        data = { 'reviews':['Unfortunately I and a few others have gotten a point in this course where a big issue arises in one of the apps and the instructor no longer responds to questions to aid with this issue','The updated/ newer versions of android studio or other services should be used in the tutorials and possible errors and their solutions should be mentioned in the same.','Overall good course. I would prefer if it was going deeper into Android Studio and Development,but good insight was provided into marketing and launching the app and all the tricks.','I enjoyed the experience of learning both android programming and thinking programmatically from you guys','This course is amazingly immersive and quite all-inclusive from end-to-end to develop an app!'],
            'name':'androidOnJava'
        }
    

    return jsonify(data)



@app.route('/web',methods=['POST'])
def reviewsWeb():
    gotData = request.json
    course = gotData['course']

    if(course == 'course1'):
        data = { 'reviews':[
            "Yeah! I was fairly new to the world of Web Development, but Colt taught a lot and very well also. Ian and Zarko were also very helpful and saved me a lot of time",
              "Wonderful course! Colt is an awesome teacher! He is very clear and detailed and his examples are spot on. This is actually one of the best of the courses I've taken on Udemy so far and Colt is definitely the best teacher. I like that his assistants answer questions in a timely manner. The only thing I find a little unfortunate about this course is that the JavaScript section only has JavaScript basics, I would have liked it if it was extended to an intermediate level and updated to ES6. But all in all its a great course. Great job Colt!",
            "Even thou English is not my native language, that wasn´t an impediment for me to learn these wonderful skils, ´cause the way the instructor designed the course, and explain it´s topics. I really encorage you to add this course and the skills that offers to your life!",
            "This course is amazing. just don't give up and go on with it. Colt is an amazing teacher and he will teach you an amazing things as time passes."
            "okay course Liked some parts, did not liked other"
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
    elif(course == 'course3'):    
        data = { 'reviews':[
                "Has mostly been a good review up to this point with a few new techniques that are very exciting. But now as I get to the more advanced tutorials, js, PHP, etc learning much more.",
                "I love this course and Brad is a very experienced and easy to follow instruc,tor :) This course teaches all the building blocks of web development. It's highly recommended",
                "This course is well explained like friends discussing over a football match, its so simple that it doused my apprehension about this course.",
                "Very Well Explained as per what a Beginner for the role of Web Designer look out for also on Intermediate learner.",
                "It's good so far, I like the way Brad teaches."
            ],
            'name':'web-developer-course'
        }
    return jsonify(data)


@app.route('/ds',methods=['POST'])
def reviewsDs():
    gotData = request.json
    course = gotData['course']
    if(course == 'course1'):
        data = { 'reviews':['Very good course for beginners but should spend enough time on other topics to get familiar with all libraries and models. This course also needs to be updated with latest versions , libraries and models','The course was really great and provided good insights to python libraries. Few topics were covered in haste just for the sake of completing the course.','Not bad for complete entry level. Not a lot of theory and background math. But good for learning all the python tools' 'not satisfied', 'Just completed the course and I can confidently say that it is a great introduction to Data Science. Kirill puts a lot of order into chaos, while still leaving the students open to find individual and independent solutions. Daniel is also a great Q&A moderator. Great team, great course!'],
            'name':'Complete DataScience with Python and Tensorflow'
        }
    elif (course == 'course2'):
        data = { 'reviews':['This is an amazing course, Kirill did a nice job here, especially the data preparation part, its very comprehensive.','The Q&A pages in the course are littered with people complaining that if you are using a Mac you are unable to install the required programs. This means you are not able to complete the third section of the course. Despite these complaints being months/years old, the creators of this course have still not updated the Requirements page. I find it incredibly misleading that the creators of the course are unwilling to make clear the hardware requirements of their course.','Did not specify this course is not compatible with Mac.', 'Not very practical.','NO Video, only audio, I have old XP computer, all other Udemy courses work fine.','poor buffering speed'],
            'name':'Complete DataScience with Python and Tensorflow'
        }
    elif(course == 'course3'):    
        data = { 'reviews':['Too much unnecessary talks, needs lot of editing to remove it. Probably 21 hours content be reduced to less than 10 hours. Hard to focus when you constantly have to filter out more than half of the things someone is saying','Expected more information like some lecture about hadoop, sparks etc. For getting data science required lots of knowledge about statistics as well as algorithms. Lot of things required to be added in this course so that anyone can apply for data science jobs. Thanks','This is the best course l have ever done, however l need the notes. where can l download them?','Good course, unfortunately they forgot to mention that the programs that about 1/4 of the course rely on are not available for mac.','In a number of occasions small things was explained repeated in a circle before moving on to the next point.'],
            'name':'Data science master course'
        }
    
    return jsonify(data)


androidJavaMasterClass= ['This course works well','Its awesome','Not a great course','works bad','getting bored lately']
androidOnJava = ['Unfortunately I and a few others have gotten a point in this course where a big issue arises in one of the apps and the instructor no longer responds to questions to aid with this issue','The updated/ newer versions of android studio or other services should be used in the tutorials and possible errors and their solutions should be mentioned in the same.','Overall good course. I would prefer if it was going deeper into Android Studio and Development,but good insight was provided into marketing and launching the app and all the tricks.','I enjoyed the experience of learning both android programming and thinking programmatically from you guys','This course is amazingly immersive and quite all-inclusive from end-to-end to develop an app!'],



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