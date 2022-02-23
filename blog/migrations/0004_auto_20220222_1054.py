# Generated by Django 4.0.2 on 2022-02-22 10:54

from django.db import migrations

def migrate_author_to_contributors(apps, schema_editor):
    Blog = apps.get_model('blog', 'Blog')
    for blog in Blog.objects.all():
        if blog.author:
            blog.contributors.add(
                blog.author, through_defaults = {'contribution': 'Primary Author'}
            )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcontributor_blog_contributors_and_more'),
    ]

    operations = [
        migrations.RunPython(migrate_author_to_contributors)
    ]
