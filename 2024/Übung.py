#import pandas as pd
# class Aufgabe:
#     def __init__(self, titel, prioritaet="mittel"):
#         self.titel = titel
#         self.erledigt = False
#         self.prioritaet = prioritaet

#     def erledigen(self):
#         self.erledigt = True

#     def __str__(self):
#         status = "✓" if self.erledigt else "✗"
#         return f"{self.titel} [{status}] - Priorität: {self.prioritaet.capitalize()}"

# # Beispiel-Aufgabenliste
# aufgaben = [
#     Aufgabe("Einkaufen", "hoch"),
#     Aufgabe("Python lernen", "mittel"),
#     Aufgabe("Wäsche waschen", "niedrig")
# ]

# # Eine Aufgabe erledigen
# aufgaben[0].erledigen()

# # Ausgabe
# for a in aufgaben:
#     print(a)


# max = {"test" : [1,2,3,4,5]}

# test1 = max["test"][0:3]
# test2  = max.get("test")[:2]
# print(test2)


# class Solution(object):
#     def isMatch(self, text: str, pattern: str) -> bool:
#         if not pattern:
#             return not text

#         first_match = bool(text) and pattern[0] in {text[0], "."}

#         if len(pattern) >= 2 and pattern[1] == "*":
#             return (
#                 self.isMatch(text, pattern[2:])
#                 or first_match
#                 and self.isMatch(text[1:], pattern)
#             )
#         else:
#             return first_match and self.isMatch(text[1:], pattern[1:])


# class Solution:
#     def longestCommonSubsequence(self, original: str, sub: str) -> int:
#         len_sub = len(sub)
#         len_original = len(original)

#         count = 0
#         for j in range(len_original):
#             i = 0
#             for i in range(len_sub):
#                 if original[j] == sub[i]:
#                     count +=1
#                 else:
#                     None
                    
#         return count
                

# obj = Solution()
# test = obj.longestCommonSubsequence("ezupkr", "ubmrapg")
# print(test)


#test = "ubmrapg"
# for test in range(5):
#     print(test)



# l = [[0] * (len(test)) for i in range((len(test)))]
# print(l)


# t = ["k" for i in test]
# print(t)

# class Solution:
#     def longestCommonSubsequence(self, original: str, sub: str) -> int:
#         # Get the lengths of both input strings
#         len_original, len_sub = len(original), len(sub)
      
#         # Initialize a 2D array (list of lists) with zeros for dynamic programming
#         # The array has (len_original + 1) rows and (len_sub + 1) columns
#         dp_matrix = [[0] * (len_sub + 1) for _ in range(len_original + 1)]
        
#         # Loop through each character index of text1 and text2
#         for i in range(1, len_original + 1):

#             for j in range(1, len_sub + 1):
#                 # If the characters match, take the diagonal value and add 1
#                 if original[i - 1] == sub[j - 1]:
                    
#                     dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                    
#                 else:
#                     # If the characters do not match, take the maximum of the value from the left and above
                    
#                     dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])
      
#         # The bottom-right value in the matrix contains the length of the longest common subsequence
#         return print(dp_matrix)#[len_original][len_sub]
    
# obj = Solution()
# test = obj.longestCommonSubsequence("ezupkr", "ubmrapg")
# print(test)


# listen= [[1, 4, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0]]
# a = listen[1]
# a[1]
# gleich schreibweise wie davor nur das die Liste einer Variable zugeordnet wird 
#print(listen[1:3][1])

# df = pd.DataFrame(listen)
# print(df[1][0])

# finde die zwei Indizes die in Summe 'target ergeben'
# nums = [8,2,11,7]
# target = 9

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#             else:
#                 continue
        
# print(twoSum(nums, target))

# find the median
# nums1 = [1,3] 
# nums2 = [2,4]


# merge_array = nums1 + nums2
# merge_array.sort()
# n = len(merge_array)

# if n%2 == 1:
#     print(merge_array[n//2])
# else:
#     print((merge_array[n//2-1]+merge_array[n//2])/2)


# nums1 = [1,2,2,1]
# nums2 = [2,2]

# hash_map = {}

# for i in nums1:
#     if i in hash_map:
#         hash_map[i] +=1
#     else:
#         hash_map[i] = 1

# result = []

# for i in nums2:
#     if i in hash_map and hash_map[i] > 0:
#         result.append(i)
#         hash_map[i] -= 1
#     else:
#         None

# print(result)

# nums = [3,2,4]

# target = 6


# hash_map = {}
# for i, num in enumerate(nums):
#     complement = target - num
#     if complement in hash_map:
#         print([hash_map[complement], i])
#         break  # Nur eine Lösung erlaubt
#     hash_map[num] = i

# print(hash_map[3] = 1)


# mein_dict = {}
# mein_dict[3] = 0

# print(mein_dict)

# meine_liste = [42]
# meine_liste[0] = 43

# print(meine_liste)


# users = {"user_id": 1, "name":"max"}


# for key, value in users.items():
#     print(value)

# users = {
#     "GruppeA":[{"user": {"user_id" : 1, "screen_name" : "maximus" }, "name":"max"}, {"user": {"user_id" : 2, "screen_name" : "luposa" }, "name":"luisa"}],
#     "GruppeB":[{"user": {"user_id" : 3, "screen_name" : "anus_maximus" }, "name":"maxi"}]
#     }
# list_dict = []
# for key, value in users.items():
#     for i in value:
#         neues_dict = {
#                     "user_id": i["user"]["user_id"],
#                     "user":i["user"]["screen_name"], 
#                     "Gruppe": key,
#                     "name": i["name"]
#                     }
#         list_dict.append(neues_dict)



# df = pd.DataFrame(list_dict)
# df["email"] = df["user"]+"@outlook.com"
# print(df[df["Gruppe"] == "GruppeA"])
#df.loc[df["Gruppe"]=="GruppeA", "Gruppe"] = "GruppeC"

# numbers = [2,7,11,15]
# target = 9

# dict = {}
# for num in numbers:
#     if num in dict:
#         dict[num] +=1
#     else:
#         dict[num] = 1

# print(dict)

#hash_map = {}
# for i in nums1:
#     if i in hash_map:
#         hash_map[i] +=1
#     else:
#         hash_map[i] = 1


# class Cat:
#     species = 'mamal'
#     def __init__(self):
#         self.set_dict = {}

#     def set_content(self, name, age):
#         self.set_dict['name'] = name
#         self.set_dict['age'] = age 
#         return self.set_dict

# cat1 = Cat()

# print(cat1.set_content('peter', 3))

# nums = [0,0,1,1,1,2,2,3,3,4]

# len_nums = len(nums)
# nums_unique = sorted(set(nums))
# len_nums_unique = len(nums_unique)


# for i in range(len_nums_unique):
#     nums[i] = nums_unique[i]



    
# print(len_nums_unique, nums)

# i = 1

# for j in range(1, len(nums)):
#     if nums[j] != nums[i - 1]:
#         nums[i] = nums[j]
#         i += 1

# print(nums)


# s = "([])"
# len_s = len(s)
# def valid_string():
#     valid = ("()","[]","{}","([])")
#     i = 1
#     for i in range(1, len_s):
#         if f"{s[i-1]}{s[i]}" in valid:
#             print(f"{s[i-1]}{s[i]}")
#             return True
        
#     return False
       

# print(valid_string())



# def isValid(self, s: str) -> bool:
#         mapping = {')': '(', '}': '{', ']': '['}
#         stack = []

#         for char in s:
#             if char in mapping.values():
#                 stack.append(char)
#             elif char in mapping:
#                 if not stack or mapping[char] != stack.pop():
#                     return False
#         return not stack


#------------------ADVENT CODING CHALLANGE----------------------------------
import requests
import os
import re
#------------------Start API für Input Daten----------------------------------
# url = "https://adventofcode.com/2024/day/1/input"
# cookies = {"session": "53616c7465645f5f1221dea191ab35dc09e6129ecd5c7dcc651c455b0af8d4a2a0e1dc534a0126d519370232e17f0f0d0a6bdc41c0680e9686f5410386be796b"}
# response = requests.get(url, cookies=cookies)

# with open(os.path.join(os.path.dirname(__file__)  , 'data/input.txt'),'w') as file:
#     file.write(response.text)
#------------------Ende API für Input Daten----------------------------------

# liste1 = []
# liste2 = []

# with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as file:
#     for line in file:
#         a, b = map(int, line.strip().split())
#         liste1.append(a)
#         liste2.append(b)

#------------------Jahr 2024 Aufgabe 1 Part 1---------------------------------------

# liste1 = [3, 4, 2, 1, 3, 3]
# liste2 = [4, 3, 5, 3, 9, 3]



# sorted_liste1= sorted(liste1)
# sorted_liste2 = sorted(liste2)

# diff = [abs(sorted_liste2[i] - sorted_liste1[i]) for i in range (len(sorted_liste1))]
# print(sum(diff))

#------------------Jahr 2024 Aufgabe 1 Part 2---------------------------------------

# set_list = []
# for i in liste1:
#     counter = 0
#     if i in liste2:
#         counter +=1
#     set_list.append(counter * i)


# result = sum(i * liste2.count(i) for i in liste1)
# print(result)

#------------------Jahr 2024 Aufgabe 2 Part 1 & 2---------------------------------------

# with open(os.path.join(os.path.dirname(__file__), 'data/input_reports.txt'), 'r') as file:
#     reports = [list(map(int, line.split())) for line in file]



# safe_differ = 3

# list_of_safe_reports = [
#     1 if (report == sorted(report) or report == sorted(report, reverse=True)) and
#          all(0 < abs(report[i] - report[i+1]) <= safe_differ for i in range(len(report)-1))
#     else 0
#     for report in reports
# ]

# print(sum(list_of_safe_reports))

# safe_differ = 3

# list_of_safe_reports = []

# for report in reports:
#     for j in range(len(report)):
#         temp_report = report.copy()
#         rem_element = temp_report.pop(j)  # Entfernt das letzte Element

#         if (temp_report == sorted(temp_report) or temp_report == sorted(temp_report, reverse=True)) and
#         all(0 < abs(temp_report[i] - temp_report[i+1]) <= safe_differ for i in range(len(temp_report)-1)):
#             list_of_safe_reports.append(1)
#             break
#         else:
#             list_of_safe_reports.append(0)


# print(sum(list_of_safe_reports))



#------------------Jahr 2024 Aufgabe 3 Part 1 & 2---------------------------------------

with open(os.path.join(os.path.dirname(__file__), 'data/corrupted_memory.txt'), 'r') as file:
    corrupted_memory = [zeile for zeile in file]


# suchwert = r'mul\((\d+),(\d+)\)'
tokens = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"
set_liste = []
enabled = True
part2 = 0
for zeile in corrupted_memory:
    for token in re.findall(tokens,zeile):
        if token[0] == "do()": 
            enabled = True
        elif token[1] == "don't()":
            enabled = False 
        elif isinstance(token, tuple)  and enabled == True:
            nums_of_mul =  int(token[2])*int(token[3])
            part2 += nums_of_mul

print(token)

# for zeile in corrupted_memory:
#     for token in re.findall(tokens,zeile):
#         print(token[0] == "do()")



        