# 622. Design Circular Queue · Python

[原题](https://leetcode.com/problems/design-circular-queue/)。

原题MyCircularQueue(k)，容量1..1000、入队值0..1000，支持enQueue/deQueue、Front/Rear、isEmpty/isFull。入队满或出队空返回False且状态不变；空访问返回-1。每对象外部操作最多3000次，不使用内置queue。

固定列表保存容量k个槽，_front指向逻辑首元素，_size区分空与满。新尾下标为(front+size)%k，删除只把front前移并减size，尾元素下标为(front+size-1)%k。索引取模重复利用前部已空槽，先判空满避免读取陈旧值或覆盖有效元素。k>=1保证取模合法，容量1也能正确区分空满。构造O(k)，所有外部方法O(1)，存储O(k)，未用列表头部移动实现出队。

独立模型用普通列表表达FIFO，枚举容量1/2/3、两种值入队和出队的长度0..6全部3279条操作序列，每步核对返回值及四个观察方法。另在容量1000上执行恰3000次外部调用，包含填满失败、删除后环绕写入、反复复用槽，验证bool和int返回类型。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
