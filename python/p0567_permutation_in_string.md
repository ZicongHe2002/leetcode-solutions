# 567. Permutation in String · Python

[原题](https://leetcode.com/problems/permutation-in-string/)。

原题s1与s2长1..10000，仅含小写英文，判断s2是否包含s1任意排列构成的连续子串。实现额外定义空s1返回True、空s2对非空s1返回False；字符串保持，返回bool。

balance是所需频次减当前窗口频次，missing是所有正缺口的总数。加入一个字符时，只有旧balance为正才减少missing，随后扣减balance；移出字符时先增加balance，只有新balance为正才增加missing。窗口长度固定在len(s1)，完整长度内missing为0就说明频次完全相同；不足完整长度时不可能填满所有缺口。时间O(len(s1)+len(s2))，额外空间O(26)。

独立oracle逐个连续切片比较Counter，不复用缺口标量。二字母s1长0..5、s2长0..7共16065对核对，空输入为扩展。边界覆盖10000字符、全部相同、末端才出现稀缺字符、模式更长及无匹配，核对bool。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。完整内容由B正式review；仅按真实内容署名。
