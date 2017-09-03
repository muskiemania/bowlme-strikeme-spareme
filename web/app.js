var express = require('express')

var app = express();

app.use('/static', express.static(__dirname + '/public'));

app.set('views', __dirname + '/views');
app.set('view engine', 'pug');

app.get('*', function(req, res) {
    res.render('index');
});

app.listen(5000, function() {
    console.log('listening on 5000...')
});
