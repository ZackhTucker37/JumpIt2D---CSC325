#!/usr/bin/env python3
#Authors: Zackh Tucker & Nathan Hall
#
#Questions:
#1.  Describe, in plain English, how the Two-Dimensional Jump-It problem exhibits overlapping subproblems.
#
#    By finding the minimum cost from an m x n matrix, you need to know the minimum cost of the m-1 x n,
#    or m x n-1 sub-problem.  And to solve those, the same process is needed again, proceeding down to
#    the point of ending at the exiting cell.
#
#2.  Describe, in plain English, how the Two-Dimensional Jump-It problem exhibits optimal substructure.
#
#    By finding the greedy solution from the exit cell, so it's accessible nieghboring cells,
#    we've found the optimum solution of this substrucutre.  The pattern repeats outward from
#    the newly evaluated cells until it reaches the starting cell.

import sys

global board, cost

with open(sys.argv[1], 'r') as board_data:
    rows, columns = tuple(int(x) for x in board_data.readline().split())
    board = [[int(v) for v in line.split()] for line in board_data]

def jumpIt(cost, rows, columns):
    
    m, n = rows - 1, columns - 1
    
    totalCost = [[0 for i in range(columns)] for j in range(rows)]

    #initialize cost of the exit
    totalCost[m][n] = board[m][n]
    
    #initialize the last column
    for i in range(1,rows):
        if i < 2:   #the adjacent pair's minimum cost is jumping to the exit cell itself.
            totalCost[m - i][n] = board[m - i][n] + totalCost[m][n]
        else:
            totalCost[m - i][n] = board[m - i][n] + min(totalCost[m - i + 1][n], totalCost[m - i + 2][n])
            
    #initialize the bottom row
    for j in range(1, columns):
        if j < 2:  # the adjacent pair's minimum cost is jumping to the exit cell itself.
            totalCost[m][n - j] = board[m][n - j] + totalCost[m][n]
        else:
            totalCost[m][n - j] = board[m][n - j] + min(totalCost[m][n - j + 1], totalCost[m][n - j + 2])
    

    #initialize cost of the interior diagonal cell at position (m-1)(n-1)
    totalCost[m-1][n-1] = min(totalCost[m][n-1], totalCost[m-1][n]) + board[m-1][n-1]
    
    
    #loop through the remaining totalCost entries, by finding the minimum cost
    #of the 4 possible jump posoitions (2 to its right, 2 below)
    for i in range(1,rows):
        for j in range(1,columns):
            #special case where the code will look for table values too far to the right AND down (exceeding both the last row and last column)
            if m-i+2 > m and n-j+2 > n:
                totalCost[m-i][n-j] = min(totalCost[m-i+1][n-j], totalCost[m-i][n-j+1]) + board[m-i][n-j]
            #special case where the code will look for table values too far to the right (exceeding the last column)
            elif m-i+2 <= m and n-j+2 > n:
                totalCost[m-i][n-j] = min(totalCost[m-i+1][n-j], totalCost[m-i][n-j+1], totalCost[m-i+2][n-j]) + board[m-i][n-j]
            #special case where the code will look for table values too far down (exceeding the last row)
            elif m-i+2 > m and n-j+2 <= n:
                totalCost[m-i][n-j] = min(totalCost[m-i+1][n-j], totalCost[m-i][n-j+1], totalCost[m-i][n-j+2]) + board[m-i][n-j]
            #fills in the rest of the table
            else:
                totalCost[m-i][n-j] = min(totalCost[m-i+1][n-j], totalCost[m-i][n-j+1], totalCost[m-i+2][n-j], totalCost[m-i][n-j+2]) + board[m-i][n-j]

    return totalCost

minCost = jumpIt(board, rows, columns)

print(minCost[0][0])