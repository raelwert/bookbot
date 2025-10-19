def sort_on(items):
     return items["num"]

def count_words(file_contents):
     word_list = file_contents.split()
     return len(word_list)

def count_characters(file_contents):
     file_contents = file_contents.lower()
     char_count = {}
     for char in file_contents:
          if(char_count.get(char) is None):
               char_count[char] = 1
          else:
               char_count[char] = char_count[char] + 1
    
     return char_count

def dict_to_sorted_list(char_count):
     char_list = []
     for key in char_count:
          char_list.append({"char": key, "num": char_count[key]})
     char_list.sort(reverse=True, key=sort_on)
     return char_list