import csv
import pandas
fileURL="Day-26-NATO AlphabetProject/nato_phonetic_alphabet.csv"
name=input("Please Write Your Name:").upper()
with open(fileURL) as data:
    rows= data.readlines()
    for row in rows:
        elements = row.strip().split(',')
        # print(elements)
keyValuePair2={}
with open(fileURL) as file:
    rows= csv.reader(file)
    for row in rows:
        if row:
            key,value=row
            keyValuePair2[key]=value

# print(keyValuePair2)

dataPanda=pandas.read_csv(fileURL)
# print(dataPanda.to_dict())
phonetic_dict={row.letter:row.code for(index,row) in dataPanda.iterrows()}
print(phonetic_dict)
Names=[phonetic_dict[letter] for letter in name]
print(Names)


