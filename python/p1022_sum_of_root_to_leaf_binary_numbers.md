# 1022. Sum of Root To Leaf Binary Numbers · Python

[原题](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)。

节点位为0或1，从根到当前节点的二进制值由父前缀乘2加当前位得到。栈给每个分支携带独立前缀，仅在左右孩子均空的叶子累计，内部共享前缀不单独计数。位运算自然处理前导0，不用为每条路径构造字符串，原树不修改。

按题目答案整数范围计，时间O(n)，DFS栈空间O(h)，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
