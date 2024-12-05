def main():
    file_contents = read_file('books/frankenstein.txt')
    word_count = count_words(file_contents)
    character_list = count_characters(file_contents)
    generate_report('books/frankenstein.txt', word_count, character_list)

def read_file(filepath):
    
    with open(filepath) as f:
        return f.read()

def count_words(file_contents):
    word_counter = 0
    words = file_contents.split()
    for word in words:
        word_counter += 1
    return word_counter  

def sort_on(char_dict):
    return char_dict["count"]

def count_characters(file_contents):
    character_dict = {}
    for char in file_contents.lower():
        if char.isalpha():  
            if char not in character_dict:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
    character_list = [{'character': char, 'count': count} for char, count in character_dict.items()]
    character_list.sort(reverse=True, key=sort_on)
    return character_list  

def generate_report(file_path, word_count, character_list):
    
    report = f"--- Begin report of {file_path} ---\n"
    report += f"{word_count} words found in the document\n\n"

    for char_info in character_list:
        report += f"The '{char_info['character']}' character was found {char_info['count']} times\n"


    report += "--- End report ---"

    print(report)
    return report

main()
