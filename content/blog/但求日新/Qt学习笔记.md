Title: Qt6学习笔记
Date: 2022-12-23
Tag: 自学, Qt, C++

## 1
main window的三种基类：
QMainWindow有toolbar
QWidget和QDialog是没有toolbar的

## 2
cpp的explicit标识符，如果写了，就表示这个类是explicit的，否则就叫一个implicit类，对于一个implicit类，如果他的构造函数只有一个参数，那么可以把这个类的类名用类似强制类型转换的方式使用，比如：
```cpp
class Foo {
	private:
		int m_foo;

	public:
		Foo(int foo): m_foo(foo) {} //这里的冒号标识符是用来initialization的。有两种用法，一是用来直接调用父类的构造函数，二是用来初始化某些值的，这里等效于m_foo = foo;，作用是在构造函数运行之前就执行这个赋值语句。如果被赋值的变量m_foo是const int m_foo;，那么在构造函数体里面不能直接给它赋值，而用这种冒号的赋值语句是可行的。如果要调用多个父函数的构造函数，或者要给多变量赋值，那多个冒号表达式用逗号隔开

		int GetFoo() { return m_foo; }
}
```

## 3
QT的stylesheet可以用类似css的方法自定义widget的样式，比如定义所有的QPushButton的背景颜色为黄色：
```CSS
QPushButton{
	background yellow;
}
```
注意如果选择更改了主窗口的样式，那主窗口下所有的按钮都会改变，因为这些窗口都是主窗口的后代widget，如果想仅改变其中一个widget的样式，可以用QPushButton#button_no_1这样的id选择器来选择特定widget，或者直接对widget本身的样式进行修订

## 4
如果在qt的design界面更改了控件的名字，则需要先构建一次才能在编辑窗口使用代码补全

## 5
cpp的标准模板库的vector，使用方法是：

```cpp
std::vector<type> variable_name = {value1, value2};
```

比如我要用一个vector装载radiobox_{1..3}的指针，就可以

```cpp
std::vector<QRadioBox *> radio_boxes = {radiobox_1, radiobox_2, radiobox_3};
```

之后用一个循环变量去便利vector里面的所有内容，就可以

```cpp
for (QRadioBox * i: radio_boxes){
	do_something();
}
```

另外QT中还自己有一个QStringList，定义方法与vector相近：

```cpp
QStringList items = {"d", "e", "f"};
```

循环也可以用foreach：

```cpp
foreach (QString item, items) {
	do_something();
}
```

## 6
QT中有不同的message boxes可供提示使用，它们在QMessageBox命名空间下边，分别是

```cpp
QMessageBox::information
QMessageBox::warning
QMessageBox::about
QMessageBox::question
```

使用的时候，以question box为例，它的第一个参数是父窗口的指针，第二个是标题字符串，第三个是信息字符串，如果是question box的话，还有第四个参数，一般设置为QMessageBox::Yes|QMessageBox::No，前者是16384（2^14，即第15位有一个1），后者是65536（2^16，即第17位有一个1），两者进行bit-wise或得到的一个bitmap，即

```cpp
QMessageBox::question(this, "Title of the question box", "Do you answer yes or no?", QMessageBox::Yes|QMessageBox::No);
```

question box的回复，是一个QMessageBox::StandardButton的值，比如说我可以这样获取question box的回复：

```cpp
QMessageBox::StandardButton reply;
reply = QMessageBox question(this, "Title", "Question", QMessageBox::Yes|QMessageBox::No);

if (reply == QMessageBox::Yes) {
	do_something_for_answering_yes();
} else if (reply == QMessageBox::No) {
	do_smething_for_answering_no();
}
```

## 7
创建项目的时候记得要用qmake来构建整个项目，而不要用cmake，否则会无法添加resource文件

## 8
设置textEdit的字体
```cpp
bool ok
Qfont font = QFontDialog::getFont(&ok, QFont("Times New Roman", 12), this);
if (ok) {
	ui->textEdit->setFont(font);
}
```
这会更改整个textedit的文字字体，无论有没有选中文本

下面一段代码可以更改选中部分的文字字体：
```cpp
	bool ok;
    QFont font = QFontDialog::getFont(&ok, QFont("Helvetica[Cronyx]", 12), this);

    QTextCharFormat format;
    format.setFont(font);
    if (ok) {
        ui->textEdit->textCursor().setCharFormat(format);
    }
```

设置textColor
```cpp
bool ok
QColor color = QColorDialog::getColor(QT::yellow, this);
ui->textEdit->setTextColor(color);
```
这个只会更改选中部分的文字颜色

设置打印对话框
```cpp
QPrinter printer;
QPrintDialog dialog(&printer, this);
dialog.setWindowTitle("Print Document");

if (ui->textEdit->textCursor().hasSelection()) {
	dialog.setOption(QAbstractPrintDialog::PrintSelection);
}

if (dialog.exec() != QDialog::Accepted) {
	return;
}
```