# 114. Flatten Binary Tree to Linked List · Python

[原题](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)。

输入二叉树有0..2000节点，值在[-100,100]。按原树前序顺序把原节点就地重连为单链：每个left为None，right指向下一个原节点，最后right为None，函数返回None。全部节点恰好一次，节点值不变；空树也返回None。

当前位置若有左子树，左子树应先于原右子树出现。沿左子树的right脊找到一个空右槽，把原右子树暂接到这里，再把整个左子树移到current.right并清空current.left。之后继续沿right推进，会先处理原左子树，最后才到原右子树；这些局部接续保留前序顺序而无需额外栈。寻找右脊的扫描可以按原树的右边摊还，每条这样的边只归属一次对应左子树扫描，外层也只沿最终链前进，故总时间O(L)，额外空间O(1)。

独立oracle在修改前用显式栈保存原前序节点数组，修改后按该数组逐项比对实际对象、left为None、原值及最后right为None；不只核对值，避免复制节点或丢节点。枚举长度0..6全部树形及二值赋值，共10067棵。边界覆盖2000节点纯左/纯右链、1999节点梳状树、值两端、相同值节点和空树；返回None也被检查。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
