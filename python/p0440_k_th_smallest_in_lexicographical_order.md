# 440. K-th Smallest in Lexicographical Order · Python

[原题](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/)。

在整数1..n按十进制字符串字典序排列后返回第k个，原题1<=k<=n<=10^9。不能构造并排序十亿个整数，也不能把数值第k名当作字符串字典序第k名。

将数字视为十叉前缀树，先序遍历恰是字典序。当前prefix子树在每层占据[first,following)范围，起始为[prefix,prefix+1)，下一层同时乘10。与1..n相交后的数量是min(n+1,following)-first；逐层累计得到整个前缀子树的节点数，包含prefix自己，最后一层会按n截断。

remaining=k-1表示从当前节点向后还需前进的个数。若子树节点数不超过remaining，目标在该子树之后，可以整体跳过并进入下一兄弟；否则目标在该子树内部，且remaining仍为正，故先消耗当前节点，再进入首个孩子prefix*10。选定子树后目标始终位于其中，不会跳出最后一个孩子而错误跨过父前缀。remaining为0时当前prefix就是目标。

设D为n的十进制位数。每层至多尝试10个兄弟，每次计数扫描至多D层，时间O(D²)，额外空间O(1)；n<=10^9时D最多10。使用整数边界n+1明确处理闭区间上限，没有遍历全部结果或创建字符串排序副本。

独立参考对小n显式构造1..n并按str排序，核对n=1..200的每个合法k，共20100项查询。另测十进制幂前后的小边界、前缀被n截断，以及n=10^9的前缀长链与最后字典序元素。大边界期望来自明确数字顺序，不枚举十亿项。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
