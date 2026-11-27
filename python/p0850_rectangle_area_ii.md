# 850. Rectangle Area II · Python

[原题](https://leetcode.com/problems/rectangle-area-ii/)。

每个矩形在左边界加入纵区间、右边界删除。相邻不同x之间活动矩形集合不变，面积是横向宽度乘纵区间并长。相同x事件先分组，先累计上一条带，再统一更新活动区间，避免零宽事件影响面积。Counter保留相同纵区间的多重出现，最后一份离开才删除。纵区间按下界排序合并，只增加未覆盖部分，重叠不重复计算。

R个矩形最多2R次不同x，采用每次重排活动区间的实现，时间O(R^2 log R)、额外空间O(R)。按题目要求对10^9+7取模，坐标乘法由Python整数处理。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
