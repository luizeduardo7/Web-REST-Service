const express = require("express");
const mongoose = require("mongoose");

const control_task = require("./control-task");

mongoose.connect("mongodb://localhost/tasks", {useNewUrlParser: true, useUnifiedTopology: true});
mongoose.Promise = global.Promise;
try{
    let db = mongoose.connection
    db.on("errr", console.error.bind("Erro de conexão com o banco de dados"))
}catch(error){
    console.log(error)
}

const router = express.Router()
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/', (req, res) => {
    res.send('teste oi')
})
app.get("/task", control_task.getTasks);
app.get("/task/:id", control_task.findTask);
app.post("/task", control_task.addTask);
app.put("/task/:id", control_task.putTask);
app.delete("/task/:id", control_task.removeTask);

app.use('/', router)

let porta = process.env.PORT || 3000

app.listen(porta, () => {
    console.log("servidor em execucao na porta " + porta)
})