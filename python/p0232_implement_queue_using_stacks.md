# 232. Implement Queue using Stacks · Python

[原题](https://leetcode.com/problems/implement-queue-using-stacks/)。

原题接口MyQueue()、push(x)、pop()、peek()、empty()，仅用栈基本操作实现FIFO。x为1..9，每个实例至多100次调用，pop/peek保证队列非空。push返回None，pop/peek返回int，empty返回bool。

incoming按入队顺序压栈，outgoing的栈顶保存当前最早元素。只有outgoing为空时，才把incoming全部弹出并压入outgoing，借反转把最早元素移到栈顶。若outgoing仍有旧元素，新插入的元素必须继续留在incoming，不能提前混入旧队首之前。pop/peek先确保输出栈可用，empty则同时检查两个栈。

一个元素最多入incoming一次、从中弹出一次、入outgoing一次、最终再弹出一次，所以一串m次操作总工作量O(m)，每操作摊销O(1)；触发搬运的单次pop/peek最坏O(n)。空间O(n)，只使用列表末端的栈操作，不从列表头删除。

独立oracle使用collections.deque的FIFO行为，不用两个栈。2种插入值、至多6次调用的全部8065个合法程序核对，排除空队列pop/peek。3个上限实例分别执行50次push加50次pop、99次push加peek、100次empty，每个实例恰100调用且值在1..9内。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
