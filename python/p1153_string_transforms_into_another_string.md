# 1153. String Transforms Into Another String · Python

[原题](https://leetcode.com/problems/string-transforms-into-another-string/)。

每步把一种小写字符的全部出现同时替换，因此同一源字符必须始终指向同一目标字符；源a在不同位置分别要变成b和c时无解。映射一致后，无环依赖可逆拓扑顺序替换，有环需要一个不出现在最终字符串中的字符暂存，才能避免提前合并后无法分离。若目标使用全部26个字母，非恒等的可行映射必含无法借空字符打破的置换环，故返回False。两串原本相同时不必执行任何替换，直接True。题目保证两串等长且仅含小写字母。

时间O(n)，固定字母表下额外空间O(1)，不实际构造替换过程。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
