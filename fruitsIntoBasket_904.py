class Solution:
    # Find a longest subarray having 2(or K) distinct elemets
    def totalFruit(self, tree: List[int]) -> int:
        # Time: O(N)
        # Space O(N)
        l, count = 0, {}
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:  # Since we have more than 2 type of fruits,
                count[tree[l]] -= 1  # Remove earlier fruit one at a time
                if count[tree[l]] == 0:
                    del count[tree[l]]
                l += 1
        return j-l + 1
