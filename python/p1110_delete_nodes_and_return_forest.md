# 1110. Delete Nodes And Return Forest · Python

[原题](https://leetcode.com/problems/delete-nodes-and-return-forest/)。

题目节点值互不相同，to_delete表示需要删除的节点值。遍历时同时携带父节点、左右链接和当前节点是否为候选根。候选根保留下来就加入forest；当前节点若删除，就清除其父节点指向它的链接，并将其所有孩子标为新的候选根继续处理。即使父子连续删除，也会继续下探，直到真正保留的后代成为根。森林输出顺序不受题意限制。

遍历使用显式栈，不依赖树深递归。n个节点、d个待删除值，时间O(n+d)，额外空间O(n+d)，原地修改树的孩子指针，LeetCode提供TreeNode类型。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
