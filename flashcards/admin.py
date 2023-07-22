from django.contrib import admin
from .models import Profile, Deck, Card, StudySession, GeneratedQuestion

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_joined']

admin.site.register(Profile, ProfileAdmin)

class DeckAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at', 'updated_at']
    search_fields = ['name', 'user__username']

admin.site.register(Deck, DeckAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ['question', 'deck', 'created_at', 'updated_at']
    search_fields = ['question', 'deck__name']
    list_filter = ['deck']

admin.site.register(Card, CardAdmin)

class StudySessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'started_at', 'ended_at']
    search_fields = ['user__username']

admin.site.register(StudySession, StudySessionAdmin)

class GeneratedQuestionAdmin(admin.ModelAdmin):
    list_display = ['type', 'study_session', 'user', 'created_at']
    search_fields = ['content', 'answer', 'user__username']
    list_filter = ['type']

admin.site.register(GeneratedQuestion, GeneratedQuestionAdmin)
