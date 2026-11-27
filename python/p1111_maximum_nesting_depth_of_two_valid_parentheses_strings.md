# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings · Python

[原题](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)。

输入是有效括号串，输出每个括号属于0组或1组。左括号先增加深度再按奇偶分组，右括号先按当前深度分组再减少深度，因此每对匹配括号一定同组，且每组保留子序列仍是有效括号串。若原串最大嵌套深度为D，两组分担嵌套链，任一方案最大组深度至少ceil(D/2)；交替分组恰好达到这个下界。不能在右括号先减深度后再分组，否则会拆散匹配对。

时间O(n)，输出空间O(n)，除输出外额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
