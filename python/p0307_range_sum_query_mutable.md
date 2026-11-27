# 307. Range Sum Query - Mutable · Python

[原题](https://leetcode.com/problems/range-sum-query-mutable/)。

原题nums长1..30000，元素和更新值都在-100..100。NumArray支持update(index,val)将某位置赋成val，返回None；sumRange(left,right)返回合法闭区间和int。每对象两种方法合计最多30000次调用。本实现复制初始列表，后续更新只影响对象内部状态，不修改调用者输入。

一基Fenwick节点i保存末尾lowbit(i)=i&-i个原元素的和，向上更新跳到i+lowbit(i)，向下求前缀跳到i-lowbit(i)。构造时从原元素开始，把每个已聚合节点加给唯一父节点，线性完成树表。赋值必须先求新值减旧值的difference，再更新保存的旧值及所有包含该点的树节点；查询闭区间用前right+1项减前left项。构造时间O(n)，update与sumRange各O(log n)，存储O(n)，单点和重复赋相同值也成立。

独立参考维护普通可变列表，更新后直接切片sum，不使用lowbit。长度1..5、值-1/0/1的363个数组，各位置连续赋-2/0/2并在每次赋值后查询全部区间。另在30000长数组上执行15000次更新和15000次查询，查询用单点、千元素块及最后全数组直接求和，总调用数恰30000；新建对象验证极值非零初始树表，检查None、int与调用者列表不变。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
