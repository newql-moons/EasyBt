import btsearch
from db import MagnetTab


if __name__ == '__main__':

    print('欢迎来到EasyBt v1.2.2')
    print('@author月梦书')
    print('------------------------------------------------------------------')
    print('------------------------------------------------------------------')

    while True:
        key = str(input('搜索关键词：'))
        if key == '':
            print('关键字不能为空！')
            continue
        while True:
            try:
                index = int(input('页码：'))
                break
            except ValueError:
                print('页码只能为数字!')

        data = btsearch.get_result(key, index)
        total = int(data['total'])

        print()
        print('搜索到{0}个结果...'.format('999+' if total > 999 else total))
        if total % 30 == 0:
            print('共 ' + str(int(total / 30)) + ' 页')
        else:
            print('共' + str(int(total / 30 + 1)) + '页')
        print()

        if total > 30 * (index - 1):
            infos = data['data']
            for hash_code, info in infos.items():
                day = info['day']
                hits = info['hits']
                size = info['size']
                title = info['title']

                # 备份数据
                dic = {
                    'hash': hash_code,
                    'day': day,
                    'hits': hits,
                    'size': size,
                    'title': title
                }
                tab = MagnetTab()
                tab.insert(dic)
                tab.close()

                # 转为gbk编码，预防无法在Windows控制台上不能正确输出
                print(title.encode('gbk', 'ignore').decode('gbk'))
                print('magnet:?xt=urn:btih:' + hash_code)
                print('日期：{0}\t大小：{1}\t点击量：{2}'
                      .format(day, size, hits))
                print()
        else:
            print('该页为空！')

        print('------------------------------------------------------------------')
        print('------------------------------------------------------------------')
