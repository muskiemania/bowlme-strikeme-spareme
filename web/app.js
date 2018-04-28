var express = require('express')

var app = express();

app.use('/static', express.static(__dirname + '/dist'));

app.set('views', __dirname + '/views');
app.set('view engine', 'pug');

app.get('*', function(req, res) {
    res.render('index');
});

app.listen(5000, function() {
    console.log('listening on 5000...')
});

const io = require('socket.io')(app);

io.on('connection', (socket) => {
    console.log('user has connected');

    socket.on('disconnect', () => {
	console.log('user has disconnected');
    });

    socket.on('join-game', (data) => {
	socket.join(data);
    });

    socket.on('leave-game', (data) => {
	socket.leave(data);
    });

    socket.on('table-activity', (data) => {
	socket.broadcast.to(data).emit('table-activity', data);
    });
	      
});
