# 225. Implement Stack using Queues · Python

[原题](https://leetcode.com/problems/implement-stack-using-queues/)。

原题接口MyStack()、push(x)、pop()、top()、empty()，仅可用队列基本操作实现栈。x在1..9内，每个实例至多100次接口调用，pop/top保证非空。push返回None，pop/top返回int，empty返回bool。

只使用一个队列，队首始终放逻辑栈顶。push先把新值入队尾，再把原来所有元素逐个从队首出队、重新入队尾，恰好把新值移到队首，同时保留旧元素的栈顶到栈底顺序。pop只从队首取出，top只查看队首；没有把队列当作可任意下标访问或从尾端弹出的栈。

push时间O(n)，pop/top/empty为O(1)，空间O(n)。每次旋转前确定原元素个数，所以不会无限搬运刚插入的新值。

独立oracle使用普通列表末端作为栈，不做队列旋转。2种插入值、至多6次调用的全部8065个合法程序核对，生成时排除空栈pop/top。上限分别用3个实例覆盖50次push加50次pop、99次push加top、100次empty，每个实例都不超过100调用，值覆盖1..9。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
