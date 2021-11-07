
WORDS_BANK = []

def Load_Data() :
    with open("words_bank.txt" , 'r') as f: #opens and closes the file after the next line
        big_text = f.read()
        words = big_text.split('\n')
    
    for i in range(0, len(words), 2) : #loading words to app 
        WORDS_BANK.append({'english' : words[i] , 'persian' : words[i+1]})       

def Save_New_Data():
    new_word= []
    continue_choice = 1
    while continue_choice :
        new_word.append(input('enter the english word you want to add: '))
        new_word.append(input('enter the persian translation: ')) 
        with open("words_bank.txt" , 'a') as f:
            f.write('\n' + new_word[0] + '\n' + new_word[1])
        new_word.clear()  #clears the new word list after adding to database        
        continue_choice= input('if you want to add another word enter "yes" else enter "no": ')
        if continue_choice == 'no':
            continue_choice= 0
            
    
def Translate_En2fa():
    input_text= input('please type your text: ')
    user_words= input_text.split(' ')
    output_text= ''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['english']:
                output_text += word['persian'] + ' '
                break
        else:
            output_text += user_word + ' '
        
    print(output_text)    
    
    
def Translate_Fa2en():
    input_text= input('please type your text: ')
    user_words= input_text.split(' ')
    output_text= ''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['persian']:
                output_text += word['english'] + ' '
                break
        else:
            output_text += user_word + ' '
        
    print(output_text)    
    
def Show_menu():
    print('-------------------------\nwelcome to mmd Dictionary\n-------------------------')
    print('1.Translate English to Persian')
    print('2.Translate Persian to English')
    print('3.Add new words to Data base')
    print('4.exit')    
    
Load_Data()        
while True:
    Show_menu()
    choice= input('please choose what you need: ')
    if choice == '1' : #translate english to persian
        Translate_En2fa()
    elif choice == '2': #tranlate persian to english
        Translate_Fa2en()
    elif choice == '3' : #add new word
        Save_New_Data()
    elif choice == '4': #exit
        break
    else:
        print('wrong choice')

        