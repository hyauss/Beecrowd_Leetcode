class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx,comb,total):
            if total == target:
                res.append(comb[:])
                return
            if total> target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            backtrack(idx,comb,total + candidates[idx])
            comb.pop()
            backtrack(idx+1,comb,total)

            return res
        return backtrack(0,[],0)

    #Complexity Analysis
    #Time Complexity: O(2^n) in the worst case, as we explore all subsets of candidates.
    #Space Complexity: O(t/d), where t is the target and d is the smallest candidate, representing the depth of the recursion.
    #Last try: 17/01/2026