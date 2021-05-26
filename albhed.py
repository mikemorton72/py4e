#Al Bhed Phrases to try:
    #Oui yvnyet uv dra cay? Faygmehk!
    #Drao yna dra cysa eh taydr.
    #Tu oui hud cbayg?

# Alphabets for english and Al Bhed
eng = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
alb = ('y','p','l','t','a','v','k','r','e','z','g','m','s','h','u','b','x','n','c','d','i','j','f','q','o','w')

#Letter substitution function
def translator(lang1,lang2,phrase):
    newphrase = ""

    for letter in phrase:
        try:
            #account for uppercase (make swap in lower)
            if letter.isupper():
                newphrase = newphrase + (lang2[lang1.index(letter.lower())]).upper()
            else:
                newphrase = newphrase + (lang2[lang1.index(letter)])
        #if phrase chracter not in alphabet, leave unchanged (usually numbers/punctuation/spaces)
        except:
            newphrase = newphrase + letter

    return newphrase

#Run program, get info from user, call function, and print result
while True:
    modes = ('1','2','3')
    mode = input("\nSelect translation mode:\nEnglish to Al Bhed (1)\nAl Bhed to English (2)\nQuit (3)\n>> ")

    if mode not in modes:
        print('\n\nInvalid input, please select one of the options below:')
        continue
    if mode == '3':
        break
    phrase = input("\nEnter phrase to be translated:\n>> ")
    if mode == '1':
        print('\nTranslated phrase:\n',translator(eng,alb,phrase))
    elif mode == '2':
        print('\nTranslated phrase:\n',translator(alb,eng,phrase))
