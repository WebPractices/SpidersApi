from pymongo import MongoClient, ASCENDING
from config import *


class MongodbClient(object):

    def __init__(self, table=TABLE):
        self.table = table
        self.client = MongoClient(HOST, PORT)
        self.db = self.client[NAME]

    def change_table(self, table):
        self.table = table

    def set_num(self):
        """
        给每条数据设置唯一num
        :return: max num
        """
        nums = []
        datas = self.get_all()
        if datas:
            for data in datas:
                nums.append(data['num'])
            return max(nums)
        return 0

    def get_all(self):
        """
        获取数据库所有数据
        :return: list
        """
        if self.get_nums != 0:
            self.sort()
            datas = [i for i in self.db[self.table].find()]
            return datas
        return None

    def get_page(self, page, count):
        """
        分页数据
        :param page: 页数
        :param count: 每页条数
        :return: 每页数据
        """
        if self.get_nums != 0:
            self.sort()
            pages = self.get_nums // count + 1 if self.get_nums >= 10 else 1

            paginate = []
            for p in range(1, pages+1):
                if p > 1:
                    datas = [i for i in self.db[self.table].find().limit(count).skip((p-1)*count)]
                else:
                    datas = [i for i in self.db[self.table].find().limit(count)]
                paginate.append({'page': p, 'data': datas})
            return [j['data'] for j in paginate if j['page'] == page]
        return None

    def get_new(self):
        """
        获得最新的一条数据
        """
        data = self.get_all()[-1] if self.get_all() else None
        return data

    def get_data(self, num):
        """
        获得指定id的数据
        """
        datas = self.get_all()
        if datas:
            data = [i for i in datas if i['num']==num][0]
            return data
        return None

    def put(self, data):
        """
        添加数据
        """
        num = self.set_num() + 1
        if self.db[self.table].find_one(data):
            self.delete(data)
            data['num'] = num
            self.db[self.table].insert_one(data)
        else:
            data['num'] = num
            self.db[self.table].insert_one(data)

    def delete(self, data):
        """
        删除指定数据
        :param date: 日期
        """
        self.db[self.table].remove(data)

    def clear(self):
        """
        清空数据库
        """
        self.client.drop_database(self.table)

    def sort(self):
        """
        按num键的大小升序
        """
        self.db[self.table].find().sort('num', ASCENDING)

    @property
    def get_nums(self):
        """
        得到数据库表里数据总数
        """
        return self.db[self.table].count()

