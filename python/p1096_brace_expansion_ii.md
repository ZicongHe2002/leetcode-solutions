# 1096. Brace Expansion II · Python

[原题](https://leetcode.com/problems/brace-expansion-ii/)。

题目输入是合法表达式，支持嵌套花括号、逗号并集以及相邻表达式连接。每层用product保存当前逗号项的全部连接结果，以空字符串集合为连接单位元；遇到逗号，将当前项并入union并重置product。遇到左括号递归解析到匹配右括号，把返回集合作为一个因子参与连接。集合会自动去重，最终排序输出。例如{a,b}{c,{d,e}}得到ac、ad、ae、bc、bd、be。

设输入长N、最长展开串长L、输出数P，解析中实际枚举的拼接对总数为T，时间O(N+TL+PL log P)。空间取决于递归栈及中间字符串集合，最坏随输入指数增长，因为结果集合本身也可能指数增长；不宣称线性解析即可在线性空间输出所有组合。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
