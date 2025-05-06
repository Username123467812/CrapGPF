# Enjoy my awful(ish) code!
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

def runProgram():
    print("--CrapGPF v" + version + "--")
    print("Enter '!quit' to exit program.")

    # data set profiles
    files_exist = False
    while not files_exist: # repeat asking for data set until input is a valid set
        profile = input("Data Profile (leave blank for default): ")
        try:
            open((profile + '-prompt-data.txt'), 'r')
            open((profile + '-answer-data.txt'), 'r')
        except:
            print("Data profile [" + profile + "] not found!")
            files_exist = False
        else:
            if profile == "":
                print("Using default data profile.")
            else:
                print("Using data profile [" + profile + "]")
            files_exist = True

    # main run loop
    while True:
        input_prompt = input(": ")
        if input_prompt.startswith("!"):
            if input_prompt == "!quit":
                print("--end--")
                exit()
            else:
                print("Command not recognized.")
        else:
            print("> " + prompt(input_prompt, profile))

# trigger the run loop
runProgram()
