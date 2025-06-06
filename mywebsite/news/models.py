from django.db import models
from django.contrib.auth.models import User
# 定義分類名稱欄位
class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

# Create your models here.
class NewsUnit(models.Model):
    # 設定新聞訊息類別
    # 外鍵關聯到Category模型，使用PROTECT保護策略防止刪除已被引用的分類，允許為空
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    # 發布新聞訊息的人
    author = models.CharField(max_length=20, null=False)
    # 新聞訊息的標題
    title = models.CharField(max_length=100, null=False)
    # 新聞訊息的內容，使用TextField，可以儲存較長的文字
    content = models.TextField(null=False)
    # 新聞訊息的發布時間
    pub_date = models.DateTimeField(auto_now_add=True)
    # 是否允許顯示
    is_show = models.BooleanField(default=False)
    # 點擊次數
    click_count = models.IntegerField(default=0)
    # 新聞訊息的圖片
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    # 新聞訊息的連結
    link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class NewsReply(models.Model):
    news = models.ForeignKey(NewsUnit, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = '新聞回覆'
        verbose_name_plural = '新聞回覆'

    def __str__(self):
        return f"[{self.news}] {self.user.username} 的回覆"
