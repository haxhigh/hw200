import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

questions = [
     " What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Patty\n d.Pizza",
     " Water boils at 212 Units at which scale? \n a.Fahrenheit\n b.Celsius\n c.Rankine\n d.Kelvin",
     " Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\n c.Walrus\n d.Seal",
     " Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Jack\n c.Johnny\n d.Mukesh",
]

answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a']

print("Server has started...")

def get_random_question_answer(conn):
    random_index = random.randint(0,len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    connection.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(conn):
    score = 0
    connection.send("Welcome to this quiz game!".encode('utf-8'))
    connection.send("You will receive a question. The answer to that question should be one of a, b, c or d\n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = connection.recv(2048).decode('utf-8')
            if message: 
                if message.lower() == answer:
                    score += 1
                    connection.send(f"correct answer!! your score is: {score}\n\n".encode('utf-8'))
                else:
                    connection.send("wrong answer\n\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else:
                remove(connection)
        except:
            continue

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    connection, addr = server.accept()
    list_of_clients.append(connection)
    print (addr[0] + " connected")
    new_thread = Thread(target= clientthread,args=(connection))
    new_thread.start()