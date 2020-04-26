"""
  作者
  功能
  版本
  日期

"""

def count_bmr(gender,weight,height,age):
    if gender == '男':

        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女':
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    else:
        bmr = -1

    if bmr != -1:
        print('您的性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}岁'.format(gender, weight, height, age))
        print('您的基础代谢率：{}大卡'.format(bmr))
    else:
        print('暂不支持该性别！')


def main():
    """

    :return:
    """

    y_or_n ='n'
    while y_or_n != 'y':
        print('BMR计算，请输入以下信息，以空格分割，例：男 62 173 50')
        input_str=input('性别 体重（kg） 身高（cm） 年龄： ')
        str_list=input_str.split(' ')

        try:

            gender = str_list[0]

            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[3])
            count_bmr(gender,weight,height,age)
        except ValueError:

            print('请输入正确的信息！')
        except IndexError:
            print('您输入的信息太少！')
        except:
            print('程序异常！')

        # #性别
        # gender = input('性别:')
        # #体重
        # weight = float(input('体重（kg）:'))
        # #身高
        # height = float(input('身高（cm）:'))
        # #年龄
        # age=int(input('年龄：'))



        print('*******************************')
        y_or_n =input('是否继续计算BMR，输入“y”退出程序？')

if __name__ == '__main__':
    main()
