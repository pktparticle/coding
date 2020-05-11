"""
Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/
O(m*n), easy
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        starting_pixel=image[sr][sc]
        if starting_pixel==newColor: return image
        def dfs(image, i, j):
            if i<0 or j<0 or i>=rows or j>=cols or image[i][j]!=starting_pixel:
                return
            else: image[i][j]=newColor
            dfs(image, i-1, j)
            dfs(image, i+1, j)
            dfs(image, i, j-1)
            dfs(image, i, j+1)
        dfs(image, sr, sc)
        return image