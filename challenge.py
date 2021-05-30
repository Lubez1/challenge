import pandas as pd
data = pd.read_csv("data.csv")
new_data = data.loc[data["last_name"] != "Test"] #odstranění řádků s testovacími hodnotami

#Number of mentees
print("Number of mentees is: ", len(new_data)) #97 mentees

#Set of all languages
languages = new_data.language
def uniq(languages):
      myset = set(languages)
      unique = list(myset)
      for x in unique:
              print(x)
print("All languages are: ")
uniq(languages)

first_name = (new_data.first_name).str.replace(" ", "")
last_name = (new_data.last_name).str.replace(" ", "")
full_name = (first_name+last_name)
#print(full_name)

#Average lenght of full names
res = sum(map(len, full_name))/float(len(full_name))
print("The Average length of mentees full names is: " + str(res))

#for item in full_name:
    #print(item+str(len(item)))

#The longest and shortest full name
longest_name = max(full_name, key=len)
print("The Longest name is: " + longest_name)

shortest_name = min(full_name, key=len)
print("The Shortest name is: " + shortest_name)

new_data.to_json("new_data.json")

