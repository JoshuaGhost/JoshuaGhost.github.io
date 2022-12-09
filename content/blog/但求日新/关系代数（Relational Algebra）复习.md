Title: 关系代数（relational Algebra）复习
Date: 2022-12-09
Tags: Relationa Algebra, review

## 关系代数与SQL语句的等效性

大部分关系代数表达式可以与sql语句等价，比如

projection: $\pi_{\text{mat_no}}(Student)$就代表select mat_no from Student

selection: $\sigma_{gender='male'}(Student)$就等效于select * from Student where gender = ‘male’

另外还有一些集合操作，比如union ($\cup$), intersection ($\cap$), difference (\) cartesian product ($\times$)

还有比如各种join：inner join ($\bowtie$)

笛卡尔积-selection与inner join等效性：$R\bowtie_{condition}S \equiv \sigma_{condition}(R\times S)$

aggregation: 比如select name from student like avg(height) > 180 group by gender，就等效于 $\pi_{name}(\sigma_{\text{height}>{avg_height}}(\text{student} \bowtie (a_{\text{gender}} \mathcal{F}_{\text{avg(height)}}(\text{student}))))$ （忽略那个诡异的a，它只是个占位符，因为mathjax无力识别前置下标）。这里之所以在aggregation之后还要join一个原来的student表，是因为在aggregation之后，新的临时表格把所有的老attribution名都删除了：

![Untitled]({attach}关系代数（Relational Algebra）复习/Untitled.png)

## 例题

![Untitled]({attach}关系代数（Relational Algebra）复习/Untitled_1.png)

![Untitled]({attach}关系代数（Relational Algebra）复习/Untitled_2.png)

分析：这道题让选出所有符合下列要求的动物（返回这只动物的名字、物种、年龄和笼子编号），这只动物需要：

1. 是濒危动物status=”stark gefaehrdet”
2. 在其对应gruppe中，年龄超过平均年龄

要求1.翻译成关系代数，应该是 $\text{Tier}\bowtie\sigma_{\text{status}=\text{"stark gefährdet"}}(\text{Tierart})$

要求2.翻译成关系代数，应该是 $\text{Tier}\bowtie\text{  }\text{Tierart}\bowtie(a_\text{gruppe}\mathcal{F}_\text{avg(alter)}(\text{Tier}\bowtie\text{Tierart}))$

所以选出所有符合这一条件的动物，应该是

<!-- $$
\text{Tier}\bowtie\text{  }\text{Tierart}\bowtie(a_\text{gruppe}\mathcal{F}_\text{avg(alter)}(\text{Tier}\bowtie\text{Tierart}))\bowtie\sigma_{\text{status}=\text{stark gefaehrdet}}(\text{Tierart})
$$ -->
![Untitled]({attach}关系代数（Relational Algebra）复习/CodeCogsEqn.png)


然后把所有这样的动物的笼子也找出来，就需要再join一个Lebt_in表：

<!-- $$
\begin{split}\pi&_{name, bezeichnung, alter, nr}(\\&\sigma_{\text{alter}>\text{avg\_alter}\wedge\text{status="stark gefährdet"}}(\\&\text{ }\text{ }\text{ }\text{Tier}\bowtie\text{  }\text{Tierart}\bowtie(a_\text{gruppe}\mathcal{F}_\text{avg(alter)}(\text{Tier}\bowtie\text{Tierart}))\\&)\bowtie\sigma_{\text{status="stark gefährdet}"}(\text{Tierart})\bowtie\text{Lebt\_in}\\)\end{split}
$$ -->
![Untitled]({attach}关系代数（Relational Algebra）复习/eq2.png)

1h 10~15min ti
12.12 14:00