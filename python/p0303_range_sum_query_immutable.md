# 303. Range Sum Query - Immutable · Python

[原题](https://leetcode.com/problems/range-sum-query-immutable/)。

原题nums长1..10000，元素在-100000..100000，构造NumArray对象后接收最多10000次sumRange(left,right)，下标满足0<=left<=right<n，返回闭区间整数和。原题接口是NumArray，不是Solution；本实现不改动传入列表。

_prefix[k]保存前k个元素之和，最前面补0使left=0也使用同一公式。闭区间[left,right]对应前right+1项减前left项，左右端点各恰保留一次；单点、负值与全数组无需额外分支。构造时间O(n)、存储O(n)，每次查询O(1)。Python整数精确求和，不在查询时重新切片或遍历原列表。

独立参考直接对原列表切片求sum，枚举长度1..7、值-1/0/1共3279个数组的全部合法区间。另在10000长极值交替数组上连续执行恰10000次查询，参考按区间长度奇偶给出；新建独立对象验证全正/全负极值和。每个对象均未超过原题查询上限，核对int、跨多次查询状态及输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
