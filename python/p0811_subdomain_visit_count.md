# 811. Subdomain Visit Count · Python

[原题](https://leetcode.com/problems/subdomain-visit-count/)。

访问完整域名也访问去掉左侧若干标签后的每个后缀。按空格拆出次数和域名，再按点拆标签，逐一拼接这些后缀并累计。只在标签边界切分，不把普通字符串后缀误认为子域名。不同输入的相同子域共享计数，输出顺序任意，输入保持。

以全部生成的域名后缀总字符数为L，期望时间O(L)，额外空间为所有不同子域名及结果总大小。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
