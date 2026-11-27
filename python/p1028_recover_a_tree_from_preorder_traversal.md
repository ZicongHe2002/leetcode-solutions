# 1028. Recover a Tree From Preorder Traversal · Python

[原题](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)。

每节点前连字符数表示深度，后面连续数字组成完整节点值。栈保存当前根到父路径，读到深度d时弹到长度d，栈顶就是父节点；前序先接左、再接右。题目单孩子保证为左孩子，所以首个孩子默认接左可唯一恢复。深度0时建立根，不把多位数拆成多个节点。

编码长L、树高H，时间O(L)，祖先栈额外空间O(H)，输出节点另计，不用递归解析。TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
