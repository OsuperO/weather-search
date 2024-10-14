const paths = require('./config/paths');
const path = require('path');
module.exports = {
    // 入口文件
    entry: {

    },
    moduleFileExtensions: ['web.mjs', 'mjs', 'web.js', 'js', 'web.ts', 'ts', 'web.tsx', 'tsx', 'json', 'web.jsx', 'jsx'],
    alias: {
        "@": path.join(__dirname, "src")
    },
    // 输出html文件
    pages: [

    ]


}