# 966. Vowel Spellchecker · Python

[原题](https://leetcode.com/problems/vowel-spellchecker/)。

匹配优先级是原字符完全相同、忽略大小写、再忽略元音差异。后两类都要求返回词表中最早的原词，因此顺序建立映射并用setdefault保留首次出现。元音键把小写a/e/i/o/u统一替为*，辅音位置和词长仍须相同。查询逐级匹配，不能让较早的宽松匹配覆盖更高优先级精确匹配。

总字符数L，期望时间O(L)，词表索引与结果总空间O(L)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
