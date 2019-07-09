# 数据模型
class StudentManager:
    def __init__(self, name, age, score, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        self.age = value

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        self.score = value

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self.id = value


class StudentController:
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        # 返回地址列表
        return self.__stu_list

    def add_student(self, new_stu):
        new_stu.id = self.__generate_id()
        self.__stu_list.append(new_stu)

    def __generate_id(self):
        if len(self.__stu_list) > 0:
            return self.stu_list[-1].id + 1
        else:
            return 1

    def del_generate_id(self,id):
        """
        删除学生
        :param id:
        :return:
        """
        for item in self.stu_list:
            if item.id==id:
                self.stu_list.remove(item)
            return True
        return False
    def up_date_stu(self,stu_info):
        for item in self.__stu_list:
            if item.id==stu_info.id:
                item.name=stu_info.name
                item.age=stu_info.age
                item.score=stu_info.score
                return True
            return False
    def dis_order(self):
        for r in range(len(self.__stu_list)-1):
            for c in range(r+1,len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r],self.__stu_list[c]=self.__stu_list[c],self.__stu_list[r]

        return self.__stu_list
