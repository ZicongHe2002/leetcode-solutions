# 1073. Adding Two Negabinary Numbers · Python

[原题](https://leetcode.com/problems/adding-two-negabinary-numbers/)。

低位和total包含两输入位及上轮进位，当前结果位必须为0或1，由total&1取奇偶。剩余进位满足total=bit+(-2)*carry，所以用(total-bit)//-2更新，可能为负，不可套用普通正二进制进位。输入耗完后仍要处理非零进位，逆序结果去高位0但至少保留一个0，最后反转。输入数组不修改。

时间O(N+M)，结果空间O(N+M)，除输出外额外状态O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
