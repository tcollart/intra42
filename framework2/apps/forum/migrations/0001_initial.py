# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BasePost',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('message', models.TextField(default='Your message', max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('basepost_ptr', models.OneToOneField(to='forum.BasePost', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
            ],
            options={
            },
            bases=('forum.basepost',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basecategory_ptr', models.OneToOneField(to='forum.BaseCategory', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
            ],
            options={
            },
            bases=('forum.basecategory',),
        ),
        migrations.CreateModel(
            name='ChildCategory',
            fields=[
                ('basecategory_ptr', models.OneToOneField(to='forum.BaseCategory', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('father', models.ForeignKey(to='forum.Category', related_name='FatherCategory')),
            ],
            options={
            },
            bases=('forum.basecategory',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('message', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='CommentAuthor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('basepost_ptr', models.OneToOneField(to='forum.BasePost', auto_created=True, serialize=False, primary_key=True, parent_link=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(to='forum.BaseCategory', related_name='OriginalCategory')),
            ],
            options={
            },
            bases=('forum.basepost',),
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(to='forum.BasePost', related_name='CommentThread'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basepost',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='ThreadUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='originalthread',
            field=models.ForeignKey(to='forum.Thread', related_name='AnswerThread'),
            preserve_default=True,
        ),
    ]
