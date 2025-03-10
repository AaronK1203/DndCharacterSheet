def build(slot_num):
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
    
    
        
        
        
    
          
if __name__ == '__main__':
    build(0)
