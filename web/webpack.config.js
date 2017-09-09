var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    entry: "./src/app.js",
    output: {
        path: __dirname + "/dist",
        filename: "bundle.js"
    },
    module: {
        loaders: [
            {
                exclude: /(node_modules)/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react']
                }
            },
            {
                test: /\.less$/,
                loader: ExtractTextPlugin.extract({ fallback: 'style-loader', use: 'css-loader!autoprefixer-loader!less-loader'})
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin('style.css', {allChunks: false})
    ],
    watch: true
};
