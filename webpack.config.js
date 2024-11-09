const path = require('path');

     module.exports = {
       entry: './frontend/index.js',
       output: {
         filename: '[name]-[hash].js',
         path: path.resolve(__dirname, 'static/bundles/'),
       },
       module: {
         rules: [
           {
             test: /\.js$/,
             exclude: /node_modules/,
             use: {
               loader: 'babel-loader',
               options: {
                 presets: ['@babel/preset-env', '@babel/preset-react'],
               },
             },
           },
         ],
       },
     };