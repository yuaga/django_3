from django.db import models


# 所有的类必须继承自 models.Model
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女")
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    # choice用于页面上的选择框标签
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)  # auto_now_add自动保存创建时间

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']  # 按降序排列
        verbose_name = '用户'  # 人类可读性，下面的是复数
        verbose_name_plural = '用户'