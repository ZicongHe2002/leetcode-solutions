# 958. Check Completeness of a Binary Tree · Python

[原题](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)。

完全二叉树的层序位置必须先全部非空，再全部空，不允许中间有空洞后还有节点。BFS把左右孩子连同None按次序入队，首次None打开gap标记；之后若出现真实节点立刻失败。None不再扩展，队列仍是有限线性规模。右孩子存在而左孩子缺失等情况自然被捕获，原树保持。

时间O(n)，队列空间O(n)，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
