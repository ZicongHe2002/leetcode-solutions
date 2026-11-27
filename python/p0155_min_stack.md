# 155. Min Stack · Python

[原题](https://leetcode.com/problems/min-stack/)。

原题接口MinStack()、push(val)、pop()、top()、getMin()，值为有符号32位整数，总调用至多30000次。pop/top/getMin保证仅在非空栈调用。push和pop返回None，top与getMin返回int。

每个栈项同时保存实际值以及到这个位置为止的最小值。入栈时用新值与旧栈顶前缀最小值取min，空栈则直接用新值；出栈时整项移除。这样弹出当前最小值后，新的栈顶已经带有旧前缀的正确最小值，不需要扫描或重新计算，重复的最小值也各自保留。

使用deque保存栈项，避免列表扩容时复制已有元素。top与getMin只读取deque末端栈项，push/pop只在末端插入或删除，四个操作均为O(1)；存储n个元素需要O(n)空间。没有通过数值编码压缩栈项，不受32位差值溢出影响。

独立oracle直接用普通值列表，top取末项、getMin每次调用原生min。枚举3种边界值、至多6次调用的全部23917个合法短程序，生成时排除空栈查询/弹出。另有15000次push、14998次pop与两次查询组成的30000调用上限程序，覆盖32位正负端点及最小值恢复。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
