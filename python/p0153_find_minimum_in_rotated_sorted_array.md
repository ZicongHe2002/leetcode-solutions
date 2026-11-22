# 153. Find Minimum in Rotated Sorted Array · Python

[原题](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)。

长度1..5000，值[-5000,5000]，互异元素来自严格递增数组的一次旋转，返回最小值。输入必须非空；重复值属于另一题合同。维护包含最小值的闭区间[left,right]，比较中点与右端：中点更大说明下降及最小值在其右侧，left=middle+1；否则最小值可能就是中点，right=middle保留它。

互异旋转数组中，中点大于右端时，中点仍在较高的旋转前段，最小值在(middle,right]；否则[middle,right]已经递增，这一段的最小值是中点，整体最小值只能在[left,middle]。两种更新保持候选且严格缩小，终止为同一下标即最小值。未旋转数组、单元素和最小值恰在端点均符合证明。时间O(log n)，额外空间O(1)，输入保持。

独立oracle线性取min。七值集合所有非空子集的全部448个旋转均核对；另外检查5000长度上0/1/1234/4999四个旋转位置、值域两端、单项与两项。大数组使用构造已知最小值，不把生产搜索结果作为期望。

A使用OpenAI Codex辅助编写；测试范围和实际结果见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
