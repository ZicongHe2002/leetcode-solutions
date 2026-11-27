# 117. Populating Next Right Pointers in Each Node II · Python

[原题](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)。

原题为任意二叉树，节点0..6000、值-100..100，初始next全部None，填入同层右邻，没有右邻则None，返回原根。只改next，保持val/left/right；Node类供本地独立导入，字段与评测器一致。

level指向当前层第一个节点，本层next链已经建立，根层由初始None成立。遍历本层next，按从左到右顺序把存在的左孩子、右孩子依次接到下一层tail后；缺孩子时直接跳过，因此可以跨过多个没有孩子的父节点。一个复用的dummy保存下一层头，每层开始清空dummy.next，结束将tail.next设None，保证层尾不串到旧链；然后level=dummy.next。没有下一层时退出，空树也直接返回None。

每个真实节点恰访问一次，时间O(n)，只有一个哨兵与固定指针，额外空间O(1)，没有层宽队列或递归栈。独立测试沿left/right用队列求各层，再核对每个next对象及原结构保持。枚举0..6节点全部树形并赋值-1/1，共10067个样本，包含空树、重复值和缺孩子；另测6000节点完全树、6000节点交替左右的深链和合法值域两端。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
