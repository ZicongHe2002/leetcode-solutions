# 919. Complete Binary Tree Inserter · Python

[原题](https://leetcode.com/problems/complete-binary-tree-inserter/)。

初始树非空且完全，层序保存所有缺孩子节点，队首就是下一个插入父节点。先补左孩子，再补右孩子；补右后父节点满，从队首移除。新叶子进入队尾，继续维持层序待填位置。insert返回实际父值，get_root返回同一根对象，插入会更新其孩子指针。TreeNode由LeetCode提供。

初始化O(n)，每次insert与get_root为O(1)，节点与候选队列总空间O(n+插入数)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
