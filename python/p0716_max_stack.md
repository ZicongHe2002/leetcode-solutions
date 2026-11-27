# 716. Max Stack · Python

[原题](https://leetcode.com/problems/max-stack/)。

原题MaxStack支持push/pop/top/peekMax/popMax，popMax在并列最大时只移除离栈顶最近的一项。值在±10^7，五个API合计最多100000次；所有读取/删除操作保证非空。要求top为O(1)，其余操作O(log n)。不能用每次线性寻找最大值或在top中清理大量过期项代替这个合同。

每次push创建一个节点，同时处于两个顺序中：previous/next构成按入栈时间排列的双向链，tail直接指向栈顶；left/right/height构成按(value,递增序号)排列的AVL树。序号区分同值的不同出现，树中最右节点就是最大值中入栈最晚、且仍存在的那一项，恰满足popMax的并列规则。

top直接读tail。pop选择tail，popMax沿AVL右链选择最大键，二者调用同一删除过程：先按唯一键从AVL移除，再常数次改写链表邻接关系，若删掉tail就回退到previous。peekMax只读树最右值。删除中间最大值不会重排其他栈元素，未来pop仍按原先入栈顺序返回。

AVL每次在递归回溯更新高度，左右高度差超过1时用单旋或双旋修复；插入与删除后都维持有序性和高度平衡，树高O(log(n+1))。删除有两个树孩子的节点时，实际摘下右子树最小的后继节点，再把它接到被删节点的树位置，而不是复制后继的value/key到旧节点。后继自己的链表位置必须保持，否则树键与入栈身份会错配。

top时间O(1)；push/pop/peekMax/popMax均为O(log(n+1))，没有拒绝采样、延迟清扫或Python数组整体搬移。存储O(n)个当前节点，AVL递归临时空间O(log(n+1))；初始化O(1)。标准对象分配按常数计，不对实际计时或分配器作测量声明。

独立oracle用普通列表实现五个操作，popMax直接找最后一个最大值并真实删除。完整枚举数字-1/0/1的长度1..5合法API程序，每步后再核对top与peekMax；另核对200个固定种子200步混合程序、重复最大值后的后续弹栈与±10^7边界。最大实例恰100000次API：50000个递增push后交替pop/popMax，闭式期待值逐个下降，覆盖大量AVL旋转与删除，无全历史排序。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
