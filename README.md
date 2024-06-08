# Knapsack Algorithms 
by Lidia Golińska (157141) and Łukasz Przykłota (159440)

## Overview

One night, a group of thieves plans to heist an exclusive museum full of valuable paintings. Their goal is to select the most valuable works to maximize the profits from the heist. With the help of a special algorithm based on the knapsack problem, they choose those that will fit into a knapsack with a maximum weight of 50 kg. Will they succeed in their plan and escape with the museum treasures? Discover this exciting story in our project!

## Usage

1. Run the script using the following command:
```sh
python3 main.py
```
2. Follow the on-screen instructions to interact with the program. Available actions are:

- `help`: Show available actions.
- `print items` or `print`: Print details of all items.
- `knapsack brute force` or `bf`: Run the knapsack brute force algorithm.
- `knapsack dynamic programming` or `dp`: Run the knapsack dynamic programming algorithm.
- `exit`: Exit the program.

## Example `data.txt` Contents

```sh
50
20
Mona Lisa,10,670
Two Tahitian Women (When You Marry),15,300
Savior of the World,20,450
The Card Players,8,250
Interchange,12,300
No. 6 (Violet Green and Red),6,186
Number 17A,7,200
Les Femmes d’Alger,9,179
Portrait of Maerten Soolmans and Oopjen Coppit,10,180
Portrait of Adele Bloch-Bauer,5,135
No.5,6,140
Buổi khiêu vũ tại Moulin de la Galette,8,110
Portrait of Dr. Gachet,6,117
Dora Maar and Cat,4,95
The Boy with the Pipe,5,104
Massacre of the Innocents,4,78
Irises,3,79
Vincent van Gogh's Self-Portrait,2,72
Pierrette's Wedding,3,73
The Curtain The Pitcher and the Fruit Bowl,2,60
```

Each line represents:

- Maximum weight of the knapsack
- Number of items
- List of valuable paintings (name, weight, value)
