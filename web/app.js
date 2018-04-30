var http = require('http');
var express = require('express');
var history = require('connect-history-api-fallback');

const app = express();

app.use('/static', express.static(__dirname + '/dist'));

app.set('views', __dirname + '/views');
app.set('view engine', 'pug');

if(process.env.NODE_ENV !== 'production') {
    const webpack = require('webpack');
    const webpackConfig = require('./webpack.config.js');
    const compiler = webpack(webpackConfig);

    app.use(require('webpack-dev-middleware')(compiler, {
	noInfo: true,
	publicPath: webpackConfig.output.publicPath
    }));

    app.use(require('webpack-hot-middleware')(compiler));
}

app.use(history());

app.get('*', function(req, res, next) {
    res.render('index');
    next();
});

const server = new http.Server(app);
const io = require('socket.io')(server);
const port = 5000;

server.listen(port);
console.log(`listening on port ${port}`);

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
