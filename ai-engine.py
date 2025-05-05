p_array = []
r_array = []
version = "0.1"

def loadFilePrompt(p):
    with open((p + '-prompt-data.txt'), 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines] # remove line characters
def loadFileResponse(p):
    with open((p + '-answer-data.txt'), 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines] # remove line characters

def getResponse(sentence, p):
    p_array = loadFilePrompt(p)
    r_array = loadFileResponse(p)
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

def prompt(text, p):
    sentences = text.split(".")
    sentences1 = sentences
    for i in range(len(sentences1)):
        sentences = sentences + sentences1[i].split("?")
    
    response_array = []

    for i in range(len(sentences)):
        if not getResponse(sentences[i].replace("'","").replace(",",""), p) in response_array:
            response_array.append(getResponse(sentences[i].replace("'","").replace(",",""), p))
    
    response = "".join(response_array)
    return response

def runLoop():
    print("--CrapGPF v" + version + "--")
    print("Enter '!quit' to exit program.")
    profile = input("Data Set Profile (leave blank for default): ")
    while True:
        input_prompt = input(": ")
        if input_prompt == "!quit":
            print("--end--")
            exit()
        else:
            print("> " + prompt(input_prompt, profile))

# have a prompt happen
runLoop()