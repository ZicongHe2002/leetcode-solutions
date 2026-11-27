# 894. All Possible Full Binary Trees · Python

[原题](https://leetcode.com/problems/all-possible-full-binary-trees/)。

满二叉树每个节点有0或2个孩子，所以节点总数只能是奇数。对奇数n，根占1，枚举左右奇数规模之和n-1，把所有左右形状做笛卡尔积。单节点形状用None标记，其余用不可变二元组；缓存只复用形状。最后为每个返回形状递归新建值为0的TreeNode，使不同结果树不共享可变节点。

令C为节点数n时的满树形状数，即Catalan((n-1)/2)，最终必须分配n*C个输出节点，时间O(nC)，输出空间O(nC)，缓存形状与递归额外空间上界O(C+n)。TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
