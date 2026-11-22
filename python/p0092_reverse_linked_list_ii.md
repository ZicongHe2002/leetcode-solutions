# 92. Reverse Linked List II · Python

[原题](https://leetcode.com/problems/reverse-linked-list-ii/)。

输入无环单链表含1..500节点，值在[-500,500]，位置满足1<=left<=right<=长度。反转闭区间[left,right]，位置使用一基下标。前后区间原顺序保留，全部原节点恰好出现一次，值不变，不构造替代结果链；不承诺空输入或越界位置。

从哨兵走left-1步得到区间前驱before，first是原区间首节点，最后将成为区间尾。每次取first.next为moved，先把它从first后摘下，再插到before之后。经过t次，原区间前t+1节点已倒序，first仍是该段尾，first.next指向下一个待搬节点或未处理后缀。执行right-left次便覆盖整个区间。哨兵统一处理left=1；单节点区间不改链接。时间O(L)，额外空间O(1)。

独立oracle将原节点数组的目标切片反序，直接比较结果身份。枚举-1/0/1上长度1..6的1092条链和每个合法闭区间，共19956次。边界覆盖500节点整段、只反首对/尾对、保留两端的中间段、相同值节点和单节点，检查所有原值及终止None；身份检查能排除只交换值的错误实现。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
