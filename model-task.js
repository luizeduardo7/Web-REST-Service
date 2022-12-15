const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const taskSchema = new Schema({
    id: {type: Number, required: true},
    descricao: {type: String, required: true},
    prazo: {type: Date, required: true},
    completa: {type: Boolean, required: true}
});

module.exports = mongoose.model("Task", taskSchema);