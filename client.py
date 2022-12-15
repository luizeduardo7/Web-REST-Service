import requests
import json
import time
import datetime

def getTasks(url):
    myResponse = requests.get(url)

    if(myResponse.ok):

        jData = json.loads(myResponse.content)

        print("Foram encontrados {0} tarefas.".format(len(jData)))
        print("\n")
        for task in jData:
            for atributo in task:
                print (atributo + ": " + str(task[atributo]))
            print("\n")
    else:
    # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()

def findTask(url):
    id = input("\nInsira o id da tarefa: ")
    url += "/"+id
    getTasks(url)

def addTask(url):
    descricao = input("Insira a descricao da tarefa: ")
    prazo = input("Insira o prazo da tarefa(MM/DD/AAAA): ")
    completa = input("Insira 'true' para tarefa completa, 'false' caso contrario: ")
    
    dic = {"id": id,"descricao": descricao, "prazo": prazo, "completa": completa} 
    res = requests.post(url=url, data=dic)
    if(res.ok):
        print("OK")
    else:
        print("NO")
        res.raise_for_status()

def alterTask(url):
    id = input("\nInsira o id da tarefa: ")
    url += "/"+id
    while(True):
        print("Isira 1 para mudar a descricao.\n")
        print("Isira 2 para mudar a prazo.\n")
        print("Isira 3 para mudar o status de completa.\n")
        print("Isira 4 para voltar.\n")
        escolha = int(input("Escolha: "))
        
        dic = {}
        if(escolha == 1): 
            descricao = input("Insira a descricao da tarefa: ")
            dic = {"descricao": descricao} 
        elif(escolha == 2):
            prazo = input("Insira o prazo da tarefa(MM/DD/AAAA): ")
            dic = {"prazo": prazo} 
        elif(escolha == 3):
            completa = input("Insira 'true' para tarefa completa, 'false' caso contrario: ")
            dic = {"completa": completa} 
        elif(escolha == 4):
            exec()
        else:
            exit()
            
        res = requests.put(url=url, data=dic)
        if(res.ok):
            print("OK")
        else:
            print("NO")
            res.raise_for_status()
        
def delTask(url):
    id = input("\nInsira o id da tarefa: ")
    url += "/"+id
    res = requests.delete(url=url)
    if(res.ok):
        print("OK")
    else:
        print("NO")
        res.raise_for_status()
    

def exec():
    url = "http://localhost:3000/task"
    
    print("Insira: 1 para listar todas as tarefas.\n")
    print("Insira: 2 para listar uma tarefa.\n")
    print("Insira: 3 para adicionar uma tarefa.\n")
    print("Insira: 4 para alterar uma tarefa.\n")
    print("Insira: 5 para deletar uma tarefa.\n")
    print("Insira: 6 para sair.\n")
    escolha = int(input("Escolha: "))
    if(escolha == 1):
        getTasks(url)
        time.sleep(2) 
    elif(escolha == 2):
        findTask(url)
        time.sleep(2) 
    elif(escolha == 3):
        addTask(url)
    elif(escolha == 4):
        alterTask(url)
    elif(escolha == 5):
        delTask(url)
    elif(escolha == 6):
        exit()
    else:
        exit()   
    exec()
    
exec()

