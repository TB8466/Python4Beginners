l = ["fem","fede","flade","flødeboller", "på"]

def sort_by_last_letter(lst):
    return lst[-1]
#sort alphabetically by last letter
print(sorted(l, key=sort_by_last_letter))

def sort_by_lenght(lst):
    return len(lst)
#sort by length of each word
print(sorted(l, key=sort_by_lenght))

