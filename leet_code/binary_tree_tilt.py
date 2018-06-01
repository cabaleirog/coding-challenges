# TODO: Documentation

# https://leetcode.com/problems/binary-tree-tilt


class Solution:
    def findTilt(self, root):
        tree_tilt, _ = self._find_tilt(root)
        return tree_tilt
    
    def _find_tilt(self, node):
        if not node:
            return 0, 0
        agg_tilt_left, agg_sum_left = self._find_tilt(node.left)
        agg_tilt_right, agg_sum_right = self._find_tilt(node.right)
        return (
            abs(agg_sum_left - agg_sum_right) + agg_tilt_left + agg_tilt_right,
            node.val + agg_sum_left + agg_sum_right)
        
