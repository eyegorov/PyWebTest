from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'important_status', 'public_status', 'note_status', 'create_at', 'update_at')

    readonly_fields = ('create_at',)
