"""
定义...文件
数据模型类：StudentModel
		数据：编号 id,姓名 name,年龄 age,成绩 score
	逻辑控制类：StudentManagerController
		数据：学生列表 __stu_list
		行为：获取列表 stu_list,添加学生 add_student
"""


# 数据模型类
class StudentModel:
    def __init__(self, name, age, score, id=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value


# 逻辑控制类
class StudentManagerController:
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        # 返回列表地址,外部还能修改
        return self.__stu_list

    def add_student(self, new_stu):
        new_stu.id = self.__generate_id()
        self.__stu_list.append(new_stu)

    def __generate_id(self):
        if len(self.__stu_list) > 0:
            return self.__stu_list[-1].id + 1
        else:
            return 1

    # 删除学生remove_student
    def del_generate_id(self, id):
        """
        根据编号删除学生
        :param id: 学生id
        :return: 是否删除成功
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
            return False

    # 3.修改学生update_student:根据编号修改其余信息
    def update_student(self, stu_info):
        """
        根据编号,修改其余信息
        :param stu_info: 学生信息
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    # 5.根据成绩降序排列
    def output_student_by_score(self):
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], \
                                                             self.__stu_list[r]

        # return self.__stu_list
        stu_model = StudentManagerView()
        stu_model.out_input(self.__stu_list[:])


# 测试
# controller = StudentManagerController()
# controller.add_student(StudentModel("无极", 25, 100))
# controller.add_student(StudentModel("赵敏", 25, 100))
# controller.add_student(StudentModel("赵敏", 25, 100))
# #从语法上看,没有修改属性,而是修改学生列表的第一个元素
# controller.stu_list[0]=StudentModel()
# for item in controller.stu_list:
#   print(item.id)
# *****************删除学生*********************************
# re=controller.del_generate_id(1)
# print(re)

# ********************修改信息***********************
# stu = StudentModel("芷若", 250, 100, 2)
# controller.update_student(stu)
# for item in controller.stu_list:
#     print(item.name)
"""
显示菜单__display_menu，选择菜单项__select_menu_item
，入口逻辑main，
"""


class StudentManagerView:
    """
      学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        """
        显示菜单
        """
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩升序显示")

    def __select_menu_item(self):
        """
          选择菜单项
        """
        number = input("请输入选项:")
        if number == "1":
            self.__input_student()
        elif number == "2":
            self.out_input(self.__manager.stu_list)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            self.__manager.output_student_by_score()

    def main(self):
        """
          入口逻辑
        """
        while True:
            self.__display_menu()
            self.__select_menu_item()




    # 将int（input（...））封装
    def __input_student(self):
        """
            输入学生
        """

        name = input("请输入姓名:")
        age = int(input("请输入年龄:"))
        score = int(input("请输入分数:"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)



    def out_input(self, list__stu):
        """
        显示学生
        """
        for item in list__stu:
            print("%d-%s-%d-%d" % (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        """
        删除学生
        """
        id = int(input("请输入您要删除的id:"))
        if self.__manager.stu_list.remove(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        id = int(input("请输入您要修改的id:"))
        name = input("请输入您要修改的姓名:")
        age = int(input("请输入您要修改的年龄:"))
        score = int(input("请输入您要修改的分数:"))
        info = StudentModel(name, age, score, id)
        if self.__manager.update_student(info):
            print("修改成功")

        else:
            print("修改失败")


view = StudentManagerView()
view.main()
