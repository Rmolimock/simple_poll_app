from django.contrib import admin
from .models import Question, Choice


admin.site.site_header = "Poll App Admin Panel"
admin.site.site_title = "Poll App"
admin.site.index_title = "Admin"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'],
                  'classes': ['collapse']})]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question)
#admin.site.register(Choice)
