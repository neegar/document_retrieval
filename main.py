import inquirer
 
file = 'ap_docs2.txt'

def read_file(file):
    with open (file, 'r') as file:
        documents = file.read().split('<NEW DOCUMENT>')
        for i, j  in enumerate(documents):
            documents[i] = set(j.lower().replace('\n', ' ').replace('.', '').replace(',', '').split(' '))

    return documents
    
doc = read_file(file)

 
def search_word(doc, word):
    a = []

    for i, j in enumerate(doc):
        if word.issubset(j):
           a.append(i)
    return a

def read_document(doc, list_d):
    global file
    number = int(input('Enter number of a file: '))
    if number in list_d:
        with open (file, 'r') as file:
            documents = file.read().split('<NEW DOCUMENT>')
            print(documents[number])

    else:
       print('invalid number, try again: ')
 
aaa = []

while True:
    questions = [
    inquirer.List('choice',
                    message="What would you like to do?",
                    choices=['Search for documents', 'Read document', 'Quit Program'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers['choice'] == 'Search for documents':
        word = set(input('enter a word: ').split(' '))
        list_d = search_word(doc, word)
        aaa = list_d
        print(aaa)
    elif answers['choice'] == 'Read document':   
        read_document(doc, aaa)
    elif answers['choice'] == 'Quit Program':
        print('bye bye')
        break
