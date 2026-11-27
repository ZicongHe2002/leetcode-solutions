# 116. Populating Next Right Pointers in Each Node · Python

[原题](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)。

原题是完美二叉树：每个非叶有两个孩子，所有叶子同层；节点0..4095，值-1000..1000，初始全部next为None。只改变next，返回原根；不能把稀疏树当作本题合法输入。Node类供本地导入，val/left/right/next与评测器一致。

当前层的next已经连好，根层初始即满足。沿next遍历本层每个父节点，把左孩子接到右孩子；右孩子接到同层下一个父节点的左孩子，若已在最右则设None。完美树保证这些孩子存在，因此本层结束时下一整层已正确连接。leftmost下移到下一层最左节点，直到叶层。跨父节点边界通过current.next.left处理，而非只连接兄弟。

所有非叶节点访问一次，时间O(n)，只用固定指针，额外空间O(1)，不使用队列或递归。测试参考只沿left/right用队列划分层，逐对象比较每个next及层尾None，另检查val/left/right完全保持。枚举高度0..3、值-1/1的全部139个完美树样本；另测4095节点最大完美树、重复值和合法值域两端。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
