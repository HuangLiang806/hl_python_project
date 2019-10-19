import re
import time
import threading
import urllib.request as req

__author__ = "huangliang"


class MyThread(threading.Thread):
    def __init__(self, target, args=()):
        """
        why: 因为threading类没有返回值,因此在此处重新定义MyThread类,使线程拥有返回值
        此方法来源 https://www.cnblogs.com/hujq1029/p/7219163.html?utm_source=itdadao&utm_medium=referral
        """
        super(MyThread, self).__init__()
        self.func = target
        self.args = args

    def run(self):
        # 接受返回值
        self.result = self.func(*self.args)

    def get_result(self):
        # 线程不结束,返回值为None
        try:
            return self.result
        except Exception:
            return None

# 为了限制真实请求时间或函数执行时间的装饰器
def time_limit_decor(limit_time):
    """
    :param limit_time: 设置最大允许执行时长,单位:秒
    :return: 未超时返回被装饰函数返回值,超时则返回 None
    """

    def functions(func):
        # 执行操作
        def run(*params):
            thre_func = MyThread(target=func, args=params)
            # 主线程结束(超出时长),则线程方法结束
            thre_func.setDaemon(True)
            thre_func.start()
            # 计算分段沉睡次数
            sleep_num = int(limit_time // 1)
            sleep_nums = round(limit_time % 1, 1)
            # 多次短暂沉睡并尝试获取返回值
            for i in range(sleep_num):
                time.sleep(1)
                infor = thre_func.get_result()
                if infor:
                    return infor
            time.sleep(sleep_nums)
            # 最终返回值(不论线程是否已结束)
            if thre_func.get_result():
                return thre_func.get_result()
            else:
                return"请求超时"  #超时返回  可以自定义

        return run

    return functions


@time_limit_decor(3)
def get_save_page(url):
    '''
    获取网页源码并保存到文件
    :param url: 输入网址
    :return: True
    '''
    file_data = open("ogre_source_temp.txt", "ab")
    req_obj = req.urlopen(url)
    source_data = req_obj.read()
    print("get done")

    # 将网页源代码追加到文件
    file_data.write(source_data)
    print("save done")
    file_data.close()
    return True


def get_souce():
    # 打开文件 预备读取地址文件
    file_addr = open("address_1.txt", "r", encoding='utf-8')
    # 获取网页地址
    url_start = "https://ogrecave.github.io/ogre/api/1.10/"
    line = 'start'
    count = 0
    while line != '':
        try:
            line = file_addr.readline()
            print(line)
            re_obj = re.search(r"(,{1}).*(\"[a-zA-Z-_.#0-9]*\")", line)
            address = re_obj.group(2)
        except:
            print("匹配%s失败" % line)
            continue
        url = url_start + address[1:-1]

        # 获取并保存网页源代码
        count += 1
        print("-------------------%d-----------------" % count)
        print("start get %s" % url)
        get_save_page(url)


    file_addr.close()



# 从网页源码文件中提取出段落
def find_text(file_source, file_result):
    file_sou = open(file_source, "r", encoding='utf-8')
    file_res = open(file_result, "w", encoding='utf-8')
    string = file_sou.read()
    string_match = re.findall(r"(<p>)(.*)(<\/p>)", string)
    file_res.write(str(string_match))

    file_sou.close()
    file_res.close()
    return None

# 从段落中提取单词，输出规定格式到文件
def find_word(file_source, file_result):
    file_sou = open(file_source, "r", encoding='utf-8')
    file_res = open(file_result, "w", encoding='utf-8')
    string = file_sou.read()
    word_match = re.findall(r"[a-zA-Z]{3,}", string)

    # 去除重复单词
    set_word = set(word_match)

    # 每行一个单词，保存到文件
    for word in set_word:
        file_res.write(word + '\n')

    file_sou.close()
    file_res.close()
    return None



def main():
    # 获取网页源代码
    # get_souce()


    # 将源代码中的段落部分提取出来
    # find_text("ogre_source_1.txt", "ogre_find_1.txt")
    #
    find_word("ogre_find_1.txt", "ogre_word_1.txt")



if __name__ == "__main__":
    main()
