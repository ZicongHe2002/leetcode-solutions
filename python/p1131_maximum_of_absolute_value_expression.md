# 1131. Maximum of Absolute Value Expression · Python

[原题](https://leetcode.com/problems/maximum-of-absolute-value-expression/)。

目标是|arr1[i]-arr1[j]|+|arr2[i]-arr2[j]|+|i-j|。每个绝对值展开为两种符号，对固定符号组合，最大差就是线性变换值的极差。整体翻转三个符号只会把差反向，极差不变，所以固定下标系数为+1，只枚举另外两个系数的四种组合即可覆盖全部情况。输入两数组等长且非空。

时间O(n)，额外空间O(1)，不建立变换数组，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
