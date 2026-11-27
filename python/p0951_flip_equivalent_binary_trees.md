# 951. Flip Equivalent Binary Trees · Python

[原题](https://leetcode.com/problems/flip-equivalent-binary-trees/)。

空树只与空树等价，根值不同立即失败。根值相同后，当前节点要么不翻转并左右对应，要么翻转并交叉对应；至少一类中两对子树都等价即可。递归表达每个节点可独立翻转，不实际修改原树。题目每棵树内节点值唯一，使两种非空候选配对不可能都沿相同值持续扩展。

在该唯一值合同下时间上界O(n+m)，递归栈O(h1+h2)。TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
