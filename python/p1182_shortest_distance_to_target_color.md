# 1182. Shortest Distance to Target Color · Python

[原题](https://leetcode.com/problems/shortest-distance-to-target-color/)。

颜色仅1、2、3，下标从0开始。按原数组扫描得到每色递增位置表。查询位置的最近目标色只可能是二分插入点或它前一项，其他同色位置更远。若目标色不存在返回-1，当前格已经是目标色时距离为0；不把颜色编号差当作位置距离。

时间O(n+q log n)，额外空间O(n+q)，不修改输入数组或查询。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
