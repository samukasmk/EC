from django.contrib import admin
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

from .forms import CreateUserFormAdmin, UpdateUserFormAdmin
from .models import (User, Calendar, Menssage, ClassRoom, Teacher, Student,
                     Youtube, PdfFile, Class)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'cod', 'first_name', 'last_name',
        'email', 'type_of_course'
    )
    date_hierarchy = 'date_joined'
    search_fields = (
        'first_name', 'last_name', 'email', 'cod',
        'date_joined', 'type_of_course'
    )
    list_filter = ('type_of_course', 'date_joined',)
    add_form = CreateUserFormAdmin
    form = UpdateUserFormAdmin

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


class CalendarAdmin(admin.ModelAdmin):
    pass


class MenssageAdmin(admin.ModelAdmin):
    pass


class YoutubeAdmin(admin.ModelAdmin):
    pass


class PdfFileAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


class ClassRoomAdmin(admin.ModelAdmin):
    pass


class ClassAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(ClassAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['attendances'].widget = CheckboxSelectMultiple()
        return form


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Menssage, MenssageAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Youtube, YoutubeAdmin)
admin.site.register(PdfFile, PdfFileAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
