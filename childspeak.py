from enum import unique
import json
from tokenize import group


## Variables

initial_path="interview"
vowels_list = ["a","e","i","o","u","y"]


##Import JSON
with open(initial_path + '/example_big_input.json') as f:
    data = json.load(f)
    #print(data)

#empty

fileempty = open(initial_path + "/output.txt", 'r+')
fileempty.truncate(0)

filempty = open(initial_path + "/final_output.txt", 'r+')
#filempty.truncate(0)

def first_consonent(word):
    fst_cons =""
    for aplhabet in word:
        if aplhabet not in vowels_list:
            fst_cons = aplhabet
            break
    return fst_cons



for word in data.get("input_data",""):
    first_cons = ""
    group_cons = ""
    first_vowel = ""
    group_vowel = ""
    last_grp_vowel = ""
    last_vowel = ""
    new_word = ""
    last_vowel_index = 0
    tmp_word = ""
    with open(initial_path + "/output.txt", "a") as text_file:
        for i in range(len(word)):   
            if i == 0 and word[0] not in vowels_list:
                first_cons = word[0]
                new_word = new_word + first_cons
                continue
            if i == 0 and word[0] in vowels_list:
                first_vowel = word[0]
                first_cons = str(first_consonent(word)) 
                new_word = new_word + first_cons + first_vowel
                continue
            if word[i] not in vowels_list and word[i-1] not in vowels_list:
                new_word = new_word[:-1]
                new_word = new_word + first_cons
                continue
            if word[i] in vowels_list and word[i-1] in vowels_list:
                last_grp_vowel = word[i]
                new_word = new_word[:-1]
                new_word = new_word + last_grp_vowel
                continue
            if word[i] not in vowels_list:
                new_word = new_word + first_cons
                continue
            if i != 0 and word[i] in vowels_list:
                sub_word=word[i:]
                for j in range(len(sub_word)):
                    if sub_word[j] in vowels_list:
                        last_vowel = sub_word[j]
                        last_vowel_index = j
                if word[i] == last_vowel and i == last_vowel_index+i:
                    new_sub_word = sub_word[:last_vowel_index+1]
                    new_word = new_word + new_sub_word
                    break
                else:
                    new_word = new_word + word[i]
                    
        text_file.write(new_word+"\n")

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

with open(initial_path + '/output.txt', "r") as tf:
    processed_data = tf.read().split('\n')
    #print(str(processed_data))

with open(initial_path + "/final_output.txt", "a") as text_file:
    unique_processed_word = set(list(filter(None, processed_data)))
    for process_word in unique_processed_word:
        text_file.write(process_word +"-"+str(countX(processed_data,process_word))+"\n")
    



            
        
