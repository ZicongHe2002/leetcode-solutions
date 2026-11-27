# 865. Smallest Subtree with all the Deepest Nodes · Python

[原题](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)。

后序给每个子树返回高度和覆盖其全部最深节点的最小子树根。左右同高时，最深节点同时分布两侧（叶子则两侧都空），必须由当前节点覆盖；高度不同时，全部最深节点只在更高一侧，直接沿用那侧候选。递归归并到原根后即得到答案，不需先列出所有最深叶或额外计算两两LCA。

时间O(n)，递归栈额外空间O(h)，h为树高。LeetCode提供TreeNode，原树不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
