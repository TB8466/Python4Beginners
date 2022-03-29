#Mandatory assignment for 17-02-2022

#1
#Model an organisation of employees, management and board of directors in 3 sets.
import re


board = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

print(board.difference(employees))                              # who in the board of directors is not an employee?
print(board.intersection(employees))                            # who in the board of directors is also an employee?
print(len(management.intersection(board)))                      # how many of the management is also member of the board?
print(management.intersection(employees))                       # All members of the managent also an employee
print(management.intersection(board))                           # All members of the management also in the board?
print(board.intersection(management).intersection(employees))   # Who is an employee, member of the management, and a member of the board?
print(employees.difference(management).difference(board))       # Who of the employee is neither a memeber or the board or management?

#2
#Using a list comprehension create a list of tuples from the folowing datastructure
dictonary = {
    "a": "Alpha",
    "b": "Beta",
    "g": "Gamma"}

print(dictonary["a"])
lst = []

for x in dictonary:
    turple = ()
    lst.append(tuple(dictonary[x]))

print(lst)
#Not quite sure I understood this assignment?

#3
#From these 2 sets:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
#Of the 2 sets create a:

print(set1.union(set2)) #Union
print(set1.symmetric_difference(set2)) #Symmetric difference
print(set2.difference(set1)) #Difference
print(set1.isdisjoint(set2)) #Disjoint

#4
#Date Decoder
date = "8-MAR-85"

dateDecoder = {
    "JAN" : "01",
    "FEB" : "02",
    "MAR" : "03",
    "APR" : "04",
    "MAY" : "05",
    "JUN" : "06",
    "JUL" : "07",
    "AUG" : "08",
    "SEP" : "09",
    "OKT" : "10",
    "NOV" : "11",
    "DEC" : "12",
}
def decodeMonth(date):
    lst = date.split("-")
    tpl = ("0"+lst[0], dateDecoder[lst[1]], "19"+lst[2])
    return tpl

print(decodeMonth(date))