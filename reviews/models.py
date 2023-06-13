from django.db import models
from users.models import User

class Review(models.Model):
    RATE_CHOICES = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )
    
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE, related_name="reviews")
    area_code = models.PositiveSmallIntegerField("지역 코드")
    sigungu_code = models.PositiveSmallIntegerField("시군구 코드")
    content_type_id = models.PositiveSmallIntegerField("관광지 유형 코드")
    content_id = models.PositiveBigIntegerField("관광지 코드")
    rate = models.PositiveSmallIntegerField("평점", choices=RATE_CHOICES, default=1)
    title = models.CharField("제목", max_length=150)
    content = models.TextField("리뷰")
    visited_date = models.DateField("방문일")
    created_at = models.DateTimeField("작성시각", auto_now_add=True)
    updated_at = models.DateTimeField("수정시각", auto_now=True)
    image = models.ImageField("대표 이미지", upload_to="review/images/%Y/%m/", blank=True)
    likes = models.ManyToManyField(User, verbose_name="좋아요", blank=True, related_name='like_reviews')
    
    
    def __str__(self):
        return self.title