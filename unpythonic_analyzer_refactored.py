# unpythonic_analyzer.py

def analyze_text(file_name):
    # This function is full of bad practices.
    
    with open(file_name, 'r') as the_file:
        the_text_content = the_file.read()
    
    my_list = the_text_content.lower().split()
    
    # Let's count the occurrences of each word.
    word_count_dict = {}
    
    for word_item in my_list:
        if word_item in word_count_dict:
            word_count_dict[word_item] = word_count_dict[word_item] + 1
        else:
            word_count_dict[word_item] = 1
    
    # Use a list comprehension to find words with more than 3 characters.
    long_words = [word_item for word_item in my_list if len(word_item) > 3] 
            
    print("The total number of words is: " + str(len(my_list)))
    print("The unique words count is: " + str(len(word_count_dict)))
    print("The most frequent words are:")
    
    for word, count in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"'{word}': {count}")
    
   
    print(f"Long words (more that 3 characters): {len(long_words)}")

# create a text file named 'sample.txt' for testing.
analyze_text("sample.txt")