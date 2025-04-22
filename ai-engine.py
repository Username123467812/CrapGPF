p_array = []
r_array = []

def loadFilePrompt():
    with open('prompt-data.txt', 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines] # remove line characters
def loadFileResponse():
    with open('answer-data.txt', 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines] # remove line characters

def getResponse(sentence):
    p_array = loadFilePrompt()
    r_array = loadFileResponse()
    words = sentence.split()
    best_index = 0
    best_length = 0
    
    # check compatability with prompts
    for i in range(len(p_array)):
        p_words = p_array[i].split()

        # get number of shared words
        try_length = len(set(p_words).intersection(set(words)))
        
        # see if the current response is more similiar
        if try_length > best_length:
            # set new record
            best_length = try_length
            best_index = i
    
    # return the best possible response
    return r_array[best_index]

def prompt(text):
    sentences = text.split(".")
    for i in range(len(sentences)):
        sentences[i].split("?")
    response = ""

    for i in range(len(sentences)):
        response = response + getResponse(sentences[i].replace("?","").replace("'","").replace(",",""))
    
    return response

def runLoop():
    while True:
        input_prompt = input()
        if input == "exit":
            exit()
        else:
            prompt(input())

# have a prompt happen
print(prompt(input()))