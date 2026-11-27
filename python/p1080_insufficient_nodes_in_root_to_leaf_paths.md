# 1080. Insufficient Nodes in Root to Leaf Paths · Python

[原题](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/)。

以原树根到叶的路径总和判定，不能把剪枝后新产生的叶子当作原叶子重新判断。进入节点时累加路径和，原叶子的结果直接由是否达到limit确定；原内部节点等两个子树处理后，只有至少一个子树仍有合格原叶子才保留。ready标记模拟后序返回，kept记录每个子树的剪枝结果。负数节点允许存在，因此不能仅凭当前前缀和提前保留或删除整个子树。

时间O(n)，字典和显式栈额外空间O(n)。原地更新保留节点的左右孩子指针，返回剪枝后的根；LeetCode提供TreeNode类型。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
