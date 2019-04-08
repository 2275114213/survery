# Generated by Django 2.1.2 on 2019-01-22 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=64, verbose_name='课程名称')),
                ('semester', models.IntegerField(verbose_name='学期')),
                ('memo', models.CharField(blank=True, max_length=100, null=True, verbose_name='说明')),
            ],
            options={
                'verbose_name': '班级列表',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='调查问卷名称')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='第几次问卷调查')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='问卷创建日期')),
                ('quantity', models.PositiveIntegerField(default=1, help_text='生成唯一码的数量', verbose_name='数量')),
                ('by_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ClassList', verbose_name='问卷调查班级')),
            ],
            options={
                'verbose_name': '调查问卷',
                'verbose_name_plural': '调查问卷',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='SurveyChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='答案内容')),
                ('points', models.IntegerField(verbose_name='分值')),
            ],
            options={
                'verbose_name': '问卷调查候选答案',
                'verbose_name_plural': '问卷调查候选答案',
            },
        ),
        migrations.CreateModel(
            name='SurveyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(max_length=32, unique=True)),
                ('used', models.BooleanField(default=False, verbose_name='使用状态')),
                ('used_time', models.DateTimeField(blank=True, null=True, verbose_name='使用时间')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='调查问题')),
                ('date', models.DateField(auto_now_add=True)),
                ('answer_type', models.CharField(choices=[('single', '单选'), ('suggestion', '建议')], default='score', max_length=32, verbose_name='问题类型')),
            ],
            options={
                'verbose_name': '调查问卷问题列表',
                'verbose_name_plural': '调查问卷问题列表',
            },
        ),
        migrations.CreateModel(
            name='SurveyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, help_text='打分为0至10,0为非常不满意,10为非常满意,请自行斟酌', null=True, verbose_name='评分')),
                ('suggestion', models.TextField(blank=True, max_length=1024, null=True, verbose_name='建议')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='答题日期')),
                ('single', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.SurveyChoices', verbose_name='单选')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Survey', verbose_name='问卷')),
                ('survey_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.SurveyCode', verbose_name='唯一码')),
                ('survey_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SurveyItem', verbose_name='调查项')),
            ],
            options={
                'verbose_name': '问卷记录',
                'verbose_name_plural': '问卷记录',
            },
        ),
        migrations.AddField(
            model_name='surveychoices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='web.SurveyItem', verbose_name='问题'),
        ),
        migrations.AddField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(to='web.SurveyItem', verbose_name='选择要调查的问题列表'),
        ),
    ]