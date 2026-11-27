# 929. Unique Email Addresses · Python

[原题](https://leetcode.com/problems/unique-email-addresses/)。

按@拆为本地名和域名。题目规则只在本地名生效：第一个+及其后文本忽略，剩余部分所有点忽略；域名的点与加号不能按本地规则删除。将规范本地名与原域名重新连接放入集合，大小即不同实际收件地址数，不修改输入。

全部地址总长度L，期望时间与额外空间O(L)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
