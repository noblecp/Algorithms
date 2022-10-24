import copy
from english_words import english_words_set
from colorama import Fore, Style

letters = input("Enter letters: ").strip()
numNodes = len(letters)
adjMatrix = [[1 for _ in range(numNodes)]for _ in range(numNodes)]
nodeToNum = {letter : i for i, letter in enumerate(letters)}
numToNode = {i : letter for i, letter in enumerate(letters)}

def dfs(node, adjMatrix, visited, solution, path):
    
    # "visit" this node
    visited[node] = True
    path += numToNode[node]

    if len(path) > 2:
        solution.append(path)

    # traverse all edges from this node
    for adj in range(len(adjMatrix[node])):
        if not visited[adj] and adjMatrix[node][adj] == 1: # second condition is redundant as this is hardcoded an undirected complete graph
            dfs(adj, adjMatrix, visited, solution, path)
    
    # set node to unvisited for subsequent path traversals
    visited[node] = False

solution = []

for char in letters:
    visited = [False for _ in range(numNodes)]
    nodeIdx = nodeToNum[char]
    dfs(nodeIdx, adjMatrix, visited, solution, "")

solution.sort(key=lambda w: len(w), reverse=True)

alternatives = []

if solution:
    for word in solution:
        if word in english_words_set:
            print(Fore.GREEN + word)
        else:
            alternatives.append(word)
    if input(Style.RESET_ALL + "Do you want to see other options? (y/n): ") == "y":
        print("Alternatives may include...")
        for alt in alternatives:
            print(Fore.YELLOW + alt)
else:
    print(Fore.RED + "ERROR: No valid words found with those letters")

'''
NOTE: the words identified are dependent on the "english_words_set" set of valid words in the english dictionary, but I've found sometimes there are variations that are accepted in Wordscapes-like games that are NOT in this set of english words
'''