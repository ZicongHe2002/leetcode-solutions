# 206. Reverse Linked List · Python

[原题](https://leetcode.com/problems/reverse-linked-list/)将一个无环单链表反转。保留`Solution.reverseList`，直接修改原节点的next并返回原尾节点，不创建结果节点。文件提供本地`ListNode`；线上可使用题目提供的节点定义。

previous是已经反转的前缀头，current是尚未处理后缀的头。必须先保存following=current.next，再将current.next指向previous，否则会失去未处理的后缀。之后把previous推进到current，再用following推进current。循环结束时后缀为空，previous就是完整反转后的头。

两个部分始终恰好覆盖原节点，已经处理的节点每次增加一个。初始previous=None保证原头最终成为尾节点且next=None；空输入自然返回None。节点值保持不变，节点身份仅改变访问顺序。时间O(n)，额外空间O(1)，不使用递归。输入必须无环；本题不兼做环检测。

测试覆盖取值−1至1、长度0至6的全部1093个链表，用原节点数组的反序逐一核对身份、值及终止None，再反转一次检查恢复完整原结构；包括空链表、单节点和重复值。实际运行结果写入PR；没有LeetCode Accepted记录。A实现，OpenAI Codex辅助整理。

## B补写：保存后继与不丢节点证明

输入`A(-1)→B(2)→C(2)→D(5)→None`，B与C值相同但身份不同。每行描述一次完整循环，following在改写next前保存：

| 改写前previous | 改写前current | 保存的following | 本轮后previous | 本轮后current | 本轮后反转前缀 |
| --- | --- | --- | --- | --- | --- |
| None | A | B | A | B | A→None |
| A | B | C | B | C | B→A→None |
| B | C | D | C | D | C→B→A→None |
| C | D | None | D | None | D→C→B→A→None |

在每轮入口，previous所指的已反转前缀与current所指的原序后缀不交叠，合起来恰是全部原节点。保存following保留了后缀除头节点之外的入口；改写current.next只把这一头节点转移到前缀，随后更新两个入口，因此下一轮仍完整覆盖原节点。每轮后缀少一个节点，无环有限输入必终止。

若首轮先做`A.next=None`，再从A.next读取following，就只读到None，B、C、D从这组遍历指针中丢失，无法继续反转。保存后继不是可交换的语句顺序。空输入不会进入循环；单节点首轮following=None，最后返回原节点且next=None。B实际补写此指针表与节点守恒证明。
