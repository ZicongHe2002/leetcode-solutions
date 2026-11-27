# 971. Flip Binary Tree To Match Preorder Traversal · Python

[原题](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/)。

节点值唯一，处理根后若左孩子存在但不是voyage下一值，不翻当前节点就不可能匹配，因此该翻转是强制的；显式栈改为先右后左遍历并记录当前值。否则保留先左后右。任何实际节点值不符、航程提前耗尽或最后仍有未消费值都失败。所有记录翻转都由下一个唯一值强制，故数量最少。只调整遍历顺序，不真的交换输入指针。

时间O(n)，栈与返回记录总空间O(n)，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
