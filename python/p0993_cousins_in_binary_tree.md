# 993. Cousins in Binary Tree · Python

[原题](https://leetcode.com/problems/cousins-in-binary-tree/)。

节点值唯一，堂兄弟要求深度相同但父节点不同。层序每次处理一整层并记录本层命中值的实际父对象；首次出现任一目标后，若另一目标没在该层出现就深度不同，直接失败。两者同层还需父身份不同，排除亲兄弟，根的父None也不会与未找到混淆，因为使用命中字典判断是否出现。

时间O(n)，队列额外空间O(n)，原树保持，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
