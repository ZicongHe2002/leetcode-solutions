# 377. Combination Sum IV · Python

[原题](https://leetcode.com/problems/combination-sum-iv/)。

原题nums含1..200个互异正整数，值在[1,1000]，target在[1,1000]，统计总和为target的有序序列数，元素可重复使用，排列顺序不同分别计数。输入保证最终答案适合32位整数。本实现额外定义target=0时空序列计1，不支持非正候选值，不修改nums。

counts[total]按序列的最后一个值分类：若最后值为value，前缀的和为total-value，贡献counts[total-value]个。候选值为正，依赖的总和更小，因此先遍历总和、再遍历所有候选；每个有序序列有唯一最后值，不重不漏。counts[0]=1表示空前缀。时间O(target·len(nums))，额外空间O(target)，与把候选循环放外层的无序硬币组合语义不同。

独立oracle枚举长度不超过target/min(nums)的全部候选元组，直接按总和筛选，不复用计数递推。从值池1..5选任意非空子集并枚举输入顺序，对target=0..6核对，共2275次，0目标为扩展。边界覆盖200候选、目标1000、不可达、单候选，以及[1,2]目标45用位置组合数求和得到1836311903的独立期望；输入保持。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
