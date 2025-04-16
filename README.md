# file-and-exception-in-python

A File and Exception Python Code that interacts with the user and 


 # File and Exception Handling in Python
 This Python script demonstrates how to handle file operations and exceptions.
 ## Overview           
 This script reads a file, writes to a file, and handles file not found errors.
 ## Features
 - Reads content from a specified file.
 - If the file is not found, prompts the user to create it.
 - Writes user-provided content to the file.
 - Handles IO errors gracefully.
 ## Usage
 1. Run the script.
 2. Enter the file name when prompted.
 3. If the file exists, its content will be displayed.
 4. If the file does not exist, you will be prompted to create it.
 5. Enter the content you want to write to the file.
 ## Example
 ```python
# fileName = input("Enter the file name: ")
# try:
#     with open(fileName, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("\nThe file was not found.\nWould you like to create it? (y/n)")
#     response = input()
#     if response == 'y':
#         with open(fileName, 'w') as file:
#             print("File created successfully.")
#             user_content = input("Enter the content to write to the file: ")
#             file.write(user_content)
#             print("Content written successfully.")
#     else:
#         print("\nGoodBye!")
# except IOError:
#     print("An error occurred while reading the file.")
# finally:
#     file.close()
#     print("File closed.")
```   
## Conclusion
This script provides a simple way to handle file operations and exceptions in Python. It demonstrates how to read from and write to files while gracefully handling errors.

# Author 
 ## Oluwajoba Enoch Imisioluwa