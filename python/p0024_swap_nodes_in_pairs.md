# 24. Swap Nodes in Pairs · Python

[原题](https://leetcode.com/problems/swap-nodes-in-pairs/)。

输入无环单链表有0..100个节点，值在[0,100]。相邻节点两两交换并返回新头，不能只交换节点值。本实现重连原节点，所有原节点恰好出现一次，值保持；奇数长度的最后一个节点留在末尾，空输入返回None。

哨兵前驱previous指向下一对之前，first/second是待交换的两个原节点。先让first接到这对之后的后缀，再让second接first，最后previous接second；这样未处理后缀不会丢失，交换后这一对的尾是first，令previous=first继续。循环前已完成前缀身份顺序正确，且previous.next是尚未处理后缀。没有完整两节点时终止，原单节点尾不改动。时间O(L)，额外空间O(1)，只分配一个哨兵。

独立oracle在原节点数组中把每个长度2的小段反序，直接核对输出的对象序列及尾部None，不复用链表重连。枚举0/1/2上长度0..7的全部3280条链；同值节点仍须按身份交换。边界覆盖100节点、100个相同值、空链、单节点和奇数尾；逐次检查全部节点值保持。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
