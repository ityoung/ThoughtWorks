# ThoughtWorks Homework 2017-chengdu

##如何运行？

###环境要求
python2.7

###运行作业：
* 运行：
  * IDE运行作业代码animal.py；
  * **或**console进入代码目录后运行 `python animal.py`；
* 输入：
  * 按行输入historyData；
  * **或**直接复制粘贴整段测试数据；
```BASH
e4e87cb2-8e9a-4749-abb6-26c59344dfee
2016/09/02 22:30:46
cat1 10 9
351055db-33e6-4f9b-bfe1-16f1ac446ac1
2016/09/02 22:30:52
cat2 2 3
cat1 10 9 2 -1
dcfa0c7a-5855-4ed2-bc8c-4accae8bd155
2016/09/02 22:31:02
cat1 12 8 3 4
```
* 输入最后一行animal数据后，**回车**结束该行数据，**再次回车**结束historyData数据的输入:
 
>此处为historyData最后一组数据cat1 12 8 3 4

>至少一个空行

>此处输入id
 
* 验证输出结果正确性:

>当输入id为`dcfa0c7a-5855-4ed2-bc8c-4accae8bd155`时，输出内容如下：

>cat1 15 12

>cat2 2 3
 
###运行测试：
* 将测试代码animal_test.py与作业代码animal.py放在**同一目录**；
  * IDE运行测试代码animal_test.py；
  * 或console进入代码目录后运行 `python animal_test.py`；
* 查看测试结果:

>Ran 6 tests in 0.012s

>OK

***
