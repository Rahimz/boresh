from django.contrib import admin

from .models import Part,Panel,Band, Project



@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('length', 'width', 'quantity', 'panel', 'project')
    ordering = ('created',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'created')
    ordering = ('author',)

@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'width')
    ordering = ('name',)

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'band')
    oredering =('name',)
