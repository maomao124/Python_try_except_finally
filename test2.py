"""
 * Project name(项目名称)：Python_try_except_finally
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:26
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    try:
        a = int(input("请输入 a 的值:"))
        print(20 / a)
    finally:
        print("执行 finally 块中的代码")
