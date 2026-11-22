# 718. Maximum Length of Repeated Subarray · Python

[原题](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)。

原题两个数组各长1..1000，每项0..100，求同时出现于两数组的最长连续子数组长度，不能跳过中间元素。两输入数组保持，额外支持空数组返回0。

suffix[j]表示恰在当前nums1位置和nums2第j项结束的公共后缀长度。当前值相同就接在旧对角后加1，不同就必须清零，不能像公共子序列那样保留邻格最大值。j倒序使suffix[j-1]仍是上一行状态；best独立记录全部结束位置的最大值。时间O(len(nums1)*len(nums2))，额外空间O(len(nums2)+1)。

独立oracle把两个数组的全部连续切片转为元组集合，再从交集中取最大长度，不复用后缀DP。二进制数组各长0..5共3969对核对，空数组单列扩展。边界覆盖1000元素、全相同、交替错位、100值打断连续性，以及公共子序列较长但连续结果仅1的反例，核对int及输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
