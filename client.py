import requests
import json
import time

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

def findTask(url, id):
    url += "/"+id
    getTasks(url)
    

def exec():
    url = "http://localhost:3000/task"
    print("Isira: 1 para listar todas as tarefas.\n")
    print("Isira: 2 para listar uma tarefa.\n")
    print("Isira: 3 para sair.\n")
    escolha = int(input("Escolha: "))
    if(escolha == 1):
        getTasks(url)
    elif(escolha == 2):
        id = input("Insira o id da tarefa: ")
        findTask(url, id)
    elif(escolha == 3):
        exit()
    time.sleep(2)    
    exec()
    
exec()

