from django.contrib import admin
from .models import Quiz, Question, Choice, Submission

# Choice modelini inline shaklida ro'yxatga olish
class ChoiceInline(admin.TabularInline):  # Yoki admin.StackedInline
    model = Choice
    extra = 1  # Bir nechta qo'shishni taklif qiladi (1 ta bo'lishi kerak)
    fields = ('choice_text', 'is_correct')  # Qaysi maydonlarni ko'rsatish

# Question Modelini ro'yxatga olish
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'difficulty_level')
    search_fields = ('question_text', 'difficulty_level')
    list_filter = ('difficulty_level',)
    inlines = [ChoiceInline]  # Inline qo'shilgan Choice modelini qo'shish

admin.site.register(Question, QuestionAdmin)

# Boshqa modellarga oid admin sozlamalari
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description')
    search_fields = ('title', 'description')

admin.site.register(Quiz, QuizAdmin)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice', 'submitted_at')
    search_fields = ('user__username', 'question__question_text')
    list_filter = ('submitted_at',)

admin.site.register(Submission, SubmissionAdmin)
