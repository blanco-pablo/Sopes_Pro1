const mongoose = require('mongoose');

const ur = 'mongodb://root:rootpassword@localhost:27017/mydatabase';

mongoose.connect(ur,{
    useNewUrlParser:true,
    useCreateIndex:true
});

const connection = mongoose.connection;

connection.once('open',()=>{
    console.log('DB');
});