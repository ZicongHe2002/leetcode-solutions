# 831. Masking Personal Information · Python

[原题](https://leetcode.com/problems/masking-personal-information/)。

邮箱包含@，统一小写后只保留名称首尾字符，中间恰好五个星号，域名保留小写完整文本。电话先丢弃分隔符，只保留数字；本地10位写成***-***-末四位，多于10的前缀是1..3位国家码，输出加号、相同数量星号和连接横杠。不把原分隔符复制到结果，输入保证符合一种合法类型。

时间O(n)，额外空间O(n)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
