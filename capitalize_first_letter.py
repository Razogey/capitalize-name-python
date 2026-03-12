name = input(">> Please Enter Your Name: ")
char_list = []

def convert_to_list(name):
    for char in name:
        char_list.append(char)
        
def capitalize_first_letter(char_list):
    for i in range(len(char_list)):
        if i == 0 or char_list[i-1] == ' ':
            char_list[i] = char_list[i].upper()

def convert_to_string(char_list):
    result = ''
    for char in char_list:
        result += char
    return result

convert_to_list(name)
capitalize_first_letter(char_list)
capitalized_name = convert_to_string(char_list)
print(capitalized_name)