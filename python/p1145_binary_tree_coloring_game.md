# 1145. Binary Tree Coloring Game · Python

[原题](https://leetcode.com/problems/binary-tree-coloring-game/)。

题目节点值唯一、n为奇数，第一位玩家先占x。删去x后树分为左子树、右子树和父方向部分。第二位玩家若选择某块与x相邻的节点，就能封住该块入口；该块超过全树一半时必胜。若三块都不超过一半，第二位玩家只能占其中一块，第一位可守住其余多数，故无法保证获胜。用迭代后序一次统计所有子树大小，并在x处保存左右大小，不修改树。

时间O(n)，额外空间O(n)，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
