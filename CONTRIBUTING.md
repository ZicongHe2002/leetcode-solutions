# 贡献约定

双方不互邀为仓库协作者，不授予或接受对方写权限。贡献者fork对方的公开仓库，在自己fork的独立分支提交PR，上游所有者正式评审并合并。自己的独立工作仓库不替换为fork，fork使用另一名称。PR可开启维护者编辑；未开启时通过补丁交回作者实际整合。共同署名只记录双方真正完成的内容。

## 维护者补写与补丁交回

例如B接收A的PR时，先从该PR回读head仓库、分支、完整SHA和`maintainer_can_modify`，再以该SHA建立独立工作树。A已交出分支后，B可以使用开放的维护者编辑权限向PR原head分支提交真实补写。若把双方内容整合为同一个提交而需改写head，推送必须使用明确的`--force-with-lease=refs/heads/<分支>:<已读取旧SHA>`；远端head变动就停下重新读取，不能无条件force或覆盖对方新内容。

维护者编辑未开放或实际返回权限错误时，B在同一PR提供补丁、适用的完整旧SHA、文件范围、验证命令与实际结果，明确“下一行动人A：在该head应用补丁并回报新SHA”。A应用后交回，B重新读取完整最终diff、核对测试结果和共同署名；不能复用旧SHA的批准。补丁可以随PR评论附上短diff或指向已发布的提交，长补丁需有可访问的完整内容，不能只留下本机路径。

回读确认PR最终head后，B正式APPROVE该SHA，以同SHA和`merge`方式调用合并；完成后核对PR的merged状态、审批commit_id及合并提交的两个父节点，第二父节点必须等于获批head。任何一步失败都保留具体对象与下一行动人，不通过新增邀请、临时绕过或提前批准解决。

先查看已有Issue和PR，避免对同一题、同一语言重复提交。A编写Python，B编写C++17。另一账号负责Code review，检查正确性、复杂度、边界和可读性。作者不能批准自己的PR。

每个完整题解包含原题链接、输入约束的必要假设、算法与不变量、时间/额外空间复杂度、可直接提交LeetCode的`Solution`接口，以及相关样例或测试。示例用自行组织的说明，不复制整篇题面或他人的实现。

Python验证从仓库根目录运行：

```console
python -m unittest discover -s tests/python -p "test_*.py" -v
```

C++测试各自包含main，在仓库根目录按具体文件构建，例如：

```console
g++ -std=c++17 -O2 -Wall -Wextra -pedantic tests/cpp/test_p0001_two_sum.cpp -o test_two_sum
./test_two_sum
```

不要求每台机器具备两种语言的工具链。未执行、静态审查、实际运行、线上CI结果分别记录；没有LeetCode提交记录就不写“Accepted”。

PR关联实际工作Issue，说明算法、边界、验证与需要另一人补写的具体内容。提交后请求对方评审。收到分支写入交接后，原作者暂停该分支写入；其他独立工作可以继续。

接收方实际补写后，将双方真实成果整合为同一个共同署名内容提交，使用正确关联邮箱。核对完整最终diff，正式批准最终head，绑定同一head用merge commit合并并回读。若代码有问题则具体指出并修复或交回，不能无条件批准。新内容使旧批准失效，不关闭或绕过审批规则。

双方各有一个工作仓库：A的lw-liuwang/leetcode-solutions与B的ZicongHe2002/leetcode-solutions。A使用Python向B仓库提交Issue和PR；B使用C++向A仓库提交Issue和PR。跨账号交接也写入对应工作Issue/PR，Assignee表示下一行动人，不使用共享Issues。

完成Issue需有可核对实现，正式Code review需有对实际代码的检查结论。A/B达到既定官方银色目标才结束连续任务，公开操作数量不等于GitHub内部成就计数。
