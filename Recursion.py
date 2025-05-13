# Permutations, Subsets, N-Queens, Word 
#DFS
#Leetcode 78, 77, 79, 39, 51

# leetcode 39
def combinationSum(candidates, target):
    '''
    Given an array of distinct integers candidates and a target integer target, 
    return a list of all unique combinations of candidates where the chosen numbers sum to target.
    You may reuse the same number unlimited times.
    >>> combinationSum([2,3,6,7], 7)
    >>> [[2,2,3], [7]]

    >>> combinationSum([2,3,5], 8)
    >>> [[2,2,2,2],[2,3,3],[3,5]]

    >>> combinationSum([2], 1)
    >>> []

    '''

    pass



# leetcode 51
def solveNQueens(n):
    '''
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
    such that no two queens attack each other
    Return all distinct solutions to the n-queens puzzle.
    Each solution contains a distinct board configuration of the queen placements.
    >>> solveNQueens(4):
    >>> [
            [".Q..",  # Solution 1
            "...Q",
            "Q...",
            "..Q."],

            ["..Q.",  # Solution 2
            "Q...",
            "...Q",
            ".Q.."]
        ]
    '''
    pass

# Leetcode 46: Permutations
def Permutations(nums):
    '''
    Given an array nums of distinct integers, 
    return all the possible permutations of the array.
    You can return the answer in any order.
    >>> Permutations([1,2,3])
    >>> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    >>> Permutations([0,1])
    >>> [[0,1],[1,0]]

    >>> nums = [1]
    >>> [[1]]
    '''
    n = len(nums)
    res, sol = [], []

    def backtrack():
        if len(sol) == n:
            res.append(sol[:])
            return

        for ele in nums:
            print(ele)
            if ele not in sol:
                sol.append(ele)
                backtrack()
                sol.pop()
                print("pop")
    backtrack()
    print("final")
    return res

# Leetcode 47: Permutations 2
def permuteUnique(nums):
    '''
    Given a collection of numbers, nums, that might contain duplicates,
    return all possible unique permutations in any order.
    >>> permuteUnique([1, 1, 2])
    >>> [[1,1,2], [1,2,1], [2,1,1]]

    '''
    res, sol = [], []
    count = {n:0 for n in nums}
    for n in nums:
        count[n] += 1
    
    def backtrack():
        if len(sol) == len(nums):
            res.append(sol[:])
            return
        
        for n in count:
            if count[n] > 0:
                sol.append(n)
                count[n] -= 1
                backtrack()
                count[n] +=1
                sol.pop()

    backtrack()
    return res

#Leetcode 78
def subsets(nums):
    '''
    Given an integer array nums of unique elements, 
    return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. 
    You may return the subsets in any order.
    >>> subsets([1,2,3])
    >>> Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

    >>> subsets([0])
    >>> Output: [[], [0]]
    '''
    n = len(nums)
    result, sol = [], []

    def backtrack(i):
        if i == n:
            result.append(sol[:])
            return
        backtrack(i+1)
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return result

#Leetcode 77
def combine(n, k):
    '''
    Given two integers n and k, 
    return all possible combinations of k numbers chosen from the range [1, n].
    You may return the answer in any order.
    >>> combine(4, 2)
    >>> Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    '''

    result, sol = [], []
    def backtrack(i):
        if len(sol) == k:
            result.append(sol[:])
            return
        left = i
        need = k -len(sol)
        if left > need:
            backtrack(i - 1)
        sol.append(i)
        backtrack(i-1)
        sol.pop()

    backtrack(n)
    return result

# leetcode 79
def exist(board, word):
    '''
    Given an m x n grid of characters board and a string word, 
    return True if word exists in the grid. 
    The word can be constructed from letters of sequentially adjacent cells, 
    where "adjacent" cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    word = "ABCCED"
    >>> exist(board, word)
    True
    '''
    pass

if __name__ == "__main__":
    #print(Permutations([1]))
    #print(Permutations([1,2]))
    #print(Permutations([1,2,3]))
    print(permuteUnique([1, 1, 2]))

    #print(subsets([0,1,3]))
    #print(subsets([0]))

    #print(combine(4,2))

