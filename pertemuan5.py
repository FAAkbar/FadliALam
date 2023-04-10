# IMPORT DATETIME
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))
# print(x)
# print(x.strftime('%d/%m/%Y'))

# MENGURUTKAN BILANGAN TERBESAR DAN TERKECIL
# arr_s = [5, 78, 2, 0]
# assert(min(arr_s)) == 0
# assert(max(arr_s)) == 78


# FUNCTION 5 PANGKAT 5
# assert(pow(5, 5)) == 3125

# PYTHON TRY EXCEPT
#   try:
#   f = open("demofile.txt")
#     try:
#       f.write("lorem ipsum")
#     except:
#         print("sometime what wrong when wrong writing to the file")
#     finally:
#         f.close()
#     except:
#       print("Sometime about the text")
# try:
#     print(x)
# except:
#     print("something went wrong")
# finally:
#     print("the try exserces is wrong")


#PYTHON JSON
# import json
# x = '{"name":"Jhon", "age"}:30, "city":"New york"'
# y = json.loads(x)
# print(y["age"])

# import json
# x = {
#         "name": "Jhon",
#         "age": 30,
#         "city": "New york"
# }
# y = json.dumps(x)
# print(y)

# FILE HANDLING
# f = open("demofile.txt", "rt")
# print(f.read())

# FILE WRITE
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
# f = open("demofile2.txt", "r")
# print(f.read())

# DELETE A FILE
# import os
# os.remove("demofile2.txt")

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# DELETE FOLDER
# import os
# os.rmdir("Myfolder")

# 1. open file & read
# f = open('./json_read.txt')

# json_string = f.read()

# print(json_string)

# 2. Loads

# json_dict = json.loads(load_string)
# print(json_dict)
# print(type(json_dict))
# print(json_dict['name'])

# users = {
#     'email': "smkn 1 kawali",
#     'password': "123"
# }

# 1. Dump

# json_string = json.dump(users)

# 2. open file & write
# f = open('./json_read.txt', 'w')

# f.write(json_string)

# f.close()

# import json 

# def write_to_file(file, data):
#     json_string = json.dumps(data)

#     f = open(file, 'w')
#     f.write(json_string)
#     f.close()

# def read_file(file, mode='r'):

#     try:
#         f = open(file, mode=mode)
#         json_string = f.read()
#         json_dict = json.loads(json_string)
#         f.close()

#     except:
#         return False
    



# Tambahkan function / module untuk menyimpan users dan transaction ke file
