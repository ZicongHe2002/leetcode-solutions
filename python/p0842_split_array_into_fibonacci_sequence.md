# 842. Split Array into Fibonacci Sequence · Python

[原题](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)。

每项必须是0..2^31-1，故最多10位；多位数不能以0开头。枚举前两项的所有可能结束位置，至少给第三项留一位。前两项确定后，后续每项由前两项之和唯一确定，直接将和转成规范十进制文本匹配当前位置，不再枚举后续分界。和超界或文本不匹配就放弃该前两项，消费完整串且项数至少3才返回。0以单字符0匹配，自动排除后续的多余前导0。

固定32位上限下至多100种前两项组合，每种沿串前进，时间O(N)，候选序列额外空间O(N)。输入保持，允许返回任意合法答案。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
