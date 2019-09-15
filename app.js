var bodyParser    = require('body-parser'),
express           = require('express'),
app               = express();

app.set("view engine","ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended:true}))
app.get("/",function(req,res){
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