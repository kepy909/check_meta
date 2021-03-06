# coding=utf-8
import re

import xlrd


class CheckMeta(object):
    def __init__(self, file):
        self.file = file

    # 打开excel文件
    def open_excel(self):
        try:
            data = xlrd.open_workbook(self.file)
            return data
        except Exception as e:
            print(str(e))

    # 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
    def excel_table_byname(self, colnameindex=0, by_name=u'Sheet1'):
        data = self.open_excel()  # 打开excel文件
        try:
            table = data.sheet_by_name(by_name)  # 根据sheet名字来获取excel中的sheet
        except Exception:
            table = data.sheet_by_index(0)
        nrows = table.nrows  # 行数
        colnames = table.row_values(colnameindex)  # 某一行数据
        list = []  # 装读取结果的序列
        for rownum in range(0, nrows):  # 遍历每一行的内容
            row = table.row_values(rownum)  # 根据行号获取行
            if row:  # 如果行存在
                app = []  # 一行的内容
                for i in range(len(colnames)):  # 一列列地读取行的内容
                    app.append(row[i])
                list.append(app)  # 装载数据
        return list

    def get_info(self):
        tables = self.excel_table_byname()
        text = []
        for rows in tables:
            for row in rows:
                if row: text.append(row)
        # print text
        infos = {}
        count = text.count('url')
        for i in range(count):
            url_index = text.index('url') + 1
            url = text.pop(url_index)
            text.remove('url')
            title_index = text.index('title') + 1
            title = text.pop(title_index)
            text.remove('title')
            keywords_index = text.index('keywords') + 1
            keywords = text.pop(keywords_index)
            text.remove('keywords')
            description_index = text.index('description') + 1
            description = text.pop(description_index)
            text.remove('description')
            infos[url] = {"title": title, "keywords": keywords, "description": description}
        return infos

    def open_website(self):
        infos = self.get_info()
        text = {}
        for url, tdk in infos.items():
            try:
                content = self.request_url(url)
            except Exception:
                continue
            if re.search(tdk['title'], content):
                text[url]['title'] = "title_success\n"
            else:
                text[url]['title'] = "title_success\n"

            if re.search(tdk['description'], content):
                text[url]['description'] = "description_success\n"
            else:
                text[url]['description'] = tdk['description']

            if re.search(tdk['keywords'], content):
                text[url]['keywords'] = "keywords_success\n"
            else:
                text[url]['keywords'] = tdk['keywords']

        return text

    def request_url(self, url):
        import requests

        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'cache-control': 'max-age=0',
        }

        res = requests.get(url, headers=headers)
        return res.text

    def check_tdk(self):
        pass


if __name__ == '__main__':
    cm = CheckMeta()
    cm.open_website()
