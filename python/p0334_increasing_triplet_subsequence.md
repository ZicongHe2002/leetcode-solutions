# 334. Increasing Triplet Subsequence · Python

[原题](https://leetcode.com/problems/increasing-triplet-subsequence/)。

原题nums长1..500000，元素在-2^31..2^31-1，判断是否有i<j<k且nums[i]<nums[j]<nums[k]，返回bool。要求严格递增，相等值不能增加长度，输入保持不变。

first保存前缀最小值，second保存前缀所有严格递增二元组中最小的末值；2^31比所有合法元素都大，表示尚不存在。新值不大于first就更新最小值，否则它可接在此前first后形成二元组；若不大于second就降低该末值，否则已有历史二元组末值小于它，三元组成立。second一旦有限，总有当时更早的严格较小前驱；后来first变小不要求它仍与second来自同一对下标，也不抹去历史见证。两处<=使重复值只替换阈值，不误当成严格增长。时间O(n)，额外空间O(1)，满足原题进阶要求。

独立参考枚举全部三下标组合，直接检查严格值序，不维护两个阈值。长度1..8、值-1/0/1的9840个数组全覆盖；另测500000元素、全同/递减/交替两值/末尾才出现三元组、first晚于历史second的状态及32位值端点，核对bool与输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
