var request = require('request');

var review_arr = []
var positivity_arr = []
var keywords_arr = []

request.post(
    'http://c3c413be.ngrok.io/ds',
    { json: { course: 'course1' } },
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            // console.log(body);
            data = response.body
            reviews = data['reviews']
            for(var i=0;i<reviews.length;i++){
                                
                request.post(
                    'http://c3c413be.ngrok.io/analyze',
                    { json: { review:`${reviews[i]}` } },
                    function (error, response, body) {
                        if (!error && response.statusCode == 200) {
                            ans = response.body
                            // console.log(response.body)
                            review = ans['review']
                            positivity_analysis = ans['positivity_analysis']
                            keywords = ans['nounSummary']
                            if(positivity_analysis > 0){
                                positivity_analysis = "Yes"
                            }
                            else{
                                positivity_analysis = "No"
                            }
                           positivity_arr.push(positivity_analysis)
                           review_arr.push(review)
                           keywords_arr.push(keywords);
                        }
                    }
                );
            }
        }
        
    }
);

console.log(positivity_arr)