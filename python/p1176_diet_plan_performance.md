# 1176. Diet Plan Performance · Python

[原题](https://leetcode.com/problems/diet-plan-performance/)。

每个连续k天窗口独立评分，和低于lower减1，高于upper加1，落在闭区间内加0。每步加入新一天，窗口超长就减掉k天前的值，只有凑满k天才评分。恰好等于任一阈值不加减分，窗口允许重叠，不能按不重叠的k天分块。

时间O(n)，额外空间O(1)，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
