const path = require('path')
//const ExtractTextPlugin = require('extract-text-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
//const UglifyJsWebpackPlugin = require('uglifyjs-webpack-plugin');
const webpack = require('webpack');


module.exports = {
    entry: {
	app: "./src/app.js"
    },
    //devtool: 'inline-source-map',
    devServer: {
	contentBase: './dist',
	//hot: true
    },
    plugins: [
	new CleanWebpackPlugin(['dist']),
	new HtmlWebpackPlugin({template: './views/index.pug', filename: './index.html'}),
	//new UglifyJsWebpackPlugin(),
	new CopyWebpackPlugin([{from: './src/assets', to: 'static'}]),
	new webpack.NamedModulesPlugin(),
	new webpack.HotModuleReplacementPlugin(),
	new MiniCssExtractPlugin({filename: '[name].css', chunkFilename: '[id].css'}),
	//new ExtractTextPlugin('style.css', {allChunks: false})
    ],
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: "bundle.js"
    },
    module: {
	rules: [
	    {
		test: /\.js$/,
		exclude: /(node_modules)/,
		use: {
		    loader: 'babel-loader',
		    options: {
			presets: ['es2015', 'react']
		    }
		}
	    },
            {
                test: /\.less$/,
                use: ['style-loader',
		      MiniCssExtractPlugin.loader,
		      'css-loader',
		      'less-loader'
		]
            },
	    {
		test: /\.pug$/,
		use: {
		    loader: 'pug-loader'
		}
	    }
        ]
    },
    watch: true
};
