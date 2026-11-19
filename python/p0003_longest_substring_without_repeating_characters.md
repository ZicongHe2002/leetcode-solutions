# 3. Longest Substring Without Repeating Characters · Python

[原题](https://leetcode.com/problems/longest-substring-without-repeating-characters/)求连续且无重复字符的最长子串长度。使用`Solution.lengthOfLongestSubstring`，不把子串与可以跳过字符的子序列混淆。

字典记录每个字符最近出现的位置，窗口[left,right]始终无重复。新字符曾在窗口中出现时，将left推进到旧位置之后；若旧位置已在窗口外，则保持left。代码使用max保证left不倒退。以`abba`为例，第二个b将left推到2，最后的a曾在0出现，不能把left退回1，否则错误地把`bba`算成无重复。

处理完当前位置后登记最新下标，并用窗口长度更新best。每个位置扫描一次，哈希表操作按平均常数时间估计，预期时间O(n)，额外空间O(min(n,字符种类数))；没有为每个窗口复制切片。Python按字符串码点遍历，不将多个码点构成的显示字形当成一个字符。

测试用枚举全部子串并检查set大小的独立oracle，覆盖字母表abc、长度0至7的全部3280个字符串，另含典型样例与left倒退反例。实际运行情况在PR中记录；没有LeetCode Accepted记录。A实现，OpenAI Codex辅助整理。

## B补写：窗口外的历史位置

`tmmzuxt`展示“字典仍记住旧字符，但旧字符已不在当前窗口”的情况。latest列记录更新前当前字符的旧位置：

| right/字符 | latest旧位置 | left更新前→后 | 当前窗口 | best |
| --- | --- | --- | --- | --- |
| 0 / t | 无 | 0→0 | t | 1 |
| 1 / m | 无 | 0→0 | tm | 2 |
| 2 / m | 1 | 0→2 | m | 2 |
| 3 / z | 无 | 2→2 | mz | 2 |
| 4 / u | 无 | 2→2 | mzu | 3 |
| 5 / x | 无 | 2→2 | mzux | 4 |
| 6 / t | 0 | 2→2 | mzuxt | 5 |

最后一步若直接令left=0+1，就会把已排除的下标1重新纳入，得到含两个m的`mmzuxt`并错误记录6。`max(left, latest[t]+1)`只保留当前候选区间或向右缩小。先更新left，再登记latest并计算长度，使无重复不变量在测量长度时成立。该表由B补写；字典允许保存窗口外历史，无需为正确性逐项删除它们。
