
# def copy_and_reverse(fileName1,fileName2):
    
#     with open(fileName1,'r') as file1:
#         data = file1.read()
        
#     with open(fileName2,'w') as file2:
#         file2.write(data[::-1])
        
        
# copy_and_reverse("story2.txt","story3.txt")

# '''
# find_and_replace('story.txt', 'Alice', 'Colt') 
# # story.txt now contains the first chapter of my new book,
# # Colt's Adventures in Wonderland
# '''

# def find_and_replace(file_name,origWord,replaceWord):
#     with open(file_name,'r+') as f:
#         data = f.read()
#         data =data.replace(origWord,replaceWord)     
#         f.seek(0)
#         f.write(data)    

# find_and_replace('story.txt','Alice','Sand')


'''

CSV Reader 
'''

from csv import reader


# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")


# '''
# Making a list from the csv_reader iterator
# '''
# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     data  = list(csv_reader)
#     print(data)

'''
Using DICT READER
'''


# from csv import DictReader

# with open('fighters.csv') as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(row['Name'] + " FROM " + row['Country'])


# '''
# Writer
# '''
# from csv import writer

# with open('cats.csv','w') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name","Age"])
#     csv_writer.writerow(["Blue","3"])
#     csv_writer.writerow(["Kitty","1"])
        
'''
READ FROM ONE CSV
CAPITALIZE 
WRITE TO ANOTHER CSV
'''

# from csv import reader,writer

# with open('fighters.csv','r') as file:
#     csv_reader = reader(file)
#     fighters = [ [item.upper() for item in row] for row in csv_reader]
#     # for row in csv_reader:
#     #     fighters = [item.upper() for item in row]
#     #     print(fighters)
        
# # print(fighters[0])
# with open("scream_fighters.csv","w") as file_1:
#     csv_writer = writer(file_1)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)
#         print(fighter)


# ''' METHOD 2 '''

# from csv import reader,writer

# with open('fighters.csv','r') as file:
#     csv_reader = reader(file)
#     with open("scream_fighters_1.csv","w") as file_1:
#         csv_writer = writer(file_1)
#         for fighter in csv_reader:
#             csv_writer.writerow([s.upper() for s in fighter])


''' DICTWRITER '''


# from csv import writer, DictWriter
# with open('cats1.csv','w') as file:
#     headers = ["name","breed","age"]
#     csv_writer = DictWriter(file, fieldnames = headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "name":"Garfield",
#         "breed":"Orange Tabby",
#         "age": 10
#     })


# from csv import DictReader,DictWriter

# def cm_to_in(cm):
#     return cm*0.39371


# with open("fighters.csv","r") as file:
#     read_csv= DictReader(file)
#     fighters = (list(read_csv))
#     print(fighters)

# with open("inches_fighters.csv","w") as file:
#     headers = ["Name","Country","Height"]
#     csv_writer = DictWriter(file, fieldnames = headers)
#     csv_writer.writeheader()
#     for f in fighters:
#         csv_writer.writerow({

#             "Name": f['Name'],
#             "Country":f['Country'],
#             "Height": cm_to_in(int(f["Height (in cm)"]))
#         })


''' Append to USERS.CSV '''


# def add_user(firstName,lastName):
#     from csv import reader,writer
#     with open("users.csv","a") as file:
#         csv_writer = writer(file)
#         csv_writer.writerow([firstName,lastName])


# add_user("Sand","Nc")
# add_user("Michael","Ricks")  
# add_user("Richard","Choy") 
# add_user("Esmaeel","Masserrat")


'''
'''