# 1157. Online Majority Element In Subarray · Python

[原题](https://leetcode.com/problems/online-majority-element-in-subarray/)。

接口为MajorityChecker，题目保证threshold严格超过查询闭区间长度的一半，数组不更新。线段树节点保存消去不同值配对后剩余的候选和值数；真正严格多数不可能被全部抵消，因此若查询存在合格值，它必为抵消后的候选。候选自身不代表已达到阈值，还要在其有序出现位置中二分统计[left,right]内真实次数。这是确定性算法，不用随机抽样冒充必然正确。

初始化时间和空间O(n)，每次查询O(log n)，不修改原数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
