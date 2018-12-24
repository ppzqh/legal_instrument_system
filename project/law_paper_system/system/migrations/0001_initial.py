# Generated by Django 2.0.6 on 2018-12-21 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custkey', models.IntegerField(db_column='custKey', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('acctbal', models.FloatField(blank=True, null=True)),
                ('mktsegment', models.CharField(blank=True, max_length=10, null=True)),
                ('comment', models.CharField(blank=True, max_length=117, null=True)),
            ],
            options={
                'db_table': 'Customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lineitem',
            fields=[
                ('orderkey', models.IntegerField(primary_key=True, serialize=False)),
                ('linenumber', models.IntegerField()),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('extendedprice', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('returnflag', models.CharField(blank=True, max_length=1, null=True)),
                ('linestatus', models.CharField(blank=True, max_length=1, null=True)),
                ('shipdate', models.DateField(blank=True, null=True)),
                ('commitdate', models.DateField(blank=True, null=True)),
                ('receiptdate', models.DateField(blank=True, null=True)),
                ('shipinstruct', models.CharField(blank=True, max_length=25, null=True)),
                ('shipmode', models.CharField(blank=True, max_length=10, null=True)),
                ('comment', models.CharField(blank=True, max_length=44, null=True)),
            ],
            options={
                'db_table': 'Lineitem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('nationkey', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('comment', models.CharField(blank=True, max_length=152, null=True)),
            ],
            options={
                'db_table': 'Nation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderkey', models.IntegerField(primary_key=True, serialize=False)),
                ('orderstatus', models.CharField(blank=True, max_length=1, null=True)),
                ('totalprice', models.FloatField(blank=True, null=True)),
                ('orderdate', models.DateField(blank=True, null=True)),
                ('orderpriority', models.CharField(blank=True, max_length=15, null=True)),
                ('clerk', models.CharField(blank=True, max_length=15, null=True)),
                ('shippriority', models.IntegerField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=79, null=True)),
            ],
            options={
                'db_table': 'Orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'paper',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('partkey', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=55, null=True)),
                ('mfgr', models.CharField(blank=True, max_length=25, null=True)),
                ('brand', models.CharField(blank=True, max_length=10, null=True)),
                ('parttype', models.CharField(blank=True, db_column='PartType', max_length=25, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('container', models.CharField(blank=True, max_length=10, null=True)),
                ('retailprice', models.FloatField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=23, null=True)),
            ],
            options={
                'db_table': 'Part',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('regionkey', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('comment', models.CharField(blank=True, max_length=152, null=True)),
            ],
            options={
                'db_table': 'Region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shoppingstat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custkey', models.IntegerField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('totalprice', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ShoppingStat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('suppkey', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('acctbal', models.FloatField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=101, null=True)),
            ],
            options={
                'db_table': 'Supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Partsupp',
            fields=[
                ('partkey', models.ForeignKey(db_column='partkey', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='system.Part')),
                ('availqty', models.IntegerField(blank=True, null=True)),
                ('supplycost', models.FloatField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=199, null=True)),
            ],
            options={
                'db_table': 'PartSupp',
                'managed': False,
            },
        ),
    ]