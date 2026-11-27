# 897. Increasing Order Search Tree · Python

[原题](https://leetcode.com/problems/increasing-order-search-tree/)。

BST中序给出非递减节点顺序。显式栈保存待回访祖先，每次取出节点先保存原右孩子，再清空左右链接、接到结果尾部，接着遍历保存的右子树。结果最左小节点成为根，所有节点无左孩子且仅沿右链递增。复用原TreeNode，所以会原地重接输入节点；哑节点不属于结果。

时间O(n)，栈额外空间O(h)，h为原树高，除哑节点不复制结果节点。LeetCode提供TreeNode。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
