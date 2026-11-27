# 943. Find the Shortest Superstring · Python

[原题](https://leetcode.com/problems/find-the-shortest-superstring/)。

先去重复与被其他词包含的冗余词。剩余词没有包含关系，可按它们在超级串中的先后次序拼接，相邻词采用最大前后缀重叠。预计算每对词的有向重叠长度，best[mask][last]保存覆盖mask且以last词结尾的最短文本；追加未选词只添加扣除重叠后的后缀。相同集合和末词下，后续追加成本只依赖末词，所以只保留最短文本即可。全覆盖末词中取最短，长度同优时任意一个均可。

N个保留词、全部拼接长度上界L，时间上界O(N^2 L^2+2^N N^2 L)，空间O(2^N NL)，包含实际字符串构造，未把字符串拼接视为常数时间。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
