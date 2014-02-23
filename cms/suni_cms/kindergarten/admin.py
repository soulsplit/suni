from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from kindergarten.models import Parent, Group, Kid

# Admin and Inline Classes
class KidAdmin(admin.ModelAdmin):
    '''Admin model for Kid model'''
    list_display = (
        'first_name',
        'middle_name',
        'last_name',
        'date_of_birth',
        'date_of_leave',
        'gender',
        'mother',
        'father',
        'group',
        'waitlisted',
    )

    search_fields = (
        'first_name',
        'middle_name',
        'last_name',
    )

    list_filter = (
        'group__name',
        'gender',
        'waitlisted',
    )

    readonly_fields = ('age',)

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 1, 'cols': 40})
        },
    }


class KidInline(admin.TabularInline):
    '''Inline table for Kid model'''
    model = Kid
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 1, 'cols': 40})
        },
    }
    datefield_overrides = {
        models.DateField: {
            'widget': TextInput(attrs={'rows': 2, 'cols': 400})
        },
    }

class GroupAdmin(admin.ModelAdmin):
    '''Admin model for Group model'''
    list_display = (
        'name',
        'max_amount_of_kids',
        'min_age',
        'max_age',
        'free_spots',
    )

    search_fields = (
        'name',
    )

    readonly_fields = ('amount_of_kids',)

    inlines = [
        KidInline,
    ]

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 1, 'cols': 40})
        },
    }
    datefield_overrides = {
        models.DateField: {
            'widget': TextInput(attrs={'rows': 2, 'cols': 400})
        },
    }

class GroupInline(admin.TabularInline):
    '''Inline table for Group model'''
    model = Group
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 1, 'cols': 40})
        },
    }
    datefield_overrides = {
        models.DateField: {
            'widget': TextInput(attrs={'rows': 2, 'cols': 400})
        },
    }

class ParentAdmin(admin.ModelAdmin):
    '''Admin model for Parent model'''
    list_display = (
        'first_name',
        'middle_name',
        'last_name',
        'gender',
    )

    search_fields = (
        'first_name',
        'middle_name',
        'last_name',
    )

    inlines = [
#        KidInline,
    ]

    list_filter = (
        'gender',
    )

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 1, 'cols': 40})
        },
    }

class ParentInline(admin.TabularInline):
    '''Inline table for Parent model'''
    model = Parent
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 1, 'cols': 40})
        },
    }
    datefield_overrides = {
        models.DateField: {
            'widget': TextInput(attrs={'rows': 2, 'cols': 400})
        },
    }

admin.site.register(Parent, ParentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Kid, KidAdmin)
