# 635. Design Log Storage System · Python

[原题](https://leetcode.com/problems/design-log-storage-system/)。

本题接口为LogSystem、put(id,timestamp)和retrieve(start,end,granularity)。ID在1..500且每条日志ID唯一，时间格式为零补齐的Year:Month:Day:Hour:Minute:Second；年2000..2017、月1..12、日1..31、时0..23、分秒0..59，最多500次公开调用。日期分量按题目范围处理，不额外要求真实日历中每月都含该日。粒度为Year/Month/Day/Hour/Minute/Second之一，返回闭区间中全部日志ID，结果顺序不限。

固定宽度、从高位到低位的十进制字段让字典序与时间分量顺序一致。按粒度分别截取4/7/10/13/16/19个字符，恰好保留该字段及更高字段；把日志和两端都截到相同长度再作lower<=prefix<=upper。被忽略的低位不参与筛选，不需把结束时间加一，也不受月末、年末或闰年日期运算影响。

put直接追加，允许相同时间戳对应多个不同ID；不依赖插入时间有序，retrieve从全部已存日志逐条筛选，保留插入顺序作为一种合法输出，不修改日志。设已存m条、命中r条，put均摊O(1)，retrieve时间O(m)，返回列表空间O(r)，持久空间O(m)；字符串长度固定19，不把线性扫描误写为对数查询。

独立oracle将六个字段解析为整数元组，按字段数量截取并比较，不使用生产字符前缀长度。固定种子存150条乱序日志，再作350次查询，共500次公开调用，覆盖全部六种粒度。另检查空存储、相同日低位不同仍纳入、秒级闭区间、2000/2017边界、重复查询不改变状态；最大调用用499个不同ID共享一个时间戳，再查询一次，确认全部保留。没有LeetCode提交记录。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
