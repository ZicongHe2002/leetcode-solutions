# 836. Rectangle Overlap · Python

[原题](https://leetcode.com/problems/rectangle-overlap/)。

轴对齐矩形的交集面积是横投影交长乘纵投影交长，两者必须都严格大于0。交集左界取较大左界、右界取较小右界，纵向同理。使用严格小于，只有边或角接触时返回False；负坐标不影响比较。不计算面积乘积。

时间与额外空间均O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
