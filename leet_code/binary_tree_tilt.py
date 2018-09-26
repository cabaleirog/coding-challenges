"""Binary Tree Tilt.

https://leetcode.com/problems/binary-tree-tilt1

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum
of all left subtree node values and the sum of all right subtree node values.
Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:

    Input:
          1
        /   \
       2     3

    Output: 1

    Explanation:
        Tilt of node 2 : 0
        Tilt of node 3 : 0
        Tilt of node 1 : |2-3| = 1
        Tilt of binary tree : 0 + 0 + 1 = 1

"""


class Solution:
    def findTilt(self, root):
        tree_tilt, _ = self._find_tilt(root)
        return tree_tilt

    def _find_tilt(self, node):
        if not node:
            return (0, 0)
        agg_tilt_left, agg_sum_left = self._find_tilt(node.left)
        agg_tilt_right, agg_sum_right = self._find_tilt(node.right)
        return (
            abs(agg_sum_left - agg_sum_right) + agg_tilt_left + agg_tilt_right,
            node.val + agg_sum_left + agg_sum_right)
