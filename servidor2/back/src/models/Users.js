const { Schema, model } = require('mongoose');

const usuario = new Schema({
    Nombre: String,
    Oracion: String
});


module.exports = model('data',usuario);