p_array = ["","What's your favorite color?","How tall am I?","How do I start a war?","What color is a banana?","How to leave a country?"]
r_array = ["I can't respond to that.","I like the color orange.","I'll go with 1.7 meters, but I obviously can't say for sure.","War is not adviseable.","A banana is yellow.","Try crossing a border."]

def getResponse(sentence):
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
        getResponse(sentences[i])

def runLoop():
    input_prompt = input()
    if input == "exit":
        exit()
    else:
        prompt(input())