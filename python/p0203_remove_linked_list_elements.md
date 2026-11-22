# 203. Remove Linked List Elements · Python

[原题](https://leetcode.com/problems/remove-linked-list-elements/)。

输入是0..10000节点的无环单链表，节点值在[1,50]，val在[0,50]。删除值等于val的全部节点。输出按原顺序重用其余节点、以None结束，不复制结果节点、不改写任何原节点值；空输入或全部删除返回None。

哨兵统一处理连续的目标值头段。previous始终是已保留前缀的最后节点，或前缀为空时的哨兵；previous.next是下一个待决定节点。该节点值匹配时跨过它而不移动previous，才能继续删除紧接的目标；不匹配才将previous前移。每轮处理一个原节点，所以时间O(L)，额外空间O(1)。

独立oracle从原节点数组按原值过滤，不复用链上跳过过程。枚举值1/2/3上长度0..7的3280条链，对val=0..4全部核对，共16400次；逐个比较输出对象、终止None与全部原值。边界覆盖10000个目标节点、10000节点交替值、值50与目标0/50、连续头尾段和空输入。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
