"""
 * Project name(项目名称)：Python_try_except_finally
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:24
 * Version(版本): 1.0
 * Description(描述)： finally 语句的功能是：无论 try 块是否发生异常，最终都要进入 finally 语句，并执行其中的代码块。
 """

if __name__ == '__main__':
    try:
        a = int(input("请输入 a 的值:"))
        print(20 / a)
    except:
        print("发生异常！")
    else:
        print("执行 else 块中的代码")
    finally:
        print("执行 finally 块中的代码")
