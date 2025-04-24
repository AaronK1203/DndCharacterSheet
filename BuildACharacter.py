def build(slot_num):

    #This collects the bare minimum information in order to get the character
    #Sheet up and running.

    print('Welcome to Build a Character')
    print('''Before you begin, this program will request names of files to be
used as character profiles or places to save data to.
Specifically, character profiles are of type .html, and save files should be
.txt with no spaces in either file names. You can also have the program create
a save file for you.

It's also highly recommended that these files be placed within the same
folder as these Python files, to make entering the file addresses easier on you.

Finally, if you have already selected a file to be used as a save slot,
bear in mind that this process will overwrite all data on this file, so
back it up to a different text file if the current information is important
to you.''')

    print('With all that said and done, are you ready to build a character?')
    print('Print \'Y\' for yes, anything else for no.')

    resp = input('/')

    if resp != 'Y':
        print('Cancelled')
        return
    
    print('Continuing...')


    #File making
    print('Would you like to make a new save file?')
    print('Print \'Y\' for yes, anything else for no.')
    print('(Note: If you already have a save file (.txt) available to use, choose no)')

    resp = input('/')

    if resp == 'Y':
        print('What would you like to name this file?')
        print("(Refrain from using spaces or periods. Use '_' or '-' instead. Do not include '.txt'")
        file_name = input('/') + '.txt'

        file1 = open(file_name,'w')
        file1.close()

        print(f'Save file \'{file_name}\' created')

    else:
        print('What is the name of the file you want to use? (Has to be of type .txt)')
        file_name = input('/')
        

    print('What is your character\'s name?')
    
    name = input('/')

    print("What is your character's class and level (E.G. Ranger I)?")

    class_level = input('/')

    print("What is your character's background?")

    background = input('/')

    print("What is your character's race?")

    race = input('/')
        
        
        
    
          
if __name__ == '__main__':
    build(0)
