const Task = require('./model-task');


exports.getTasks = function(req, res){
    Task.find({}, function(err, tasks){
        if(err) return next(err);
        return res.json(tasks);
    });
}

exports.findTask = function(req, res){
    Task.find(req.params, function(err, tasks){
        if(err) return next(err);
        return res.json(tasks);
    });
}

incremento = 0;
exports.addTask = function(req, res){
    let task = new Task({
        id: incremento++,
        descricao: req.body.descricao,
        prazo: req.body.prazo,
        completa: req.body.completa
    });
    task.save(function(err){
        if(err) return next(err);
    });
    res.send("Tarefa cadastrada.")
}

exports.putTask = function(req, res){
    Task.updateMany(req.params, req.body, function(err){
        if(err) return next(err);
    });
    res.send("Tarefa alterada.")
}

exports.removeTask = function(req, res){
    Task.deleteOne(req.params, function(err, tasks){
        if(err) return next(err);
        return res.json(tasks);
    });
}
