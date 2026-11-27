# 1008. Construct Binary Search Tree from Preorder Traversal · Python

[原题](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)。

前序先根再左再右，节点值唯一。新值小于栈顶时属于其左子树，直接接左；更大时，弹出所有比它小的已结束祖先，它应作为最后弹出节点的右孩子，剩余栈顶仍是更大上界祖先。新节点再压栈，保持尚未完成右子树的祖先链。每节点进出栈一次，不对每个节点反复从根搜索。

时间O(n)，祖先栈空间O(h)，结果节点O(n)，输入前序保持，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
