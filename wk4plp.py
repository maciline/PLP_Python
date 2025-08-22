def modify_content (content):
    # Example:Make all text uppercase
    return content.upper()

try:
    #Ask user for the input filename
    input_filename = input("Enter the name of the file to read:")

    #Try to open and read the file
    with open(input_filename, 'r') as infile:
        original_content = infile.read()

    #Modify the content
    modified_content = modify_content(original_content)

    #Create a new filename for the output
    output_filename = "modified_" + input_filename

    #Write the modified content to the new file
    with open(output_filename, 'w') as outfile:
         outfile.write(modified_content)

    print(f"File modified aand saved as '{output_filename}'") 

except FileNotFoundError:
    print("X Error: The file does not exist.Please check the filename and try again!") 
except IOError:
      print("X Error: The file could not be read or written.Check permission or file status!") 




