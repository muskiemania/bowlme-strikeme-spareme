const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const GitRevisionWebpackPlugin = require('git-revision-webpack-plugin');
const webpack = require('webpack');

require('dotenv').config();

//const revisionPlugin = new GitRevisionWebpackPlugin();

const plugins = [];
plugins.push(new CleanWebpackPlugin(['dist']));
plugins.push(new GitRevisionWebpackPlugin({versionCommand: 'describe --long'}));
plugins.push(new HtmlWebpackPlugin({template: './views/index.pug', filename: './index.html'}));
plugins.push(new CopyWebpackPlugin([{from: './src/assets', to: 'static'}]));
plugins.push(new webpack.NamedModulesPlugin());
plugins.push(new MiniCssExtractPlugin({filename: '[name].css', chunkFilename: '[id].css'}));
plugins.push(new webpack.DefinePlugin({
    'process.env.WEB_PORT': JSON.stringify(`${process.env.WEB_PORT}`),
    'process.env.API_PATH': JSON.stringify(`${process.env.API_PATH}`),
    'process.env.WEB_PATH': JSON.stringify(`${process.env.WEB_PATH}`)
}));

const production = (process.env.NODE_ENV === 'production');

if(!production) {
    plugins.push(
	new webpack.optimize.OccurrenceOrderPlugin(),
	new webpack.HotModuleReplacementPlugin(),
    );
}

module.exports = {
    mode: process.env.NODE_ENV || 'development',
    entry: [
	"webpack-hot-middleware/client",
	"./src/app.js"
    ],
    plugins,
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle_[git-revision-version].js',
	publicPath: '/'
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
    watch: !production
};
