# 496. Next Greater Element I · Python

[原题](https://leetcode.com/problems/next-greater-element-i/)。

原题nums1与nums2都非空、各自无重复，nums1是nums2的子集，长度至多1000，值在0..10000。对nums1每项，返回它在nums2右边第一个严格更大值；没有则为-1，答案按nums1顺序排列，两输入保持。

pending按从栈底到栈顶递减保存尚未找到答案的值。读到更大value时，栈顶此前经过的位置都没有更大值，当前值就是第一个合格答案，可依次弹出并建立映射；剩余值继续等待。原题唯一性让值本身可作键。每项至多入栈出栈一次，平均哈希操作下时间O(len(nums1)+len(nums2))，额外空间O(len(nums2))。

独立oracle先找nums1值在nums2的位置，再直接扫描右侧直到严格更大，不复用栈或映射。nums2取大小1..6的全部873个秩排列，nums1取每个非空子集并反序，共49489次查询。边界覆盖1000项、递增/递减、10000最大值与输出顺序，核对列表及两输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
