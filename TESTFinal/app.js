var bodyParser    = require('body-parser'),
express           = require('express'),
app               = express();
// const { URLSearchParams } = require('url');
var request = require('request');


// const body = { "course": "course1" };

// var fetch = require('node-fetch');

app.set("view engine","ejs");
app.use(express.static("public"));

// fetch('https://github.com/')
//     .then(res => res.text())
//     .then(body => console.log(body));

app.use(bodyParser.urlencoded({extended:true}))
app.get("/",function(req,res){
    // fetch('http://240e2138.ngrok.io',{ method: 'GET', body: '' })
    // fetch('http://240e2138.ngrok.io/ml', {
    //     method: 'get',
    //     body:    body,
    //     headers: { 'Content-Type': 'application/json' },
    // })
    // .then(res => res.text())
    // .then(data => console.log(data));
    // res.render("index");
    // })

    // request.get(url, (error, response, body) => {
    //     let json = JSON.parse(body);
    //     console.log(body);
    //   });
    request.post(
        'http://240e2138.ngrok.io/ds',
        { json: { course: 'course1' } },
        function (error, response, body) {
            if (!error && response.statusCode == 200) {
                // console.log(body);
                data  = response.body
                reviews = data['reviews']
                for(var i=0;i<reviews.length;i++){
                    request.post(
                        'http://240e2138.ngrok.io/analyze',
                        { json: { review:`${reviews[i]}`} },
                        function (error, response, body) {
                            if (!error && response.statusCode == 200) {
                                console.log(response.body)
                            }
                        }
                    );
                }
            }
        }
    );
    
      res.render("index");
    })

app.get("/android",function(req,res){
    res.render("android");
    })
    
app.get("/ml",function(req,res){
    res.render("ml");
    })

   
app.get("/web",function(req,res){
    res.render("web");
    })
    
app.listen(5555,function(){
    console.log("Ready");
})