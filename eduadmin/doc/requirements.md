学籍管理系统
==========

## 刚性需求 ##

### 学籍数据库的有关语义 ###
+ 一个系可以若干专业, 每个专业每年可以招若干班, 每个班有若干学生
+ 系里对每个专业每年都制订了教学计划, 学生每年必须按照教学计划修完一定学分的课程
    >（必修课、限选课和任选课）, 如2000年入学的学生大三上学期必修课30学分, 限选课10学分, 任选课6学分
+ 系里的教师可以给多个班带课, 但是不能给一个班带多门课程
+ 一门课程最多允许学生一次补考, 学生达到如下条件之一的被开除
    + 一学期不及格的必修课学分超过10个
    + 不及格必修课学分累计超过30个
    + 不及格选修课学分累计超过20个

### 处理要求 ###
+ 查询学生所选修的课程及成绩, 并给出必修课平均成绩和选修课平均成绩
+ 查某一个学生被哪些教师教过课
+ 查询应被开除的学生（假定差2学分即被开除）

### 注意事项 ###
+ 在数据库的设计过程中需要运用规范化理论, 避免出现插入异常、删除异常、数据冗余等问题
+ 必须设定关系的完整性规则
    > 如实体完整性（例如设置主码）, 参照完整性（例如设置外码和对应的主码）, 用户自定义完整性（例如性别只能为“男”或“女”）
+ 可以使用索引来加快查询的速度
+ 可以使用视图来简化系统的设计

### 实验报告要求 ###
0. 需求分析（系统数据和功能）
0. 概念结构设计（E-R图设计）
0. 逻辑结构设计（E-R图转换为关系模型）
0. 应用程序设计（分析哪些需求由应用程序实现, 哪些由约束（触发器）实现）
0. 总结
