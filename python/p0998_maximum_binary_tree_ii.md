# 998. Maximum Binary Tree II · Python

[原题](https://leetcode.com/problems/maximum-binary-tree-ii/)。

新值追加在原数组末尾，中序位置必须是最右，所以只影响原树右链。若新值大于整树根，它成为新根，旧树作左孩子；否则沿右链越过所有更大节点，找到首个更小右子树，把它作为新节点左孩子，再把新节点接为当前位置右孩子。这样同时保持最大堆序与追加后的中序顺序。复用旧节点，会修改相应右指针，TreeNode由LeetCode提供。

时间O(h)，除新节点外额外空间O(1)，h为右链长度上界。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
