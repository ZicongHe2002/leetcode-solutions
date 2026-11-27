# 1163. Last Substring in Lexicographical Order · Python

[原题](https://leetcode.com/problems/last-substring-in-lexicographical-order/)。

对任意固定起点，延伸到串尾的后缀不小于该起点的任何更短子串，所以答案必是最大后缀。比较候选first与second，相等就延长offset；首次不同后，较小候选及其相等前缀内部对应起点都受同样字符差支配，可整体跳过offset+1个位置。若第二候选获胜，first至少前进到second，始终保持first<second；比较到串尾时保留first。

双指针淘汰使总比较数O(n)，除返回切片O(n)外额外空间O(1)，不创建所有后缀。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
