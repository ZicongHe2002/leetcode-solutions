# 889. Construct Binary Tree from Preorder and Postorder Traversal · Python

[原题](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)。

值互异，前序首项为根，下一项为第一个非空孩子的根。用它在后序中的位置确定该孩子子树长度，递归切分两遍历的下标区间。只有一个孩子时，前后序无法分辨左右，把它放左侧仍是题目允许的合法答案。用起点与长度传参，不反复复制遍历切片。TreeNode由LeetCode提供。

时间O(n)，后序下标表与递归栈额外空间O(n)，新建结果节点O(n)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
