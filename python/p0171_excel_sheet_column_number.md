# 171. Excel Sheet Column Number · Python

[原题](https://leetcode.com/problems/excel-sheet-column-number/)。

原题列名长1..7，仅大写字母，处于Excel列序A到FXSHRXW对应的合法范围，即数值不超过2^31-1。A..Z表示1..26；字符串AAAAAAA合法，但并非任意七字母组合都在数值上界内。

从左到右读取，number始终是已读前缀的列编号。追加一个字母时，旧前缀全部位权提高一位，先乘26，再加当前字母的1..26数值。归纳得到完整列编号，不需要减1或把A当成0。时间O(L)，额外空间O(1)，整数上界由原题保证。

独立参考从右向左把每个字母值乘对应26的幂后求和，不复用逐位Horner累积。全部1..3字母的18278个列名逐一核对，另覆盖A/Z/AA/ZZ/AAA、AAAAAAA与最大FXSHRXW，检查结果为int且在合法范围内。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
