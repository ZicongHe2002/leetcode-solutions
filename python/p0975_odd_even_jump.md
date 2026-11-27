# 975. Odd Even Jump · Python

[原题](https://leetcode.com/problems/odd-even-jump/)。

奇跳选右侧不小于当前的最小值，偶跳选不大于当前的最大值，值相同取最小下标。分别按(值,下标)与(-值,下标)排序，在此顺序上用下标单调栈给更早下标匹配下一更大下标；值排序保证值优先级，下标升序保证同值最早优先。得到两类后继后，逆序令odd[i]=even[奇后继]、even[i]=odd[偶后继]，末位置两态都成功，答案为odd成功数。

时间O(n log n)，额外空间O(n)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
