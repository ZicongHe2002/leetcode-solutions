# 964. Least Operators to Express Number · Python

[原题](https://leetcode.com/problems/least-operators-to-express-number/)。

表达式按x的幂展开，x^i在i>=1时需要i-1次乘法，加上连接前项的正负号按成本i计；单位1要写成x/x，含连接符成本2。逐x进制位处理，positive记录已处理低位直接表达的最小带连接成本，negative记录相对于下一位整幂的补数成本。当前位d可用d份当前幂相加，也可先从高位借1再减x-d份，因此两状态分别比较无进位与进位来源。最低位使用特殊单位成本2，结束时可直接用positive，或用一个x^exponent减去补数，最后统一减1去掉首项不存在的连接符。

x>=2、target正数，时间O(log_x target)，额外空间O(1)，全部用整数，不构造候选表达式文本。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
