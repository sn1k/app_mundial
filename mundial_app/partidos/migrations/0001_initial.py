# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('local', models.ForeignKey(to='equipos.Equipo', to_field='id')),
                ('visitante', models.ForeignKey(to='equipos.Equipo', to_field='id')),
                ('fecha', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
