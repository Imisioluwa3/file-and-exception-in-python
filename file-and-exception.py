# try:
#     with open('file.txt', 'r') as file:
#         content = file.read()
#         # print(content)
#         with open('file.txt', 'w') as file:
#             file.write("New content, not meant for the babies of the house, but for the adults.")
#             print("File name:", file.name, "was modified")
# except FileNotFoundError:
#     print("The file was not found.")
    
    
    
    
fileName = input("Enter the file name: ") 
try: 
    with open(fileName, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("\nThe file was not found.\nWould you like to create it? (y/n)")
    response = input()
    if response == 'y':
        with open(fileName, 'w') as file:
            print("File created successfully.")
            user_content =input("Enter the content to write to the file: ")
            file.write(user_content)
            print("Content written successfully.")
    else:
        print("\nGoodBye!")
except IOError:
    print("An error occurred while reading the file.")
    
finally:
    file.close()
    print("File closed.")
    
    