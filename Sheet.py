import tkinter as tk
from tkinter import ttk
import random
import webbrowser as browser



def main(file_name):
    #print(f'Opening {file_name}')
    file1 = open(file_name)
    
    #Attributes of a DND Character
    name = 'xxx-xxx'
    class_level = 'xxx-0'
    background = 'xxx'
    race = 'xxx'
    alignment = 'xxx'
    xp_points = '0'
    
    personality = 'Does not load correctly, enjoys absent files'
    ideals = 'Will never load save data, ever'
    bonds = 'Do not load the information'
    flaws = 'Doesn\'t work'
    features_traits = 'BlahBlahBlah'
    
    html_file = 'Nothing.htmL+bozo'

    ab_scores = {'strength':0, 'dext':0, 'const':0, 'intel':0,
                      'wis':0, 'charis':0 }
    ab_modifiers = { 'strength':0, 'dext':0, 'const':0, 'intel':0,
                      'wis':0, 'charis':0 }

    passive_wisdom = 0
    inspiration = 0
    prof_bonus = 0

    saving_throws = []
    skills = []
    other_skills = ''

    armor_class = 0
    initiative = 0
    speed = 0

    hp = 0
    max_hp = 0
    temp_hp = 0

    hit_dice = '1d4'

    weapons = [['weapon1','atkbonus1','die1'],['weapon2','atkbonus2','die2']]

    money = 'None lol'

    inventory_nums = [[0,'itemname'],[0,'itemname2']]

    treasure = ''

    spellcasting = 0

    spell_save = 'd10'

    spell_atk_bonus = 0

    cantrips = []

    num_slots = []
    
    max_slots = []

    lvl1_spells = []
    
    lvl2_spells = []

    lvl3_spells = []

    lvl4_spells = []

    lvl5_spells = []

    lvl6_spells = []

    lvl7_spells = []

    lvl8_spells = []

    lvl9_spells = []

    all_spells = [lvl1_spells,lvl2_spells,lvl3_spells,lvl4_spells,lvl5_spells,
                      lvl6_spells,lvl7_spells,lvl8_spells,lvl9_spells]
    
    character_data = file1.read()
    file1.close()
    #To help speed things along
    def data_at(key):
        start = character_data.find(key + '[')
        if(start == -1):
            return
        start += (len(key) + 1)
        end = character_data.find(']',start)
        return character_data[start:end]
        
    #Mein Gott
    try:
        name = data_at('name')
        class_level = data_at('class_level')
        background = data_at('background')
        race = data_at('race')
        alignment = data_at('alignment')
        xp_points = data_at('xp_points')

        personality = data_at('personality')
        ideals = data_at('ideals')
        bonds = data_at('bonds')
        flaws = data_at('flaws')

        features_traits = data_at('features_traits')
        
        html_file = data_at('html_file')

        ab_scores['strength'],ab_modifiers['strength'] = (str)(data_at('strength')).split(',')
        ab_scores['dext'],ab_modifiers['dext'] = (str)(data_at('dexterity')).split(',')
        ab_scores['const'],ab_modifiers['const'] = (str)(data_at('constitution')).split(',')
        ab_scores['intel'],ab_modifiers['intel'] = (str)(data_at('intelligence')).split(',')
        ab_scores['wis'],ab_modifiers['wis'] = (str)(data_at('wisdom')).split(',')
        ab_scores['charis'],ab_modifiers['charis'] = (str)(data_at('charisma')).split(',')

        passive_wisdom = data_at('wisdom_pass')
        inspiration = (data_at('inspiration'))
        prof_bonus = int(data_at('prof_bonus'))

        saving_throws = str(data_at('saving_throws')).split(',')
        skills = str(data_at('skills')).split(',')
        other_skills = str(data_at('skills_other'))

        armor_class = int(data_at('armor_class'))
        initiative = int(data_at('initiative'))
        speed = int(data_at('speed'))

        hp = int(data_at('hp'))
        max_hp = int(data_at('hp_max'))
        temp_hp = int(data_at('hp_temp'))

        hit_dice = data_at('hit_dice')

        weapons = data_at('weapons')

        money = (data_at('money').split(','))
        for i in range(len(money)):
            money[i] = int(money[i])

        inventory_nums = data_at('inventory_nums')

        treasure = data_at('treasure')

        spellcasting = data_at('spellcasting')

        spell_save = data_at('spell_save')

        spell_atk_bonus = data_at('spell_atk_bonus')

        cantrips = data_at('cantrips').split('|')
        for i in range(len(cantrips)):
            cantrips[i] = cantrips[i].split('$')

        num_slots = data_at('num_slots').split(',')

        max_slots = data_at('max_slots').split(',')

        for i in range(len(num_slots)):
            num_slots[i] = int(num_slots[i])
            max_slots[i] = int(max_slots[i])

        lvl1_spells = data_at('lvl1_spells').split('|')
        for i in range(len(lvl1_spells)):
            lvl1_spells[i] = lvl1_spells[i].split('$')

        lvl2_spells = data_at('lvl2_spells').split('|')
        for i in range(len(lvl2_spells)):
            lvl2_spells[i] = lvl2_spells[i].split('$')

        lvl3_spells = data_at('lvl3_spells').split('|')
        for i in range(len(lvl3_spells)):
            lvl3_spells[i] = lvl3_spells[i].split('$')

        lvl4_spells = data_at('lvl4_spells').split('|')
        for i in range(len(lvl4_spells)):
            lvl4_spells[i] = lvl4_spells[i].split('$')

        lvl5_spells = data_at('lvl5_spells').split('|')
        for i in range(len(lvl5_spells)):
            lvl5_spells[i] = lvl5_spells[i].split('$')

        lvl6_spells = data_at('lvl6_spells').split('|')
        for i in range(len(lvl6_spells)):
            lvl6_spells[i] = lvl6_spells[i].split('$')

        lvl7_spells = data_at('lvl7_spells').split('|')
        for i in range(len(lvl7_spells)):
            lvl7_spells[i] = lvl7_spells[i].split('$')

        lvl8_spells = data_at('lvl8_spells').split('|')
        for i in range(len(lvl8_spells)):
            lvl8_spells[i] = lvl8_spells[i].split('$')

        lvl9_spells = data_at('lvl9_spells').split('|')
        for i in range(len(lvl9_spells)):
            lvl9_spells[i] = lvl9_spells[i].split('$')
            
        all_spells = [cantrips,lvl1_spells,lvl2_spells,lvl3_spells,lvl4_spells,lvl5_spells,
                      lvl6_spells,lvl7_spells,lvl8_spells,lvl9_spells]
        
    except Exception:
        print('Error Fetching Data')
    
    
    def write():
        nonlocal weapons
        nonlocal inventory_nums
        #Format specific data to save to csv

        if weapons == '':
            weapons = ',,|,,'
        if inventory_nums == '':
            inventory_nums = '0,placeholder'

        #Spells
        cantrips_str = ''
        for row in cantrips:
            cantrips_str += row[0] + '$' + row[1] + '|'
        cantrips_str = cantrips_str[0:len(cantrips_str)-1]

        lvl1_str = ''
        for row in lvl1_spells:
            lvl1_str += row[0] + '$' + row[1] + '|'
        lvl1_str = lvl1_str[0:len(lvl1_str)-1]

        lvl2_str = ''
        for row in lvl2_spells:
            lvl2_str += row[0] + '$' + row[1] + '|'
        lvl2_str = lvl2_str[0:len(lvl2_str)-1]

        lvl3_str = ''
        for row in lvl3_spells:
            lvl3_str += row[0] + '$' + row[1] + '|'
        lvl3_str = lvl3_str[0:len(lvl3_str)-1]

        lvl4_str = ''
        for row in lvl4_spells:
            lvl4_str += row[0] + '$' + row[1] + '|'
        lvl4_str = lvl4_str[0:len(lvl4_str)-1]

        lvl5_str = ''
        for row in lvl5_spells:
            lvl5_str += row[0] + '$' + row[1] + '|'
        lvl5_str = lvl5_str[0:len(lvl5_str)-1]

        lvl6_str = ''
        for row in lvl6_spells:
            lvl6_str += row[0] + '$' + row[1] + '|'
        lvl6_str = lvl6_str[0:len(lvl6_str)-1]

        lvl7_str = ''
        for row in lvl7_spells:
            lvl7_str += row[0] + '$' + row[1] + '|'
        lvl7_str = lvl7_str[0:len(lvl7_str)-1]

        lvl8_str = ''
        for row in lvl8_spells:
            lvl8_str += row[0] + '$' + row[1] + '|'
        lvl8_str = lvl8_str[0:len(lvl8_str)-1]

        lvl9_str = ''
        for row in lvl9_spells:
            lvl9_str += row[0] + '$' + row[1] + '|'
        lvl9_str = lvl9_str[0:len(lvl9_str)-1]
                
        
        character_data = f'''name[{name}]
class_level[{class_level}]
background[{background}]
race[{race}]
alignment[{alignment}]
xp_points[{xp_points}]

personality[{personality}]
ideals[{ideals}]
bonds[{bonds}]
flaws[{flaws}]

features_traits[{features_traits}]

html_file[{html_file}]

strength[{ab_scores['strength']},{ab_modifiers['strength']}]
dexterity[{ab_scores['dext']},{ab_modifiers['dext']}]
constitution[{ab_scores['const']},{ab_modifiers['const']}]
intelligence[{ab_scores['intel']},{ab_modifiers['intel']}]
wisdom[{ab_scores['wis']},{ab_modifiers['wis']}]
charisma[{ab_scores['charis']},{ab_modifiers['charis']}]

wisdom_pass[{passive_wisdom}]
inspiration[{inspiration}]
prof_bonus[{prof_bonus}]

saving_throws{str(saving_throws).replace('\'','').replace(' ','')}
skills{str(skills).replace('\'','').replace(' ','')}
skills_other[{other_skills}]

armor_class[{armor_class}]
initiative[{initiative}]
speed[{speed}]

hp[{hp}]
hp_max[{max_hp}]
hp_temp[{temp_hp}]

hit_dice[{hit_dice}]

weapons[{weapons}]

money{money}

inventory_nums[{inventory_nums}]
treasure[{treasure}]

spellcasting[{spellcasting}]

spell_save[{spell_save}]

spell_atk_bonus[{spell_atk_bonus}]

cantrips[{cantrips_str}]

num_slots{str(num_slots).replace(' ','').replace("'",'')}

max_slots{str(max_slots).replace(' ','').replace("'",'')}

lvl1_spells[{lvl1_str}]

lvl2_spells[{lvl2_str}]

lvl3_spells[{lvl3_str}]

lvl4_spells[{lvl4_str}]

lvl5_spells[{lvl5_str}]

lvl6_spells[{lvl6_str}]

lvl7_spells[{lvl7_str}]

lvl8_spells[{lvl8_str}]

lvl9_spells[{lvl9_str}]
'''

        
        file2 = open(file_name,'w')
        file2.write(character_data)
        file2.close()
        #print(character_data)
        
    #For now, just prints the data, but in the future will write to
    #the intended file
    #write()

    
    # V V V V V V V GUI STARTS HERE V V V V V V V V    
    root = tk.Tk()
    root.title('D&D Character Sheet')
    root.geometry('1200x950')        


    '''Spell Sheet'''
    #Note: For testing purposes only
    def print_spells():
        print('Cantrips:')
        print(cantrips)
        print('Slots Available:')
        print(num_slots)
        print('Slots Total:')
        print(max_slots)
        
    def open_spells():
        nonlocal all_spells
        #Specifies the level being looked at (i)
        splvl = tk.IntVar()
        #Specifies the spell in said level (j)
        splnum = tk.IntVar()
        #A 3d Array that stores all of the widgets in each frame (For universal reference)
        spell_widgets = [[[]]]

        #Writes whatever is in the text box to the responding spell's description
        def set_desc():
            nonlocal all_spells
            all_spells[splvl.get()][splnum.get()][1] = description_box.get(1.0,tk.END)
        #Writes all spell information
        def set_spells():
            nonlocal all_spells
            #All the spell widgets
            for i in range(len(spell_widgets)):
                #print(f'Level {i}')
                #Spell widgets at level i
                for j in range(len(spell_widgets[i])):
                    #print(j)
                    all_spells[i][j][0] = spell_widgets[i][j][0].get()
        #Writes the description of the spell at (i,j) to the description box
        def write_desc(i,j):
           nonlocal all_spells
           #print(all_spells[i][j][1])
           splvl.set(i); splnum.set(j)
           description_box.delete(1.0,tk.END)
           description_box.insert(1.0,all_spells[i][j][1])

        #Prereq: destination is of type tk.Label
        def set_num_slots(destination,i,amount):
            num_slots[i] = amount;
            if(num_slots[i] > max_slots[i]):
                num_slots[i] = max_slots[i]
            elif(num_slots[i] < 0):
                num_slots[i] = 0
            destination.config(text = f'Slots: {num_slots[i]}')
        #Prereq: destination is of type tk.Label
        def set_max_slots(destination,i,amount):
            max_slots = amount;
            if(max_slots[i] < 0):
                max_slots[i] = 0
            destination.config(text = f'Max Slots: {max_slots[i]}')
        
        spell_level = tk.Toplevel(root)
        spell_level.geometry('1000x800')
        spell_level.title('Spell Sheet')

        spellname_canvas = tk.Canvas(spell_level,width = 850,height = 80,bg = 'white')
        spellname_canvas.create_rectangle(2,2,850,80)
        spellname_canvas.place(relx = 0.5,rely = 0.0625,anchor = tk.CENTER)

        class_label = tk.Label(spellname_canvas,text = f'Class: {class_level}',width = 15,height = 2,font = ('Ariel',15))
        class_label.place(relx = 0.2,rely = 0.5,anchor = tk.CENTER)

        spellcasting_label = tk.Label(spellname_canvas,text = f'Spellcasting Ability\n{spellcasting}',width = 15,height = 2,font = ('Ariel',12))
        spellcasting_label.place(relx = 0.45,rely = 0.5,anchor = tk.CENTER)

        spellsave_label = tk.Label(spellname_canvas,text = f'Spell Save DC\n{spell_save}',width = 15,height = 2,font = ('Ariel',12))
        spellsave_label.place(relx = 0.65,rely = 0.5,anchor = tk.CENTER)

        spellatk_label = tk.Label(spellname_canvas,text = f'Spell Atk Bonus\n+{spell_atk_bonus}',width = 15,height = 2,font = ('Ariel',12))
        spellatk_label.place(relx = 0.85,rely = 0.5,anchor = tk.CENTER)
        
        '''Beginning of Individual Spell Levels'''

        #Cantrips
        cantrips_frame = tk.Frame(spell_level,width = 250,height = 150,highlightbackground = 'black',
                                  highlightthickness = 1)
        cantrips_frame.place(relx = 0.2,rely = 0.25,anchor = tk.CENTER)

        cantrips_canvas = tk.Canvas(cantrips_frame,width = 250,height = 150,bg = 'white')
        cantrips_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        cantrips_y_scrollbar = ttk.Scrollbar(cantrips_frame,orient = tk.VERTICAL,command = cantrips_canvas.yview)
        cantrips_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        cantrips_canvas.configure(yscrollcommand = cantrips_y_scrollbar.set)
        cantrips_canvas.bind("<Configure>",lambda e: cantrips_canvas.config(scrollregion = cantrips_canvas.bbox(tk.ALL)))

        cantrips_frame2 = tk.Frame(cantrips_canvas,width = 250,height = 150,bg = 'white')
        
        cantrips_canvas.create_window((0,0),window = cantrips_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Cantrips').place(relx = 0.2,rely = 0.135,anchor = tk.CENTER)

        for j in range(9):
            spell_widgets[0][j].append(tk.Entry(cantrips_frame2))
            spell_widgets[0][j].append(tk.Button(cantrips_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(0,j)))
            spell_widgets[0][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[0][j][1].grid(row = j,column = 2)
            spell_widgets[0][j][0].insert(0,cantrips[j][0])
            if j < 8:
                spell_widgets[0].append([])

        spell_widgets.append([[]])
        

        #Lvl 1 Spells
        spell_1_frame = tk.Frame(spell_level,width = 250,height = 150,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_1_frame.place(relx = 0.2,rely = 0.50,anchor = tk.CENTER)

        spell_1_canvas = tk.Canvas(spell_1_frame,width = 250,height = 150,bg = 'white')
        spell_1_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_1_y_scrollbar = ttk.Scrollbar(spell_1_frame,orient = tk.VERTICAL,command = spell_1_canvas.yview)
        spell_1_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_1_canvas.configure(yscrollcommand = spell_1_y_scrollbar.set)
        spell_1_canvas.bind("<Configure>",lambda e: spell_1_canvas.config(scrollregion = spell_1_canvas.bbox(tk.ALL)))

        spell_1_frame2 = tk.Frame(spell_1_canvas,width = 250,height = 150,bg = 'white')
        
        spell_1_canvas.create_window((0,0),window = spell_1_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 1 Spells').place(relx = 0.2,rely = 0.375,anchor = tk.CENTER)

        lvl1_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[0]}')
        lvl1_maxslots.place(relx = 0.1,rely = 0.375,anchor = tk.CENTER)

        lvl1_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[0]}')
        lvl1_totalslots.place(relx = 0.3,rely = 0.375,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl1_totalslots,0,num_slots[0]+1)).place(relx = 0.35,rely = 0.375,anchor = tk.CENTER)         
        for j in range(13):
            tk.Button(spell_1_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl1_totalslots,0,num_slots[0]-1)).grid(row = j,column = 0)
            spell_widgets[1][j].append(tk.Entry(spell_1_frame2))
            spell_widgets[1][j].append(tk.Button(spell_1_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(1,j)))
            spell_widgets[1][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[1][j][1].grid(row = j,column = 2)
            spell_widgets[1][j][0].insert(0,lvl1_spells[j][0])
            if j < 12:
                spell_widgets[1].append([])
                                
        spell_widgets.append([[]])


        #Lvl 2 Spells

        spell_2_frame = tk.Frame(spell_level,width = 250,height = 150,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_2_frame.place(relx = 0.2,rely = 0.75,anchor = tk.CENTER)

        spell_2_canvas = tk.Canvas(spell_2_frame,width = 250,height = 150,bg = 'white')
        spell_2_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_2_y_scrollbar = ttk.Scrollbar(spell_2_frame,orient = tk.VERTICAL,command = spell_2_canvas.yview)
        spell_2_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_2_canvas.configure(yscrollcommand = spell_2_y_scrollbar.set)
        spell_2_canvas.bind("<Configure>",lambda e: spell_2_canvas.config(scrollregion = spell_2_canvas.bbox(tk.ALL)))

        spell_2_frame2 = tk.Frame(spell_2_canvas,width = 250,height = 150,bg = 'white')
        
        spell_2_canvas.create_window((0,0),window = spell_2_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 2 Spells').place(relx = 0.2,rely = 0.625,anchor = tk.CENTER)

        lvl2_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[1]}')
        lvl2_maxslots.place(relx = 0.1,rely = 0.625,anchor = tk.CENTER)

        lvl2_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[1]}')
        lvl2_totalslots.place(relx = 0.3,rely = 0.625,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl2_totalslots,1,num_slots[1]+1)).place(relx = 0.35,rely = 0.625,anchor = tk.CENTER)         
        for j in range(13):
            tk.Button(spell_2_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl2_totalslots,1,num_slots[1]-1)).grid(row = j,column = 0)
            spell_widgets[2][j].append(tk.Entry(spell_2_frame2))
            spell_widgets[2][j].append(tk.Button(spell_2_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(2,j)))
            spell_widgets[2][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[2][j][1].grid(row = j,column = 2)
            spell_widgets[2][j][0].insert(0,lvl2_spells[j][0])
            if j < 12:
                spell_widgets[2].append([])
                                
        spell_widgets.append([[]])

        #Lvl 3 Spells

        spell_3_frame = tk.Frame(spell_level,width = 250,height = 150,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_3_frame.place(relx = 0.5,rely = 0.25,anchor = tk.CENTER)

        spell_3_canvas = tk.Canvas(spell_3_frame,width = 250,height = 150,bg = 'white')
        spell_3_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_3_y_scrollbar = ttk.Scrollbar(spell_3_frame,orient = tk.VERTICAL,command = spell_3_canvas.yview)
        spell_3_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_3_canvas.configure(yscrollcommand = spell_3_y_scrollbar.set)
        spell_3_canvas.bind("<Configure>",lambda e: spell_3_canvas.config(scrollregion = spell_3_canvas.bbox(tk.ALL)))

        spell_3_frame2 = tk.Frame(spell_3_canvas,width = 250,height = 150,bg = 'white')
        
        spell_3_canvas.create_window((0,0),window = spell_3_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 3 Spells').place(relx = 0.5,rely = 0.135,anchor = tk.CENTER)

        lvl3_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[2]}')
        lvl3_maxslots.place(relx = 0.4,rely = 0.135,anchor = tk.CENTER)

        lvl3_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[2]}')
        lvl3_totalslots.place(relx = 0.6,rely = 0.135,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl3_totalslots,2,num_slots[2]+1)).place(relx = 0.65,rely = 0.135,anchor = tk.CENTER)         
        for j in range(13):
            tk.Button(spell_3_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl3_totalslots,2,num_slots[2]-1)).grid(row = j,column = 0)
            spell_widgets[3][j].append(tk.Entry(spell_3_frame2))
            spell_widgets[3][j].append(tk.Button(spell_3_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(3,j)))
            spell_widgets[3][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[3][j][1].grid(row = j,column = 2)
            spell_widgets[3][j][0].insert(0,lvl3_spells[j][0])
            if j < 12:
                spell_widgets[3].append([])
                                
        spell_widgets.append([[]])

        #Lvl 4 Spells

        spell_4_frame = tk.Frame(spell_level,width = 250,height = 150,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_4_frame.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

        spell_4_canvas = tk.Canvas(spell_4_frame,width = 250,height = 150,bg = 'white')
        spell_4_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_4_y_scrollbar = ttk.Scrollbar(spell_4_frame,orient = tk.VERTICAL,command = spell_4_canvas.yview)
        spell_4_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_4_canvas.configure(yscrollcommand = spell_4_y_scrollbar.set)
        spell_4_canvas.bind("<Configure>",lambda e: spell_4_canvas.config(scrollregion = spell_4_canvas.bbox(tk.ALL)))

        spell_4_frame2 = tk.Frame(spell_4_canvas,width = 250,height = 150,bg = 'white')
        
        spell_4_canvas.create_window((0,0),window = spell_4_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 4 Spells').place(relx = 0.5,rely = 0.375,anchor = tk.CENTER)

        lvl4_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[3]}')
        lvl4_maxslots.place(relx = 0.4,rely = 0.375,anchor = tk.CENTER)

        lvl4_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[3]}')
        lvl4_totalslots.place(relx = 0.6,rely = 0.375,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl4_totalslots,3,num_slots[3]+1)).place(relx = 0.65,rely = 0.375,anchor = tk.CENTER)         
        for j in range(13):
            tk.Button(spell_4_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl4_totalslots,3,num_slots[3]-1)).grid(row = j,column = 0)
            spell_widgets[4][j].append(tk.Entry(spell_4_frame2))
            spell_widgets[4][j].append(tk.Button(spell_4_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(4,j)))
            spell_widgets[4][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[4][j][1].grid(row = j,column = 2)
            spell_widgets[4][j][0].insert(0,lvl4_spells[j][0])
            if j < 12:
                spell_widgets[4].append([])

        spell_widgets.append([[]])
                              
        #Lvl 5 Spells

        spell_5_frame = tk.Frame(spell_level,width = 250,height = 150,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_5_frame.place(relx = 0.5,rely = 0.75,anchor = tk.CENTER)

        spell_5_canvas = tk.Canvas(spell_5_frame,width = 250,height = 150,bg = 'white')
        spell_5_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_5_y_scrollbar = ttk.Scrollbar(spell_5_frame,orient = tk.VERTICAL,command = spell_5_canvas.yview)
        spell_5_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_5_canvas.configure(yscrollcommand = spell_5_y_scrollbar.set)
        spell_5_canvas.bind("<Configure>",lambda e: spell_5_canvas.config(scrollregion = spell_5_canvas.bbox(tk.ALL)))

        spell_5_frame2 = tk.Frame(spell_5_canvas,width = 250,height = 150,bg = 'white')
        
        spell_5_canvas.create_window((0,0),window = spell_5_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 5 Spells').place(relx = 0.5,rely = 0.625,anchor = tk.CENTER)

        lvl5_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[4]}')
        lvl5_maxslots.place(relx = 0.4,rely = 0.625,anchor = tk.CENTER)

        lvl5_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[4]}')
        lvl5_totalslots.place(relx = 0.6,rely = 0.625,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl5_totalslots,4,num_slots[4]+1)).place(relx = 0.65,rely = 0.625,anchor = tk.CENTER)         
        for j in range(9):
            tk.Button(spell_5_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl5_totalslots,4,num_slots[4]-1)).grid(row = j,column = 0)
            spell_widgets[5][j].append(tk.Entry(spell_5_frame2))
            spell_widgets[5][j].append(tk.Button(spell_5_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(5,j)))
            spell_widgets[5][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[5][j][1].grid(row = j,column = 2)
            spell_widgets[5][j][0].insert(0,lvl5_spells[j][0])
            if j < 8:
                spell_widgets[5].append([])
                                
        spell_widgets.append([[]])

        #Lvl 6 Spells

        spell_6_frame = tk.Frame(spell_level,width = 250,height = 100,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_6_frame.place(relx = 0.8,rely = 0.225,anchor = tk.CENTER)

        spell_6_canvas = tk.Canvas(spell_6_frame,width = 250,height = 100,bg = 'white')
        spell_6_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_6_y_scrollbar = ttk.Scrollbar(spell_6_frame,orient = tk.VERTICAL,command = spell_6_canvas.yview)
        spell_6_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_6_canvas.configure(yscrollcommand = spell_6_y_scrollbar.set)
        spell_6_canvas.bind("<Configure>",lambda e: spell_6_canvas.config(scrollregion = spell_6_canvas.bbox(tk.ALL)))

        spell_6_frame2 = tk.Frame(spell_6_canvas,width = 250,height = 100,bg = 'white')
        
        spell_6_canvas.create_window((0,0),window = spell_6_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 6 Spells').place(relx = 0.8,rely = 0.135,anchor = tk.CENTER)

        lvl6_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[5]}')
        lvl6_maxslots.place(relx = 0.7,rely = 0.135,anchor = tk.CENTER)

        lvl6_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[5]}')
        lvl6_totalslots.place(relx = 0.9,rely = 0.135,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl6_totalslots,5,num_slots[5]+1)).place(relx = 0.95,rely = 0.135,anchor = tk.CENTER)         
        for j in range(9):
            tk.Button(spell_6_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl6_totalslots,5,num_slots[5]-1)).grid(row = j,column = 0)
            spell_widgets[6][j].append(tk.Entry(spell_6_frame2))
            spell_widgets[6][j].append(tk.Button(spell_6_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(6,j)))
            spell_widgets[6][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[6][j][1].grid(row = j,column = 2)
            spell_widgets[6][j][0].insert(0,lvl6_spells[j][0])
            if j < 8:
                spell_widgets[6].append([])
                                
        spell_widgets.append([[]])

        #Lvl 7 Spells

        spell_7_frame = tk.Frame(spell_level,width = 250,height = 100,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_7_frame.place(relx = 0.8,rely = 0.4,anchor = tk.CENTER)

        spell_7_canvas = tk.Canvas(spell_7_frame,width = 250,height = 100,bg = 'white')
        spell_7_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_7_y_scrollbar = ttk.Scrollbar(spell_7_frame,orient = tk.VERTICAL,command = spell_7_canvas.yview)
        spell_7_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_7_canvas.configure(yscrollcommand = spell_7_y_scrollbar.set)
        spell_7_canvas.bind("<Configure>",lambda e: spell_7_canvas.config(scrollregion = spell_7_canvas.bbox(tk.ALL)))

        spell_7_frame2 = tk.Frame(spell_7_canvas,width = 250,height = 100,bg = 'white')
        
        spell_7_canvas.create_window((0,0),window = spell_7_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 7 Spells').place(relx = 0.8,rely = 0.31,anchor = tk.CENTER)

        lvl7_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[6]}')
        lvl7_maxslots.place(relx = 0.7,rely = 0.31,anchor = tk.CENTER)

        lvl7_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[6]}')
        lvl7_totalslots.place(relx = 0.9,rely = 0.31,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl7_totalslots,6,num_slots[6]+1)).place(relx = 0.95,rely = 0.31,anchor = tk.CENTER)         
        for j in range(9):
            tk.Button(spell_7_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl7_totalslots,6,num_slots[6]-1)).grid(row = j,column = 0)
            spell_widgets[7][j].append(tk.Entry(spell_7_frame2))
            spell_widgets[7][j].append(tk.Button(spell_7_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(7,j)))
            spell_widgets[7][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[7][j][1].grid(row = j,column = 2)
            spell_widgets[7][j][0].insert(0,lvl7_spells[j][0])
            if j < 8:
                spell_widgets[7].append([])
                                
        spell_widgets.append([[]])

        #Lvl 8 Spells

        spell_8_frame = tk.Frame(spell_level,width = 250,height = 100,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_8_frame.place(relx = 0.8,rely = 0.575,anchor = tk.CENTER)

        spell_8_canvas = tk.Canvas(spell_8_frame,width = 250,height = 100,bg = 'white')
        spell_8_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_8_y_scrollbar = ttk.Scrollbar(spell_8_frame,orient = tk.VERTICAL,command = spell_8_canvas.yview)
        spell_8_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_8_canvas.configure(yscrollcommand = spell_8_y_scrollbar.set)
        spell_8_canvas.bind("<Configure>",lambda e: spell_8_canvas.config(scrollregion = spell_8_canvas.bbox(tk.ALL)))

        spell_8_frame2 = tk.Frame(spell_8_canvas,width = 250,height = 100,bg = 'white')
        
        spell_8_canvas.create_window((0,0),window = spell_8_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 8 Spells').place(relx = 0.8,rely = 0.485,anchor = tk.CENTER)

        lvl8_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[7]}')
        lvl8_maxslots.place(relx = 0.7,rely = 0.485,anchor = tk.CENTER)

        lvl8_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[7]}')
        lvl8_totalslots.place(relx = 0.9,rely = 0.485,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl8_totalslots,7,num_slots[7]+1)).place(relx = 0.95,rely = 0.485,anchor = tk.CENTER)         
        for j in range(7):
            tk.Button(spell_8_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl8_totalslots,7,num_slots[7]-1)).grid(row = j,column = 0)
            spell_widgets[8][j].append(tk.Entry(spell_8_frame2))
            spell_widgets[8][j].append(tk.Button(spell_8_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(8,j)))
            spell_widgets[8][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[8][j][1].grid(row = j,column = 2)
            spell_widgets[8][j][0].insert(0,lvl8_spells[j][0])
            if j < 6:
                spell_widgets[8].append([])
                                
        spell_widgets.append([[]])

        #Lvl 9 Spells

        spell_9_frame = tk.Frame(spell_level,width = 250,height = 100,highlightbackground = 'black',
                          highlightthickness = 1)
        spell_9_frame.place(relx = 0.8,rely = 0.750,anchor = tk.CENTER)

        spell_9_canvas = tk.Canvas(spell_9_frame,width = 250,height = 100,bg = 'white')
        spell_9_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

        spell_9_y_scrollbar = ttk.Scrollbar(spell_9_frame,orient = tk.VERTICAL,command = spell_9_canvas.yview)
        spell_9_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

        spell_9_canvas.configure(yscrollcommand = spell_9_y_scrollbar.set)
        spell_9_canvas.bind("<Configure>",lambda e: spell_9_canvas.config(scrollregion = spell_9_canvas.bbox(tk.ALL)))

        spell_9_frame2 = tk.Frame(spell_9_canvas,width = 250,height = 100,bg = 'white')
        
        spell_9_canvas.create_window((0,0),window = spell_9_frame2,anchor = tk.NW)

        tk.Label(spell_level,text = 'Level 9 Spells').place(relx = 0.8,rely = 0.66,anchor = tk.CENTER)

        lvl9_maxslots = tk.Label(spell_level,text = f'Max Slots: {max_slots[8]}')
        lvl9_maxslots.place(relx = 0.7,rely = 0.66,anchor = tk.CENTER)

        lvl9_totalslots = tk.Label(spell_level,text = f'Slots: {num_slots[8]}')
        lvl9_totalslots.place(relx = 0.9,rely = 0.66,anchor = tk.CENTER)

        tk.Button(spell_level,text = '+',width = 2,command = lambda: set_num_slots(lvl9_totalslots,8,num_slots[8]+1)).place(relx = 0.95,rely = 0.66,anchor = tk.CENTER)         
        for j in range(7):
            tk.Button(spell_9_frame2,text = '-',width = 2,command = lambda: set_num_slots(lvl9_totalslots,8,num_slots[8]-1)).grid(row = j,column = 0)
            spell_widgets[9][j].append(tk.Entry(spell_9_frame2))
            spell_widgets[9][j].append(tk.Button(spell_9_frame2,text = 'Desc',width = 6,height = 1,command = lambda j=j: write_desc(9,j)))
            spell_widgets[9][j][0].grid(row = j,column = 1,padx = 2,pady = 1)
            spell_widgets[9][j][1].grid(row = j,column = 2)
            spell_widgets[9][j][0].insert(0,lvl9_spells[j][0])
            if j < 6:
                spell_widgets[9].append([])
                                

        maxlevel_labels = [lvl1_maxslots,lvl2_maxslots,lvl3_maxslots,lvl4_maxslots,lvl5_maxslots,lvl6_maxslots,lvl7_maxslots,lvl8_maxslots,lvl9_maxslots]


        '''End of Individual Spell Levels'''

        def spell_options():
            nonlocal max_slots
            spellops_level = tk.Toplevel(spell_level)
            spellops_level.title('Spell Options')
            spellops_level.geometry('600x500')

            
            maxslot_entries = []

            def set_all():
                nonlocal spellcasting
                nonlocal spell_save
                nonlocal spell_atk_bonus
                spellcasting = spellcasting_entry.get()
                spell_save = spellsave_entry.get()
                spell_atk_bonus = spellatkbonus_entry.get()

                spellcasting_label.config(text = f'Spellcasting Ability\n{spellcasting}')
                spellsave_label.config(text = f'Spell Save DC\n{spell_save}')
                spellatk_label.config(text = f'Spell Atk Bonus\n+{spell_atk_bonus}')

                try:
                    for i in range(len(maxslot_entries)):
                        max_slots[i] = int(maxslot_entries[i].get())
                        maxlevel_labels[i].config(text = f'Max Slots: {max_slots[i]}')
                except Exception:
                    pass

            tk.Label(spellops_level,text = 'Spellcasting').place(relx = 0.25,rely = 0.2,anchor = tk.CENTER)
            spellcasting_entry = tk.Entry(spellops_level)
            spellcasting_entry.place(relx = 0.25,rely = 0.25,anchor = tk.CENTER)
            spellcasting_entry.insert(0,spellcasting)

            tk.Label(spellops_level,text = 'Spell Save DC').place(relx = 0.25,rely = 0.45,anchor = tk.CENTER)
            spellsave_entry = tk.Entry(spellops_level)
            spellsave_entry.place(relx = 0.25,rely = 0.5,anchor = tk.CENTER)
            spellsave_entry.insert(0,spell_save)

            tk.Label(spellops_level,text = 'Spell Attack Bonus').place(relx = 0.25,rely = 0.7,anchor = tk.CENTER)
            spellatkbonus_entry = tk.Entry(spellops_level)
            spellatkbonus_entry.place(relx = 0.25,rely = 0.75,anchor = tk.CENTER)
            spellatkbonus_entry.insert(0,spell_atk_bonus)

            tk.Label(spellops_level,text = 'Max Slots Per Level').place(relx = 0.75,rely = 0.05,anchor = tk.CENTER)
            
            j = 0
            for i in range(9):
                j+=0.085
                tk.Label(spellops_level,text = f'Lvl {i+1}').place(relx = 0.705,rely = j,anchor = tk.CENTER)
                maxslot_entries.append(tk.Entry(spellops_level,width = 5))
                maxslot_entries[i].insert(0,max_slots[i])
                maxslot_entries[i].place(relx = 0.795,rely = j,anchor = tk.CENTER)
                

            setall_button = tk.Button(spellops_level,text = 'Set Values',width = 10,command = set_all)
            setall_button.place(relx = 0.5,rely = 0.875,anchor = tk.CENTER)
            
            done_button = tk.Button(spellops_level,text = 'Done',width = 10,command = spellops_level.destroy)
            done_button.place(relx = 0.5,rely = 0.95,anchor = tk.CENTER)
            
        
        description_box = tk.Text(spell_level,width = 30,height = 5)
        description_box.place(relx = 0.75,rely = 0.975,anchor = tk.S)

        set_desc_button = tk.Button(spell_level,text = 'Set Desc',
                                    width = 6,height = 1,command = set_desc)
        set_desc_button.place(relx = 0.925,rely = 0.925,anchor = tk.CENTER)

        set_button = tk.Button(spell_level,text = 'Set Spells',width = 10,command = set_spells)
        set_button.place(relx = 0.5,rely = 0.925,anchor = tk.S)

        spelloptions_button = tk.Button(spell_level,text = 'Options',width = 8,height = 3,command = spell_options)
        spelloptions_button.place(relx = 0.25,rely = 0.925,anchor = tk.CENTER)
        
        close_button = tk.Button(spell_level,text = 'Close',width = 10,height = 1,command = spell_level.destroy)
        close_button.place(relx = 0.5,rely = 0.975,anchor = tk.S)

        spell_level.mainloop()             


    spell_button = tk.Button(root,text = 'Spell Sheet',width = 14,height = 6,command = open_spells)
    spell_button.place(relx = 0.9,rely = 0.075,anchor = tk.CENTER)
    
    #Reference
    #dice_button = tk.Button(root,text = 'Dice Board',width = 14,height = 6,command = dice_board)
    #dice_button.place(relx = 0.1,rely = 0.075,anchor = tk.CENTER)
    '''End of Spell Sheet'''

    
    '''Name Plate'''
        
    name_canvas = tk.Canvas(root,width = 800,height = 100,bg = 'white')
    name_canvas.place(relx = 0.5,rely = 0.075,anchor = tk.CENTER)

    name_canvas.create_rectangle(2,2,800,100,outline = 'black')

    main_name = tk.Label(name_canvas,text = name,font = ('Arial',20))
    main_name.place(relx = 0.05,rely = 0.5,anchor = tk.W)

    classname_label = tk.Label(name_canvas,text = f'-Class: {class_level.replace(","," ")}  -Background: {background}',
             font = ('Arial',10))
    classname_label.place(relx = 0.5,rely = 0.3,anchor = tk.W)

    html_button = tk.Button(name_canvas,text = 'View Profile',width = 10,
                            command = lambda: browser.open_new_tab(html_file))
    html_button.place(relx = 0.94,rely = 0.3,anchor = tk.CENTER)

    racename_label = tk.Label(name_canvas,text = f'-Race: {race}  -Alignment: {alignment}  -XP: {xp_points}',
             font = ('Arial',10))
    racename_label.place(relx = 0.5,rely = 0.7,anchor = tk.W)

    tk.Label(name_canvas,text = 'Name:').place(relx = 0.05,rely = 0.15,
                                               anchor = tk.W)
    '''End of Name Plate'''


    '''Abilities Plate'''     

    mod_labels = []
    score_labels = []
        
    ability_canvas = tk.Canvas(root,width = 110,height = 600,bg = 'white')
    ability_canvas.place(relx = 0.1,rely = 0.775,anchor = tk.S)

    ab_rect = ability_canvas.create_rectangle(2,2,110,600,outline = 'black')
    
    i = 0.05
    j = 0
    AB_NAMES = ['STRENGTH','DEXTERITY','CONSTITUTION','INTELLIGENCE','WISDOM','CHARISMA']
    for ab in ab_scores:
        tk.Label(ability_canvas,text = f'  {AB_NAMES[j]}  ').place(relx = 0.5,rely = i,
                                                 anchor = tk.CENTER)
        temp = ''
        if ab_modifiers[ab][0:1] != '-':
            temp = '+'+(ab_modifiers[ab])
        else:
            temp = ab_modifiers[ab]
            
        mod_labels.append(tk.Label(ability_canvas,text = temp,font = (25)))
        mod_labels[j].place(relx = 0.5,rely = i+0.05,anchor = tk.CENTER)
        score_labels.append(tk.Label(ability_canvas,text = ab_scores[ab]))
        score_labels[j].place(relx = 0.5,rely = i+0.1,anchor = tk.CENTER)
        i+=0.16
        j+=1

   
    
    '''End of Ability Plate'''

    '''Skills and Proficiencies'''
    passperc_canvas = tk.Canvas(root,width = 150,height = 75,bg = 'white')
    passperc_canvas.place(relx = 0.25,rely = 0.18,anchor = tk.CENTER)
    passperc_canvas.create_rectangle(2,2,150,75,outline = 'black')

    #Calculate Passive Perception
    
    pass_perc = int(ab_modifiers['wis']) + 10
    if 'Perception' in skills:
        pass_perc += prof_bonus
    

    passperc_label = tk.Label(passperc_canvas,text = f'Passive Wisdom: {passive_wisdom}')
    passperc_label.place(relx = 0.5,rely = 0.2,anchor = tk.CENTER)
    
    insp_label = tk.Label(passperc_canvas,text = f'Inspiration: {inspiration}')
    insp_label.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
    
    profb_label = tk.Label(passperc_canvas,text = f'Proficiency Bonus: +{prof_bonus}')
    profb_label.place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

    #Final
    ALL_SKILLS = 'Acrobatics,Animal-Handling,Arcana,Athletics,Deception,History,Insight,Intimidation,Investigation,Medicine,Nature,Perception,Performance,Persuasion,Religion,Slight-Of-Hand,Stealth,Survival'.split(',')
    skill_types_abs = 'D,W,I,S,Ch,I,W,Ch,I,W,I,W,Ch,Ch,I,D,D,W'.split(',')

    skills_canvas = tk.Canvas(root,width = 150,height = 400,bg = 'white')
    skills_canvas.place(relx = 0.25,rely = 0.775,anchor = tk.S)
    skills_canvas.create_rectangle(2,2,150,400,outline = 'black')

    skill_labels = []
    
    i = 0.035
    j = 0
    for skill in ALL_SKILLS:
        is_skill = skill + ': '
        if skill in skills:
            is_skill += f'[ X ] ({skill_types_abs[j]})'
        else:
            is_skill += f'[   ] ({skill_types_abs[j]})'
        skill_labels.append(tk.Label(skills_canvas,text = is_skill,font = ('Ariel',9)))
        skill_labels[-1].place(relx = 0.05,rely = i,anchor = tk.W)
        i+=0.0545
        j+=1
        
    tk.Label(skills_canvas,text = 'Skills',font = ('Ariel',8)).place(relx = 0.975,
                                                                     rely = 0.99,anchor = tk.SE)
        
    savthrows_canvas = tk.Canvas(root,width = 150,height = 110,bg = 'white')
    savthrows_canvas.place(relx = 0.25,rely = 0.285,anchor = tk.CENTER)
    savthrows_canvas.create_rectangle(2,2,150,110,outline = 'black')
    
    sv_labels = []

    
    i = 0.125
    for ab in AB_NAMES:
        is_sv = ab + ': '
        if ab in saving_throws:
            is_sv += '[ X ]'
        else:
            is_sv += '[   ]'
        sv_labels.append(tk.Label(savthrows_canvas,text = is_sv,font = ('Ariel',8)))
        sv_labels[-1].place(relx = 0.05,rely = i,anchor = tk.W)
        i+=0.15
        

    tk.Label(savthrows_canvas,text = 'Saving Throws',font = ('Ariel',6)).place(relx = 0.975,
                                                                     rely = 0.95,anchor = tk.SE)

    
    languages_canvas = tk.Canvas(root,width = 270,height = 180,bg = 'white')
    languages_canvas.place(relx = 0.185,rely = 0.885,anchor = tk.CENTER)
    languages_canvas.create_rectangle(2,2,270,180,outline = 'black')

    lang_text = tk.Text(languages_canvas,width = 42,height = 12.385,font = ('Ariel',8))
    lang_text.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

    lang_text.insert(tk.END,other_skills)

    tk.Label(languages_canvas,text = 'Other Proficiencies and Languages').place(relx = 0.5,rely = 0.9,
                                                                                anchor = tk.CENTER)
    
    '''End of Skills and Proficiencies'''



    '''Health and Armor'''


    def update_hp(mode):
        if istemp.get():
            mode += 3
        nonlocal hp
        nonlocal temp_hp
        if not updatehp_entry.get().isdigit():
            return
        if mode == 0:
            hp += int(updatehp_entry.get())
        elif mode == 1:
            hp = int(updatehp_entry.get())
        elif mode == 2:
            hp -= int(updatehp_entry.get())
        elif mode == 3:
            temp_hp += int(updatehp_entry.get())
        elif mode == 4:
            temp_hp = int(updatehp_entry.get())
        elif mode == 5:
            temp_hp -= int(updatehp_entry.get())
        

        #Final Checks
        if hp > int(max_hp):
            hp = int(max_hp)
        if hp < 0:
            hp = 0;
        if temp_hp < 0:
            temp_hp = 0
            
        health_label.config(text = f'{hp} HP')
        temphp_label.config(text = f'{temp_hp} Temporary HP')

    def update_ac(mode):
        nonlocal armor_class
        if mode == 0:
            armor_class += 1
        elif mode == 1:
            armor_class -= 1
        ac_label.config(text = armor_class)
            
        
    
    health_canvas = tk.Canvas(root,width = 350,height = 250,bg = 'white')
    health_canvas.place(relx = 0.5,rely = 0.355,anchor = tk.CENTER)
    health_canvas.create_rectangle(2,2,350,250,outline = 'black')
    health_canvas.create_line(0,125,350,125)

    maxhp_label = tk.Label(health_canvas,text = f'Max hp: {max_hp}')
    maxhp_label.place(relx = 0.5,rely = 0.1,anchor = tk.CENTER)

    health_label = tk.Label(health_canvas,text = f'{hp} HP',font = ('Ariel',25))
    health_label.place(relx = 0.5,rely = 0.25,anchor = tk.CENTER)

    temphp_label = tk.Label(health_canvas,text = f'{temp_hp} Temporary HP',font = ('Ariel',15))
    temphp_label.place(relx = 0.3,rely = 0.6,anchor = tk.W)

    istemp = tk.BooleanVar(health_canvas)
    istemp.set(False)

    edit_temphp = tk.Checkbutton(health_canvas,text = 'Edit Temp',variable = istemp,onvalue = True,
                                 offvalue = False,width = 8,height = 1)
    edit_temphp.place(relx = 0.15,rely = 0.6,anchor = tk.CENTER)

    updatehp_entry = tk.Entry(health_canvas,width = 10)
    updatehp_entry.place(relx = 0.2,rely = 0.25,anchor = tk.CENTER)
    updatehp_entry.insert(0,'1')

    plus_hp = tk.Button(health_canvas,text = '+',width = 2,height = 1,command = lambda: update_hp(0))
    plus_hp.place(relx = 0.2,rely = 0.15,anchor = tk.CENTER)
    
    equals_hp = tk.Button(health_canvas,text = '=',width = 2,height = 1,command = lambda: update_hp(1))
    equals_hp.place(relx = 0.05,rely = 0.25,anchor = tk.CENTER)

    minus_hp = tk.Button(health_canvas,text = '-',width = 2,height = 1,command = lambda: update_hp(2))
    minus_hp.place(relx = 0.2,rely = 0.35,anchor = tk.CENTER)

    health_canvas.create_line(0,187.5,350,187.5)
    health_canvas.create_line(175,187.5,175,250)
    
    hitdice_label = tk.Label(health_canvas,text = hit_dice,font = ('Ariel',12))
    hitdice_label.place(relx = 0.25,rely = 0.825,anchor = tk.CENTER)
    tk.Label(health_canvas,text = 'Hit Dice').place(relx = 0.25,rely = 0.94,anchor = tk.CENTER)

    #Death Saves
    tk.Label(health_canvas,text = 'Death Saves').place(relx = 0.75,rely = 0.94,anchor = tk.CENTER)
    tk.Label(health_canvas,text = 'S',font = ('Ariel',8)).place(relx = 0.51,rely = 0.8,anchor = tk.W)
    tk.Label(health_canvas,text = 'F',font = ('Ariel',8)).place(relx = 0.98,rely = 0.8,anchor = tk.E)

    for i in range(5):
        x = i/15 + 0.625
        tk.Checkbutton(health_canvas,width = 1,height = 1).place(relx = x,rely = 0.8,anchor = tk.CENTER)

    
    #Armor Class stuff
    armor_canvas = tk.Canvas(root,width = 350,height = 75,bg = 'white')
    armor_canvas.place(relx = 0.5,rely = 0.175,anchor = tk.CENTER)
    armor_canvas.create_rectangle(2,2,350,75,outline = 'black')
    armor_canvas.create_line(100,0,100,75)
    armor_canvas.create_line(250,0,250,75)

    ac_label = tk.Label(armor_canvas,text = armor_class,font = ('Ariel',15))
    ac_label.place(relx = 0.5,rely = 0.4,anchor = tk.CENTER)
    tk.Label(armor_canvas,text = 'Armor Class').place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

    plus_ac = tk.Button(armor_canvas,text = '+',width = 1,height = 1,command = lambda: update_ac(0))
    plus_ac.place(relx = 0.6,rely = 0.4,anchor = tk.CENTER)

    minus_ac = tk.Button(armor_canvas,text = '-',width = 1,height = 1,command = lambda: update_ac(1))
    minus_ac.place(relx = 0.4,rely = 0.4,anchor = tk.CENTER)

    speed_label = tk.Label(armor_canvas,text = f'{speed}',font = ('Ariel',20))
    speed_label.place(relx = 0.85,rely = 0.4,anchor = tk.CENTER)

    tk.Label(armor_canvas,text = 'Speed').place(relx = 0.85,rely = 0.8,anchor = tk.CENTER)
    
    #Displays Initiative, Which is just your Dex Modifier
    initiative_label = tk.Label(armor_canvas,text = f'+{initiative}',font = ('Ariel',20))
    initiative_label.place(relx = 0.15,rely = 0.4,anchor = tk.CENTER)
    tk.Label(armor_canvas,text = 'Initiative').place(relx = 0.15,rely = 0.8,anchor = tk.CENTER)

    

    

    
    
   
   

    '''End of Health and Armor'''

    '''Digital Dice'''
    def dice_board():

        dice_types = ['d4','d6','d8','d10','d100','d12','d20']

        def update_sums():
            nonlocal x
            nonlocal y
            nonlocal z
            total_label.config(text = f'Total Sum: {x+y+z}')
            side_label1.config(text = f'Left Sum: {x+y}')
            side_label2.config(text = f'Right Sum: {y+z}')

        def reset():
            nonlocal x
            nonlocal y
            nonlocal z
            x,y,z = 0,0,0
            
            num_label1.config(text = x)
            num_label2.config(text = y)
            num_label3.config(text = z)

            update_sums()

        def roll_x(die):
            nonlocal x
            if not die in dice_types:
                return
            if die == 'd4':
                x = random.randint(1,4)
            elif die == 'd6':
                x = random.randint(1,6)
            elif die == 'd8':
                x = random.randint(1,8)
            elif die == 'd10':
                x = random.randint(0,9)
            elif die == 'd100':
                x = random.randint(0,9) * 10
            elif die == 'd12':
                x = random.randint(1,12)
            elif die == 'd20':
                x = random.randint(1,20)

            num_label1.config(text = x)
            update_sums()

        def roll_y(die):
            nonlocal y
            if not die in dice_types:
                return
            if die == 'd4':
                y = random.randint(1,4)
            elif die == 'd6':
                y = random.randint(1,6)
            elif die == 'd8':
                y = random.randint(1,8)
            elif die == 'd10':
                y = random.randint(0,9)
            elif die == 'd100':
                y = random.randint(0,9) * 10
            elif die == 'd12':
                y = random.randint(1,12)
            elif die == 'd20':
                y = random.randint(1,20)

            num_label2.config(text = y)
            update_sums()

        def roll_z(die):
            nonlocal z
            if not die in dice_types:
                return
            if die == 'd4':
                z = random.randint(1,4)
            elif die == 'd6':
                z = random.randint(1,6)
            elif die == 'd8':
                z = random.randint(1,8)
            elif die == 'd10':
                z = random.randint(0,9)
            elif die == 'd100':
                z = random.randint(0,9) * 10
            elif die == 'd12':
                z = random.randint(1,12)
            elif die == 'd20':
                z = random.randint(1,20)

            num_label3.config(text = z)
            update_sums()
            
        
        
        dice_level = tk.Toplevel(root)
        dice_level.title('Let\'s Go Gambling!')
        dice_level.geometry('600x400+400+400')

        x = 1
        y = 2
        z = 3

        reset_button = tk.Button(dice_level,text = 'Reset',width = 10,command = reset)
        reset_button.place(relx = 0.5,rely = 0.925,anchor = tk.CENTER)

        close_button = tk.Button(dice_level,text = 'Close',width = 10,command = dice_level.destroy)
        close_button.place(relx = 0.825,rely = 0.925,anchor = tk.CENTER)

        canvas1 = tk.Canvas(dice_level,width = 180,height = 180,bg = 'white')
        canvas2 = tk.Canvas(dice_level,width = 180,height = 180,bg = 'white')
        canvas3 = tk.Canvas(dice_level,width = 180,height = 180,bg = 'white')

        canvas1.place(relx = 0.175,rely = 0.65,anchor = tk.CENTER)
        canvas2.place(relx = 0.5,rely = 0.65,anchor = tk.CENTER)
        canvas3.place(relx = 0.825,rely = 0.65,anchor = tk.CENTER)

        canvas1.create_rectangle(2,2,180,180,outline = 'black')
        canvas2.create_rectangle(2,2,180,180,outline = 'black')
        canvas3.create_rectangle(2,2,180,180,outline = 'black')

        num_label1 = tk.Label(canvas1,text = x,font = ('Ariel',30))
        num_label2 = tk.Label(canvas2,text = y,font = ('Ariel',30))
        num_label3 = tk.Label(canvas3,text = z,font = ('Ariel',30))

        num_label1.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
        num_label2.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
        num_label3.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

        total_label = tk.Label(canvas2,text = f'Total Sum: {x+y+z}')
        total_label.place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

        side_label1 = tk.Label(canvas1,text = f'Left Sum: {x+y}')
        side_label1.place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

        side_label2 = tk.Label(canvas3,text = f'Right Sum: {y+z}')
        side_label2.place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

        x_dice = []
        y_dice = []
        z_dice = []

        j = 0
        for die in dice_types:
            x_dice.append(tk.Button(dice_level,text = die,width = 10,command = lambda die=die: roll_x(die)))
            #x_dice[j].place(relx = 0.175,rely = i,anchor = tk.CENTER)
            j+=1
            
        i = 0.05
        for j in range(0,6,2):
            x_dice[j].place(relx = 0.1,rely = i,anchor = tk.CENTER)
            i+=0.1
            
        i = 0.05
        for j in range(1,7,2):
            x_dice[j].place(relx = 0.25,rely = i,anchor = tk.CENTER)
            i+=0.1

        x_dice[6].place(relx = 0.175,rely = i,anchor = tk.CENTER)

        j = 0
        for die in dice_types:
            y_dice.append(tk.Button(dice_level,text = die,width = 10,command = lambda die=die: roll_y(die)))
            #y_dice[j].place(relx = 0.175,rely = i,anchor = tk.CENTER)
            j+=1
            
        i = 0.05
        for j in range(0,6,2):
            y_dice[j].place(relx = 0.425,rely = i,anchor = tk.CENTER)
            i+=0.1
            
        i = 0.05
        for j in range(1,7,2):
            y_dice[j].place(relx = 0.575,rely = i,anchor = tk.CENTER)
            i+=0.1

        y_dice[6].place(relx = 0.5,rely = i,anchor = tk.CENTER)

        j = 0
        for die in dice_types:
            z_dice.append(tk.Button(dice_level,text = die,width = 10,command = lambda die=die: roll_z(die)))
            #z_dice[j].place(relx = 0.175,rely = i,anchor = tk.CENTER)
            j+=1
            
        i = 0.05
        for j in range(0,6,2):
            z_dice[j].place(relx = 0.75,rely = i,anchor = tk.CENTER)
            i+=0.1
            
        i = 0.05
        for j in range(1,7,2):
            z_dice[j].place(relx = 0.9,rely = i,anchor = tk.CENTER)
            i+=0.1

        z_dice[6].place(relx = 0.825,rely = i,anchor = tk.CENTER)
    
    dice_button = tk.Button(root,text = 'Dice Board',width = 14,height = 6,command = dice_board)
    dice_button.place(relx = 0.1,rely = 0.075,anchor = tk.CENTER)
    
    '''End of Digital Dice'''


    '''Weapons Inventory'''
    
    
    #Formatting weapons

    temp_array = weapons.split('|')
    weap_array = []

    i = 0

    for s in temp_array:
        weap_array.append(s.split(','))
        i+=1

    for j in range(20-i):
        weap_array.append(['','',''])
            
        
    wep_frame = tk.Frame(root,width = 350,height = 150,highlightbackground = 'black',
                          highlightthickness = 1)
    wep_frame.place(relx = 0.5,rely = 0.58,anchor = tk.CENTER)

    wep_canvas = tk.Canvas(wep_frame,width = 350,height = 150,bg = 'white')
    wep_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

    wep_y_scrollbar = ttk.Scrollbar(wep_frame,orient = tk.VERTICAL,command = wep_canvas.yview)
    wep_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

    wep_canvas.configure(yscrollcommand = wep_y_scrollbar.set)
    wep_canvas.bind("<Configure>",lambda e: wep_canvas.config(scrollregion = wep_canvas.bbox(tk.ALL)))

    wep_frame2 = tk.Frame(wep_canvas,width = 350,height = 150,bg = 'white')
        
    wep_canvas.create_window((0,0),window = wep_frame2,anchor = tk.NW)

    tk.Label(wep_frame2,text = 'Name').grid(row = 0,column = 0,sticky = tk.S)
    tk.Label(wep_frame2,text = 'Atk Bonus').grid(row = 0,column = 1,sticky = tk.S)
    tk.Label(wep_frame2,text = 'Dmg Type').grid(row = 0,column = 2,sticky = tk.S)
    tk.Label(wep_frame2,text = 'Attacks & Spellcasting').grid(row = 21,column = 1)
        
        
    #Notice, 2D, this stores ALL of the Entries
    entries2d = []

    for i in range(0,20):
        temp = []
        for j in range(3):
            temp.append(tk.Entry(wep_frame2,width = 19))
        entries2d.append(temp)

    for i in range(len(entries2d)):
        for j in range(len(entries2d[i])):
            entries2d[i][j].grid(row = i+1,column = j)
            entries2d[i][j].insert(0,weap_array[i][j])
        
        
                
            
        
    #To update weapons as the user edits
    def apply_weapons():
        nonlocal weapons
        nonlocal weap_array
        temp_s = ''
        for i in range(len(entries2d)):
            if (entries2d[i][0].get() != '') or (entries2d[i][1].get() != '') or (entries2d[i][2].get() != ''):
                temp_s += f'{entries2d[i][0].get()},{entries2d[i][1].get()},{entries2d[i][2].get()}|'
        temp_s = temp_s[0:len(temp_s)-1]
        if len(weap_array) == 0:
            temp_s = ',,|,,'
        weapons = temp_s


        

    '''End of Weapons Inventory'''


    '''Regular Inventory'''
    #Currency Handling
    COINS = ['cp','sp','ep','gp','pp']

    money_labels = []

    wallet_entries = []
    sum_entries = []
    ref_entries = []

    
            
    
    def open_wallet():
        wallet_entries = []
        sum_entries = []
        ref_entries = []

        def update_wallet():
            for i in range(len(wallet_entries)):
                money[i] = int(wallet_entries[i].get())
                wallet_entries[i].delete(0,tk.END)
                wallet_entries[i].insert(0,money[i])
                money_labels[len(money_labels)-(i+1)].config(text = money[i])
        
        wallet_level = tk.Toplevel(root)
        wallet_level.title('Wallet')
        wallet_level.geometry('800x500+400+400')

        

        #Placing Everything

        i = 0
        y = 0.1
        for coin in COINS:
            tk.Label(wallet_level,text = coin).place(relx = 0.05,rely = y,anchor = tk.CENTER)
            wallet_entries.append(tk.Entry(wallet_level,width = 15))
            wallet_entries[i].place(relx = 0.075,rely = y,anchor = tk.W)
            wallet_entries[i].insert(0,money[i])
            
            sum_entries.append(tk.Entry(wallet_level,width = 15))
            sum_entries[i].place(relx = 0.5,rely = y,anchor = tk.CENTER)
            sum_entries[i].insert(0,'0')

            ref_entries.append(tk.Entry(wallet_level,width = 15))
            ref_entries[i].place(relx = 0.925,rely = y,anchor = tk.E)
            ref_entries[i].insert(0,'0')
            
            i+=1
            y+=0.15

        #Other buttons
        set_button = tk.Button(wallet_level,width = 10,text = 'Set',command = update_wallet)
        set_button.place(relx = 0.1325,rely = 0.8,anchor = tk.CENTER)
            
        close_button = tk.Button(wallet_level,width = 10,text = 'Close',
                                 command = wallet_level.destroy)
        close_button.place(relx = 0.5,rely = 0.9,anchor = tk.CENTER)
        
        
    currency_canvas = tk.Canvas(root,width = 360,height = 60,bg = 'white')
    currency_canvas.place(relx = 0.5,rely = 0.705,anchor = tk.CENTER)
    currency_canvas.create_rectangle(2,2,360,60,outline = 'black')

    #LINES
    currency_canvas.create_rectangle(60,0,120,60)
    currency_canvas.create_rectangle(180,0,240,60)
    currency_canvas.create_rectangle(300,0,360,60)
    
    #Creates the labels (obviously)
    
    x = 1
    for i in range(len(COINS)-1,-1,-1):
        tk.Label(currency_canvas,text = COINS[i],font = ('Ariel',8)).place(relx = x/12,rely = 0.75,anchor = tk.CENTER)
        x+=2
    
    x = 1
    for i in range(len(money)):
        money_labels.append(tk.Label(currency_canvas,text = money[len(money)-(i+1)],font = ('Ariel',16)))
        money_labels[i].place(relx = x/12,rely = 0.4,anchor = tk.CENTER)
        x+=2
        
    wallet_button = tk.Button(currency_canvas,width = 5,height = 2,text = 'Wallet',command = open_wallet)
    wallet_button.place(relx = (0.91),rely = 0.5,anchor = tk.CENTER)

    #Actual Inventory
    temp_array = inventory_nums.split('|')
    number_items = []
    for i in range(len(temp_array)):
        temp = temp_array[i].split(',')
        number_items.append(temp)
    for i in range(len(number_items)):
        number_items[i][0] = int(number_items[i][0])

    #Records the numbers for the numbered items
    n_entries = []
    #Records the actual items
    ni_entries = []

    def apply_inventory_nums():
        nonlocal inventory_nums
        temp = ''
        for i in range(len(n_entries)):
            if ni_entries[i].get() != '':
                if n_entries[i].get() == '':
                    temp += f'1,{ni_entries[i].get()}|'
                else:
                    temp += f'{n_entries[i].get()},{ni_entries[i].get()}|'
        temp = temp[0:len(temp)-1]
        inventory_nums = temp
    

    inv_frame = tk.Frame(root,width = 350,height = 220,highlightbackground = 'black',
                          highlightthickness = 1)
    inv_frame.place(relx = 0.5,rely = 0.87,anchor = tk.CENTER)
    
    inv_canvas = tk.Frame(root,width = 350,height = 150,highlightbackground = 'black',
                          highlightthickness = 1)

    inv_canvas = tk.Canvas(inv_frame,width = 350,height = 220,bg = 'white')
    inv_canvas.pack(side = tk.LEFT,fill = tk.BOTH,expand = 0)

    inv_y_scrollbar = ttk.Scrollbar(inv_frame,orient = tk.VERTICAL,command = inv_canvas.yview)
    inv_y_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

    inv_canvas.configure(yscrollcommand = inv_y_scrollbar.set)
    inv_canvas.bind("<Configure>",lambda e: inv_canvas.config(scrollregion = inv_canvas.bbox(tk.ALL)))

    inv_frame2 = tk.Frame(inv_canvas,width = 350,height = 150,bg = 'white')
        
    inv_canvas.create_window((0,0),window = inv_frame2,anchor = tk.NW)
    #print(number_items)
    

    #Entry Stuff
    for i in range(40):
        n_entries.append(tk.Entry(inv_frame2,width = 5))
        ni_entries.append(tk.Entry(inv_frame2,width = 24))
        
    for i in range(0,40,2):
        n_entries[i].grid(row = i//2,column = 1)
        ni_entries[i].grid(row = i//2,column = 3)
        n_entries[i+1].grid(row = i//2,column = 5)
        ni_entries[i+1].grid(row = i//2,column = 7)
    for i in range(len(number_items)):
        n_entries[i].insert(0,number_items[i][0])
        ni_entries[i].insert(0,number_items[i][1])

    
    tk.Label(inv_frame2,text = 'Inventory').grid(row = 41,column = 3)
    
    #THERE BE TREASURE
    def open_treasure():
        nonlocal treasure

        #Why do I have to do this...?
        def apply():
            nonlocal treasure
            treasure = treasure_text.get('1.0',tk.END)
            
        treasure_level = tk.Toplevel(root)
        treasure_level.title('THERE BE TREASURE!')
        treasure_level.geometry('400x300+400+400')

        treasure_text = tk.Text(treasure_level,width = 40,height = 10,font = ('Ariel',12))
        treasure_text.place(relx = 0.5,rely = 0.4,anchor = tk.CENTER)
        treasure_text.insert(tk.END,treasure)
        
        
        apply_button = tk.Button(treasure_level,width = 10,text = 'Apply',
                                 command = apply)
        apply_button.place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)
        
        close_button = tk.Button(treasure_level,width = 10,text = 'Done',
                                 command = treasure_level.destroy)
        close_button.place(relx = 0.5,rely = 0.9,anchor = tk.CENTER)
        

    treasure_button = tk.Button(inv_frame2,width = 10,text = 'Treasure',command = open_treasure)
    treasure_button.grid(row = 41,column = 7)
    
        
    
       
    

    

    '''End of Regular Inventory'''

    #Home stretch

    '''Personality'''
    
    def update_personality():
        nonlocal personality
        nonlocal ideals
        nonlocal bonds
        nonlocal flaws
        nonlocal features_traits

        personality = personality_text.get('1.0',tk.END)
        ideals = ideals_text.get('1.0',tk.END)
        bonds = bonds_text.get('1.0',tk.END)
        flaws = flaws_text.get('1.0',tk.END)
        features_traits = features_text.get('1.0',tk.END)


        

    #Personality_traits   
    personality_canvas = tk.Canvas(root,width = 270,height = 80,bg = 'white')
    personality_canvas.place(relx = 0.83,rely = 0.188,anchor = tk.CENTER)
    personality_canvas.create_rectangle(2,2,270,80,outline = 'black')

    personality_text = tk.Text(personality_canvas,width = 42,height = 5,font = ('Ariel',8))
    personality_text.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

    personality_text.insert(tk.END,personality)

    tk.Label(personality_canvas,text = 'Personality Traits').place(relx = 0.5,rely = 0.8,
                                                                                anchor = tk.CENTER)

    #Ideals
    ideals_canvas = tk.Canvas(root,width = 270,height = 80,bg = 'white')
    ideals_canvas.place(relx = 0.83,rely = 0.288,anchor = tk.CENTER)
    ideals_canvas.create_rectangle(2,2,270,80,outline = 'black')

    ideals_text = tk.Text(ideals_canvas,width = 42,height = 5,font = ('Ariel',8))
    ideals_text.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

    ideals_text.insert(tk.END,ideals)

    tk.Label(ideals_canvas,text = 'Ideals').place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

    #Bonds
    bonds_canvas = tk.Canvas(root,width = 270,height = 80,bg = 'white')
    bonds_canvas.place(relx = 0.83,rely = 0.388,anchor = tk.CENTER)
    bonds_canvas.create_rectangle(2,2,270,80,outline = 'black')

    bonds_text = tk.Text(bonds_canvas,width = 42,height = 5,font = ('Ariel',8))
    bonds_text.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

    bonds_text.insert(tk.END,bonds)

    tk.Label(bonds_canvas,text = 'Bonds').place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

    #flaws
    flaws_canvas = tk.Canvas(root,width = 270,height = 80,bg = 'white')
    flaws_canvas.place(relx = 0.83,rely = 0.488,anchor = tk.CENTER)
    flaws_canvas.create_rectangle(2,2,270,80,outline = 'black')

    flaws_text = tk.Text(flaws_canvas,width = 42,height = 5,font = ('Ariel',8))
    flaws_text.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

    flaws_text.insert(tk.END,flaws)

    tk.Label(flaws_canvas,text = 'Flaws').place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

    #Features and Traits
    features_canvas = tk.Canvas(root,width = 270,height = 250,bg = 'white')
    features_canvas.place(relx = 0.83,rely = 0.7,anchor = tk.CENTER)
    features_canvas.create_rectangle(2,2,270,250,outline = 'black')

    features_text = tk.Text(features_canvas,width = 42,height = 16,font = ('Ariel',8))
    features_text.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)

    features_text.insert(tk.END,features_traits)

    tk.Label(features_canvas,text = 'Features & Traits').place(relx = 0.5,rely = 0.925,anchor = tk.CENTER)

    

    '''End of Personality'''

    
    

    '''Options'''
   
        
        
        
    def open_options():

        def set_name():
            nonlocal name
            nonlocal class_level
            nonlocal background
            nonlocal race
            nonlocal alignment
            nonlocal xp_points

            def apply_name():
                nonlocal name
                nonlocal class_level
                nonlocal background
                nonlocal race
                nonlocal alignment
                nonlocal xp_points

                name = name_entry.get()
                class_level = class_entry.get()
                background = background_entry.get()
                race = race_entry.get()
                alignment = alignment_entry.get()
                xp_points = xp_entry.get()

                main_name.config(text = name)
                classname_label.config(text = f'-Class: {class_level.replace(","," ")}  -Background: {background}')
                racename_label.config(text = f'-Race: {race}  -Alignment: {alignment}  -XP: {xp_points}')
                

                
                
            setname_level = tk.Toplevel(options_level)
            setname_level.title('Change Name Values')
            setname_level.geometry('600x350')

            tk.Label(setname_level,text = 'Change Nameplate').place(relx = 0.5,rely = 0.1,anchor = tk.CENTER)

            tk.Label(setname_level,text = 'Name').place(relx = 0.2,rely = 0.2,anchor = tk.CENTER)
            name_entry = tk.Entry(setname_level)
            name_entry.place(relx = 0.2,rely = 0.3,anchor = tk.CENTER)
            name_entry.insert(0,name)

            tk.Label(setname_level,text = 'Class & Level').place(relx = 0.5,rely = 0.2,anchor = tk.CENTER)
            class_entry = tk.Entry(setname_level)
            class_entry.place(relx = 0.5,rely = 0.3,anchor = tk.CENTER)
            class_entry.insert(0,class_level)

            tk.Label(setname_level,text = 'Background').place(relx = 0.8,rely = 0.2,anchor = tk.CENTER)
            background_entry = tk.Entry(setname_level)
            background_entry.place(relx = 0.8,rely = 0.3,anchor = tk.CENTER)
            background_entry.insert(0,background)

            tk.Label(setname_level,text = 'Race').place(relx = 0.2,rely = 0.5,anchor = tk.CENTER)
            race_entry = tk.Entry(setname_level)
            race_entry.place(relx = 0.2,rely = 0.6,anchor = tk.CENTER)
            race_entry.insert(0,race)

            tk.Label(setname_level,text = 'Alignment').place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
            alignment_entry = tk.Entry(setname_level)
            alignment_entry.place(relx = 0.5,rely = 0.6,anchor = tk.CENTER)
            alignment_entry.insert(0,alignment)

            tk.Label(setname_level,text = 'XP Points').place(relx = 0.8,rely = 0.5,anchor = tk.CENTER)
            xp_entry = tk.Entry(setname_level)
            xp_entry.place(relx = 0.8,rely = 0.6,anchor = tk.CENTER)
            xp_entry.insert(0,xp_points)
            
            

            apply_button = tk.Button(setname_level,width = 10,text = 'Apply',command = apply_name)
            apply_button.place(relx = 0.4,rely = 0.8,anchor = tk.CENTER)

            close_button = tk.Button(setname_level,width = 10,text = 'Done',command = setname_level.destroy)
            close_button.place(relx = 0.6,rely = 0.8,anchor = tk.CENTER)
            

        def set_abs():
            nonlocal ab_scores
            nonlocal ab_modifiers

            def apply_abs():
                i = 0
                for ab in ab_scores:
                    ab_scores[ab] = (score_entries[i].get())
                    score_labels[i].config(text = ab_scores[ab])
                    ab_modifiers[ab] = (mod_entries[i].get())

                    temp = ''
                    if ab_modifiers[ab][0] != '-':
                        temp = '+'+str(ab_modifiers[ab])
                    else:
                        temp = ab_modifiers[ab]
                        
                    mod_labels[i].config(text = temp)
                    i+=1
                    
                
            setabs_level = tk.Toplevel(options_level)
            setabs_level.title('Change Ability Values')
            setabs_level.geometry('350x600')

            apply_button = tk.Button(setabs_level,width = 10,text = 'Apply',
                                     command = apply_abs)
            apply_button.place(relx = 0.25,rely = 0.05,anchor = tk.CENTER)
            
            done_button = tk.Button(setabs_level,width = 10,text = 'Done',
                                    command = setabs_level.destroy)
            done_button.place(relx = 0.75,rely = 0.05,anchor = tk.CENTER)

            tk.Label(setabs_level,text = 'Score').place(relx = 0.4,rely = 0.2,
                                                        anchor = tk.CENTER)
            tk.Label(setabs_level,text = 'Modifier').place(relx = 0.8,rely = 0.2,
                                                        anchor = tk.CENTER)
            score_entries = []
            mod_entries = []
            
            i = 0.3
            j = 0
            
            for ab in ab_scores:
                #Create Label
                tk.Label(setabs_level,text = ab).place(relx = 0.1,rely = i,
                                                       anchor = tk.CENTER)
                #Create Score Entry
                score_entries.append(tk.Entry(setabs_level))
                score_entries[j].place(relx = 0.4,rely = i,anchor = tk.CENTER)
                score_entries[j].insert(0,ab_scores[ab])
                
                #Create Modifier Entry
                mod_entries.append(tk.Entry(setabs_level))
                mod_entries[j].place(relx = 0.8,rely = i,anchor = tk.CENTER)
                mod_entries[j].insert(0,ab_modifiers[ab])
            
                i+=0.1
                j+=1

        def set_hp():

            nonlocal max_hp
            nonlocal initiative
            nonlocal speed
            nonlocal hit_dice

            def apply_hp():
                nonlocal max_hp
                nonlocal initiative
                nonlocal speed
                nonlocal hit_dice

                max_hp = int(maxhp_entry.get())
                hit_dice = hd_entry.get()

                initiative = initiative_entry.get()
                initiative_label.config(text = f'+{initiative}')

                speed = speed_entry.get()
                speed_label.config(text = speed)
                
                maxhp_label.config(text = f'Max hp: {max_hp}')
                hitdice_label.config(text = hit_dice)

                
                

            hp_level = tk.Toplevel(options_level)
            hp_level.title('Edit HP Stats')

            tk.Label(hp_level,text = 'Max HP:').pack()
            maxhp_entry = tk.Entry(hp_level)
            maxhp_entry.pack()
            maxhp_entry.insert(0,max_hp)

            tk.Label(hp_level,text = 'Initiative').pack()
            initiative_entry = tk.Entry(hp_level)
            initiative_entry.pack()
            initiative_entry.insert(0,initiative)

            tk.Label(hp_level,text = 'Speed').pack()
            speed_entry = tk.Entry(hp_level)
            speed_entry.pack()
            speed_entry.insert(0,speed)

            tk.Label(hp_level,text = 'Hit Dice:').pack()
            hd_entry = tk.Entry(hp_level)
            hd_entry.pack()
            hd_entry.insert(0,hit_dice)

            apply_button = tk.Button(hp_level,width = 15,text = 'Apply',command = apply_hp)
            apply_button.pack(pady = 5)

            tk.Button(hp_level,width = 15,text = 'Done',command = hp_level.destroy).pack()
        
        def set_skills():
            nonlocal ALL_SKILLS
            nonlocal skills
            nonlocal AB_NAMES
            nonlocal saving_throws
            nonlocal inspiration
            nonlocal prof_bonus

            #Whenever this issue arises, add a mainloop() statement

            checkbuttons_sk = []
            skbool_vars = []

            def apply_skills():
                nonlocal ALL_SKILLS
                nonlocal skills
                nonlocal skill_labels
                nonlocal sv_labels
                nonlocal passive_wisdom
                nonlocal inspiration
                nonlocal prof_bonus
                nonlocal passperc_label
                nonlocal insp_label
                nonlocal profb_label
                nonlocal skill_types_abs

                #Proficiencies
                temp = []
                for i in range(len(ALL_SKILLS)):
                    if skbool_vars[i].get():
                        temp.append(ALL_SKILLS[i])
                skills = temp
                
                i = 0
                for skill in ALL_SKILLS:
                    is_skill = skill + ': '
                    if skill in skills:
                        is_skill += f'[ X ] ({skill_types_abs[i]})'
                    else:
                        is_skill += f'[   ] ({skill_types_abs[i]})'
                    skill_labels[i].config(text = is_skill)
                    i+=1

                #Saving Throws
                temp = []
                for i in range(len(AB_NAMES)):
                    if stbool_vars[i].get():
                        temp.append(AB_NAMES[i])
                saving_throws = temp
                                    
                i = 0
                for sv in AB_NAMES:
                    is_sv = sv + ': '
                    if sv in saving_throws:
                        is_sv += '[ X ]'
                    else:
                        is_sv += '[   ]'
                    sv_labels[i].config(text = is_sv)
                    i+=1

                passive_wisdom = passwis_entry.get()
                passperc_label.config(text = f'Passive Wisdom: {passive_wisdom}')

                inspiration = inspiration_entry.get()
                prof_bonus = profb_entry.get()

                insp_label.config(text = f'Inspiration: {inspiration}')
                profb_label.config(text = f'Proficiency Bonus: +{prof_bonus}')
                
                    

                


            setskills_level = tk.Toplevel(options_level)
            setskills_level.title('Edit Skills')
            setskills_level.geometry('600x600+200+300')
            
            checkbuttons_sk = []
            skbool_vars = []

            checkbuttons_st = []
            stbool_vars = []

            
            
            j = 0.05
            for i in range(len(ALL_SKILLS)):
                #Skill Checkbuttons
                boolvar = tk.BooleanVar(setskills_level)
                cb = tk.Checkbutton(setskills_level,onvalue = True,offvalue = False,text = ALL_SKILLS[i],variable = boolvar)
                skbool_vars.append(boolvar)
                checkbuttons_sk.append(cb)
                checkbuttons_sk[i].place(relx = 0.1,rely = j,anchor = tk.W)
                if ALL_SKILLS[i] in skills:
                    skbool_vars[i].set(True)
            
                
                #Saving Throws Checkbuttons
                if i < len(AB_NAMES):
                    boolvar = tk.BooleanVar(setskills_level)
                    cb = tk.Checkbutton(setskills_level,text = AB_NAMES[i],
                                    variable = boolvar)
                    stbool_vars.append(boolvar)
                    checkbuttons_st.append(cb)
                    checkbuttons_st[i].place(relx = 0.8,rely = j,anchor = tk.W)
                    if AB_NAMES[i] in saving_throws:
                        stbool_vars[i].set(True)

                j+=0.05

                 
            tk.Label(setskills_level,text = 'Skills').place(relx = 0.1,rely = 0.95,anchor = tk.W)
            tk.Label(setskills_level,text = 'Saving Throws').place(relx = 0.8,rely = 0.35,anchor = tk.W)

            #Passive Wisdom

            passwis_entry = tk.Entry(setskills_level)
            passwis_entry.place(relx = 0.775,rely = 0.5,anchor = tk.W)
            passwis_entry.insert(0,passive_wisdom)
            tk.Label(setskills_level,text = 'Passive Wisdom').place(relx = 0.6,rely = 0.5,anchor = tk.W)

            #Inspiration

            inspiration_entry = tk.Entry(setskills_level)
            inspiration_entry.place(relx = 0.775,rely = 0.6,anchor = tk.W)
            inspiration_entry.insert(0,inspiration)
            tk.Label(setskills_level,text = 'Inspiration').place(relx = 0.6,
                                                                 rely = 0.6,anchor = tk.W)


            #Proficiency Bonus
                
            profb_entry = tk.Entry(setskills_level)
            profb_entry.place(relx = 0.775,rely = 0.7,anchor = tk.W)
            profb_entry.insert(0,prof_bonus)
            tk.Label(setskills_level,text = 'Proficiency Bonus').place(relx = 0.6,
                                                                       rely = 0.7,anchor = tk.W)
                                

            apply_button = tk.Button(setskills_level,width = 10,text = 'Apply',command = apply_skills)
            apply_button.place(relx = 0.5,rely = 0.85,anchor = tk.CENTER)

            tk.Button(setskills_level,width = 10,text = 'Done',
                      command = setskills_level.destroy).place(relx = 0.5,rely = 0.9,anchor = tk.CENTER)
            
            setskills_level.mainloop()

        def set_html():
            

            def apply_html():
                nonlocal html_file

                html_file = html_entry.get()

            html_level = tk.Toplevel(options_level)
            html_level.title('Set HTML FIle Address')

            html_entry = tk.Entry(html_level)
            html_entry.pack()
            html_entry.insert(0,html_file)

            apply_button = tk.Button(html_level,width = 15,text = 'Apply',command = apply_html)
            apply_button.pack()

            done_button = tk.Button(html_level,width = 15,text = 'Done',command = html_level.destroy)
            done_button.pack()

            

            
        
        options_level = tk.Toplevel(root)
        options_level.title('Options')
        options_level.geometry('350x600')

        tk.Label(options_level,text = 'Change Variables').pack()

        changeab_button = tk.Button(options_level,width = 15,text = 'Edit Abilities',command = set_abs)
        changeab_button.pack()

        changename_button = tk.Button(options_level,width = 15,text = 'Edit Nameplate',command = set_name)
        changename_button.pack(pady = 5)

        changehp_button = tk.Button(options_level,width = 15,text = 'Edit HP Bar',command = set_hp)
        changehp_button.pack(pady = 5)

        changeskills_button = tk.Button(options_level,width = 15,text = 'Edit Skills',command = set_skills)
        changeskills_button.pack(pady = 5)

        changehtml_button = tk.Button(options_level,width = 15,text = 'Edit HTML Address',command = set_html)
        changehtml_button.pack(pady = 5)

        

        tk.Label(options_level,text = '').pack()
        close_button = tk.Button(options_level,width = 15,text = 'Close',command = options_level.destroy)
        close_button.pack()

       

        

    options_button = tk.Button(root,text = 'Options',width = 10,height = 2 ,command = open_options)
    options_button.place(relx = 0.75,rely = 0.9,anchor = tk.CENTER)

    '''End of Options'''
    
    '''Background Processes'''
    
    #This is where to put all of the routine events, such as updating text widgets and their variables
    #KEEP THIS AT THE BOTTOM
    def one_clock():
        pass
        root.after(1000,one_clock)
        
    
    def five_clock():
        nonlocal other_skills
        other_skills = str(lang_text.get('1.0',tk.END))
        apply_weapons()
        apply_inventory_nums()
        update_personality()
        try:
            root.after(5000,five_clock)
        except Exception:
            pass
            

    def ten_clock(): 
        pass
    
        root.after(10000,ten_clock)

    '''End of Background Processes'''
    
    '''Save and Quit Buttons'''
    def save():
        nonlocal other_skills
        other_skills = str(lang_text.get('1.0',tk.END))
        apply_weapons()
        apply_inventory_nums()
        update_personality()
        write()
            
    after_id = None
    
    def attempt_quit():

        def save_quit():
            save()
            root.after_cancel(after_id)
            root.destroy()
            
        def nosave_quit():
            root.after_cancel(after_id)
            root.destroy()
            
        
        quit_toplevel = tk.Toplevel(root)
        quit_toplevel.title('Exit and Save?')
        tk.Label(quit_toplevel,text = 'Save Data?').pack()
        tk.Button(quit_toplevel,width = 10,text = 'Yes',command = save_quit).pack()
        tk.Button(quit_toplevel,width = 10,text = 'No',command = root.destroy).pack()
        tk.Button(quit_toplevel,width = 10,text = 'Cancel',command = quit_toplevel.destroy).pack()
        
    save_button = tk.Button(root,width = 10,height = 2,text = 'Save',command = save)
    save_button.place(relx = 0.83,rely = 0.875,anchor = tk.CENTER)

    quit_button = tk.Button(root,width = 10,height = 2,text = 'Quit',command = attempt_quit)
    quit_button.place(relx = 0.83,rely = 0.925,anchor = tk.CENTER)

    '''End of Save and Quit Buttons'''

    try:
        after_id = root.after(5000,five_clock)
    except Exception:
        pass

    root.mainloop()
    
    

    


if __name__ == '__main__':

    print('Executing Main')
    
    #main('Jose-Santiano.txt')
    main('Vedmid.txt')
    
