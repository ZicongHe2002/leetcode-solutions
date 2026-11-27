# 1120. Maximum Average Subtree · Python

[原题](https://leetcode.com/problems/maximum-average-subtree/)。

题目根节点非空，子树包含某个节点及其全部后代，不能任意挑选部分节点。后序遍历在两个孩子结果可用后，计算当前子树总和与节点数，再用二者之比更新答案。空孩子贡献(0,0)，叶子直接得到自身数值。显式栈的ready标记模拟递归返回，避免深树触及Python递归深度限制。

时间O(n)，字典及遍历栈额外空间O(n)，不修改树节点；TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
