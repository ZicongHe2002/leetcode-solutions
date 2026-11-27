# 1058. Minimize Rounding Error to Meet Target · Python

[原题](https://leetcode.com/problems/minimize-rounding-error-to-meet-target/)。

每价格有三位小数，先全部向下取整，差target-lower_sum就是必须向上取整的非整数项数，超出0..可上取整数则无解。小数部分为f千分位时，下取整误差f，上取整误差1000-f，改向上的代价变化为1000-2f，所以应选f最大的指定项数。整数项上下取整相同，不能增加总和，不加入候选。全程整数千分位，最后固定三位格式化，不用浮点舍入。

时间O(n log n)，额外空间O(n)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
