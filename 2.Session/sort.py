l = ["fem","fede","flade","flødeboller", "på"]

def sort_by_last_letter(str):
    return str[-1]
#sort alphabetically by last letter
print(sorted(l, key=sort_by_last_letter))

def sort_by_lenght(str):
    return len(str)
#sort by length of each word
print(sorted(l, key=sort_by_lenght))