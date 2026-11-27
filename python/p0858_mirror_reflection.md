# 858. Mirror Reflection · Python

[原题](https://leetcode.com/problems/mirror-reflection/)。

把反射展开为穿过镜像房间的直线，首次到达角点时横向经过p/gcd(p,q)个房间、纵向经过q/gcd(p,q)个房间。横数偶则折回左墙，约分互质保证纵数奇，到左上接收器2；横数奇到右墙，纵数奇为右上1、纵数偶为右下0。q=0由gcd约分自然得到右下0，不模拟多次反弹。

欧几里得算法时间O(log p)，额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
