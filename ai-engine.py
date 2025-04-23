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
    words = sentence.lower().split()
    best_index = 0
    best_length = 0
    
    # check compatability with prompts
    for i in range(len(p_array)):
        p_words = p_array[i].lower().split()

        # get number of shared words
        try_length = len(set(p_words).intersection(set(words)))
        
        # see if the current response is more similiar
        if try_length > best_length:
            # set new record
            best_length = try_length
            best_index = i
    
    # return the best possible response if prompt's not blank
    output = r_array[best_index] + " "
    if sentence == "" or sentence == " ":
        output = ""
    return output

def prompt(text):
    sentences = text.split(".")
    sentences1 = sentences
    for i in range(len(sentences1)):
        sentences = sentences + sentences1[i].split("?")
    
    response_array = []

    for i in range(len(sentences)):
        if not getResponse(sentences[i].replace("'","").replace(",","")) in response_array:
            response_array.append(getResponse(sentences[i].replace("'","").replace(",","")))
    
    response = "".join(response_array)
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