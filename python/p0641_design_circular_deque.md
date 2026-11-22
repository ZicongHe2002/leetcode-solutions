# 641. Design Circular Deque · Python

[原题](https://leetcode.com/problems/design-circular-deque/)。

原题MyCircularDeque(k)容量1..1000，插入值0..1000，支持两端插删、两端访问和空满查询，每对象最多2000次外部调用。插删成功返回bool，满时不能插、空时不能删，空访问返回-1。

用固定数组、front和size表示逻辑区间。前插先将front模k减1再写入，后插写(front+size)%k；前删移动front并减size，后删只减size。后端位置由front+size-1计算，所以无需维护额外尾指针；所有读写先判空满，失败不改变索引或大小。Python正模使前端从0向前也合法环绕。构造O(k)，所有外部操作O(1)，空间O(k)，不使用内置deque或数组头部移动。

独立普通列表模型覆盖容量1/2/3，前后插0或1、前后删这6种变更的长度0..5全部27993条序列，每步检查完整两端和空满状态。另在容量1000执行恰2000次外部调用，包含满失败、前删后插环绕、后删前插和观察方法，核对bool与int。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
