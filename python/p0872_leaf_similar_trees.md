# 872. Leaf-Similar Trees · Python

[原题](https://leetcode.com/problems/leaf-similar-trees/)。

只有左右孩子都不存在的节点才是叶子。迭代DFS先压右再压左，使弹栈访问叶子的顺序为从左到右；分别得到两棵树的完整叶值序列，相等就叶相似。比较顺序与重复次数，不能仅比较集合，也不要求两棵树结构相同。

两树节点数N和M，时间O(N+M)，包含叶值列表和栈的额外空间O(N+M)。LeetCode提供TreeNode，原树保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
