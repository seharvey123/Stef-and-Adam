import random

ar_verbs = ['hablar', 'cantar', 'bailar','trabajar','estudiar','caminar','escuchar','llevar','comprar','mirar']
ir_verbs = ['correr', 'vender', 'aprender','comprender','creer','romer','temer','comer','beber','comer']
er_verbs = ['vivir', 'escribir', 'abrir','recibir','comprartir','decidir','subir','insistir','permitir','existir']

def get_verb(verb_type):
    if verb_type == 'ar':
        print (random.choice(ar_verbs))
    elif verb_type == 'er':
        print (random.choice(er_verbs))
    elif verb_type == 'ir':
        print (random.choice(ir_verbs))
    else:
        print ("Invalid Verb Type")

while True: #to make it go forever, it wouldn't be helpful to just use this tool once
    verb_type = input('Please enter what type of verb you want to practice, ar, er, or ir ')
    get_verb(verb_type)

