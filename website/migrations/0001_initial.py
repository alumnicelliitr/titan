# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-03 19:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.BooleanField(default=False)),
                ('office_add', models.CharField(default=None, max_length=500, verbose_name='current office address')),
                ('residence_add', models.CharField(default=None, max_length=500, verbose_name='current residence address')),
                ('delivery_add', models.CharField(default=None, max_length=500, verbose_name='current delivery address')),
                ('address', models.CharField(default=None, max_length=500)),
                ('photo', models.ImageField(upload_to=website.models.get_file_path)),
                ('photo_sign', models.ImageField(upload_to=website.models.get_file_path)),
                ('photo_degree', models.ImageField(upload_to=website.models.get_file_path)),
                ('first_name', models.CharField(default=None, max_length=255)),
                ('middle_name', models.CharField(blank=True, default=None, max_length=255)),
                ('last_name', models.CharField(default=None, max_length=255)),
                ('dob', models.DateField(default=None)),
                ('degree_name', models.CharField(default=None, max_length=255)),
                ('degree_branch', models.CharField(default=None, max_length=255)),
                ('degree_year', models.IntegerField(choices=[(1847, 1847), (1848, 1848), (1849, 1849), (1850, 1850), (1851, 1851), (1852, 1852), (1853, 1853), (1854, 1854), (1855, 1855), (1856, 1856), (1857, 1857), (1858, 1858), (1859, 1859), (1860, 1860), (1861, 1861), (1862, 1862), (1863, 1863), (1864, 1864), (1865, 1865), (1866, 1866), (1867, 1867), (1868, 1868), (1869, 1869), (1870, 1870), (1871, 1871), (1872, 1872), (1873, 1873), (1874, 1874), (1875, 1875), (1876, 1876), (1877, 1877), (1878, 1878), (1879, 1879), (1880, 1880), (1881, 1881), (1882, 1882), (1883, 1883), (1884, 1884), (1885, 1885), (1886, 1886), (1887, 1887), (1888, 1888), (1889, 1889), (1890, 1890), (1891, 1891), (1892, 1892), (1893, 1893), (1894, 1894), (1895, 1895), (1896, 1896), (1897, 1897), (1898, 1898), (1899, 1899), (1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)], default=None)),
                ('present_desig', models.CharField(default=None, max_length=255)),
                ('present_dept', models.CharField(default=None, max_length=255)),
                ('telephone', models.CharField(blank=True, default=None, max_length=20)),
                ('mobile', models.CharField(default=None, max_length=20)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('address_for_correspondence', models.CharField(choices=[('Office Address', 'Office Address'), ('Residence Address', 'Residence Address')], default='Office Address', max_length=50)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='alumniCard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(default=None)),
                ('link', models.URLField(verbose_name='Donation Link')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=60, verbose_name='Course Name')),
                ('duration', models.CharField(max_length=50, verbose_name='Course Duration')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentBatchAlumniCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.BooleanField(default=False)),
                ('office_add', models.CharField(default=None, max_length=500, verbose_name='current office address')),
                ('residence_add', models.CharField(default=None, max_length=500, verbose_name='current residence address')),
                ('delivery_add', models.CharField(default=None, max_length=500, verbose_name='current delivery address')),
                ('address', models.CharField(default=None, max_length=500)),
                ('photo', models.ImageField(upload_to=website.models.get_file_path)),
                ('photo_sign', models.ImageField(upload_to=website.models.get_file_path)),
                ('photo_degree', models.ImageField(upload_to=website.models.get_file_path)),
                ('first_name', models.CharField(default=None, max_length=255)),
                ('middle_name', models.CharField(blank=True, default=None, max_length=255)),
                ('last_name', models.CharField(default=None, max_length=255)),
                ('dob', models.DateField(default=None)),
                ('degree_name', models.CharField(default=None, max_length=255)),
                ('degree_branch', models.CharField(default=None, max_length=255)),
                ('degree_year', models.IntegerField(default=None)),
                ('present_desig', models.CharField(default=None, max_length=255)),
                ('present_dept', models.CharField(default=None, max_length=255)),
                ('telephone', models.CharField(blank=True, default=None, max_length=20)),
                ('mobile', models.CharField(default=None, max_length=20)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('address_for_correspondence', models.CharField(choices=[('Office Address', 'Office Address'), ('Residence Address', 'Residence Address')], default='Office Address', max_length=50)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='currentAlumniCard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DonationScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(default=None)),
                ('link', models.URLField(default=None, verbose_name='External Link')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('GL', 'Guest Lecture'), ('AM', 'Alumni meet')], default=None, max_length=20)),
                ('content', models.TextField(verbose_name='Event Details')),
                ('link', models.URLField(verbose_name='External links')),
                ('venue', models.CharField(blank=True, default=None, max_length=100)),
                ('start_date', models.DateTimeField(default=None, verbose_name='Event start Date')),
                ('end_date', models.DateTimeField(default=None, verbose_name='Event end Date')),
                ('coverImage', models.ImageField(default=None, upload_to='img/events', verbose_name='Cover Image of Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default=None, upload_to=website.models.event_image_directory_path, verbose_name='Image')),
                ('description', models.CharField(blank=True, max_length=50, verbose_name='Small Description of Image')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tagLine', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField(default=None)),
                ('image', models.ImageField(default='None', upload_to='img/headlines')),
                ('link', models.URLField(blank=True, default=None)),
                ('mainPage', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200)),
                ('description', models.TextField(default=None, verbose_name='Small Description of Initiative')),
            ],
        ),
        migrations.CreateModel(
            name='KnowYourAlumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, verbose_name='Alumni Name')),
                ('year', models.PositiveIntegerField(default=None)),
                ('branch', models.CharField(choices=[('ACA', 'Advanced Chemical Analysis'), ('AGPT', 'Geophysical Technology'), ('AHEC', 'Alternate Hydro Energy Centre'), ('AHES', 'Alternate Hydro Energy Systems'), ('AR', 'Architecture and Planning'), ('ARCD', 'Architecture Department'), ('ASED', 'Applied Science and Engineering Department'), ('BE', 'M.Tech. Bioprocess Engineering'), ('BST', 'Building Technology'), ('BT', 'Biotechnology'), ('BTD', 'Biotechnology Department'), ('BTMS', 'Biotechnology'), ('CAG', 'Control & Guidance'), ('CAPPD', 'Computer Aided Process Plant Design'), ('CCR', 'CAD,CAM & Robotics'), ('CDM', 'Disaster Management and Mitigation'), ('CE', 'Civil Engineering'), ('CED', 'Civil Engineering Department'), ('CES', 'Civil Engineering with specialisation in Structures'), ('CH', 'Chemical Engineering'), ('CHCPP', 'B.Tech. (Chemical Engineering) with M.Tech. (Computer Aided Process Plant Design)'), ('CHED', 'Chemical Engineering Department'), ('CHH', 'B. Tech. (Chemical Engineering) and M. Tech. (Hydrocarbon Engineering)'), ('CHMS', 'Chemistry'), ('CNT', 'Centre of Nanotechnology'), ('CRE', 'Corrosion Engineering'), ('CSAE', 'Computer Science & Engineering'), ('CSE', 'Computer Science and Engineering'), ('CSEC', 'Communication Systems '), ('CSED', 'Computer Science and Engineering Department'), ('CSI', 'B. Tech. (Computer Science & Engineering) and M. Tech. (Information Technology)'), ('CT', 'Centre for Transportation Systems'), ('CYD', 'Chemistry Department'), ('DMM', 'Disaster Mitigation and Management'), ('DWRD', 'Water Resources Development'), ('ECCS', 'B.Tech (Electronics & Communication) & M.Tech (Communication System)'), ('ECE', 'Electronics & Communication Engineering'), ('ECED', 'Electronics and Communication Engineering'), ('ECW', 'B. Tech. (Electronics & Communication Engineering) and M. Tech. (Wireless Communication)'), ('EDPE', 'Electric Drives and Power Electronics'), ('EE', 'Electrical Engineering'), ('EED', 'Electrical Engineering Department'), ('EEG', 'Environmental Engineering'), ('EMRL', 'Environmental Management of Rivers and Lakes'), ('EPE', 'B. Tech. (Electrical Engineering) and M.Tech. (Power Electronics)'), ('EPH', 'Engineering Physics'), ('EQD', 'Earthquake Department'), ('ESD', 'Earth Sciences Department'), ('GE', 'Geomatics Engineering'), ('GPT', 'Geophysical Technology'), ('GT', 'Geological Technology'), ('GTE', 'Geotechnical Engineering'), ('GWH', 'Ground Water Hydrology'), ('HENG', 'Hydraulics Engineering'), ('HSD', 'Humanities and Social Sciences Department'), ('HSEM', 'Hydroelectric System Engineering and Management'), ('HY', 'Hydrology'), ('HYD', 'Hydrology Department'), ('IFS', 'Infrastructure Systems'), ('II', 'Institute Instrumentation'), ('IN', 'Production and Industrial Engineering'), ('INM', 'Industrial Metallurgy'), ('IPA', 'Industrial Pollution Abatement'), ('ISHM', 'Industrial Safety and Hazards Management'), ('ISP', 'Instrumentation and Signal Processing'), ('IT', 'Information Technology'), ('IWM', 'Irrigation Water Management'), ('MAD', 'Mathematics Department'), ('MAR', 'Architecture and Planning'), ('MBA', 'Management and Business Administration'), ('MCA', 'Master of Computer Application'), ('MDE', 'Machine Design Engineering'), ('ME', 'Mechanical Engineering'), ('MEC', 'M.Sc. Economics'), ('MES', 'Applied Geology'), ('MET', 'B.Tech. (Mechanical Engineering) and M.Tech. (Thermal Engineering)'), ('MEV', 'Micro Electronic and VLSI'), ('MGLT', 'Geological Technology'), ('MGPT', 'Geophysical Technology'), ('MHY', 'Hydrology'), ('MIED', 'Mechanical and Industrial Engineering'), ('MMED', 'Metallurgical and Materials Engineering'), ('MMT', 'Metallurgy Dual'), ('MSAM', 'Applied Mathematics'), ('MSC', 'Chemistry'), ('MSCM', 'M.Sc. Mathematics'), ('MSCPH', 'Physics'), ('MSD', 'Management Studies'), ('MSIM', 'M.sc Industrial Mathematics and Informatics'), ('MSM', 'Applied Mathematics'), ('MSP', 'Physics'), ('MT', 'Metallurgical & Materials Engineering'), ('MURP', 'Master of Urban and Rural Planning'), ('NT', 'Nanotechnology'), ('PEM', 'B. Tech. (Process Engineering) and M.B.A.'), ('PHD', 'Physics'), ('PHM', 'Materials Engineering'), ('PHPD', 'Photonics'), ('PISE', 'Production & Industrial Systems Engineering'), ('PKG', 'Packaging Technology'), ('PP', 'Pulp & Paper Technology'), ('PPE', 'Pulp & Paper Engineering'), ('PPED', 'Polymer and Process Engineering Department'), ('PS', 'Polymer Science and Technology'), ('PSE', 'Power System Engineering'), ('PST', 'Polymer Science and Technology'), ('PTD', 'Paper Technology Department'), ('RFM', 'RF and Microwave Engineering'), ('SAC', 'System and Control'), ('SD', 'Soil Dynamics'), ('SDV', 'Semiconductor Design and VLSI Technology'), ('SE', 'Structural Engineering'), ('SMC', 'System Modelling and Control'), ('SSEM', 'Solid State Electronic Materials'), ('STD', 'Structural Dynamics'), ('SVRA', 'Seismic Vulnerability & Risk Assessment'), ('SWH', 'Surface Water Hydrology'), ('TE', 'Transportation Engineering'), ('TEMI', 'Thermal Engineering'), ('TPH', 'Civil Engineering with specialisation in Structures'), ('TSE', 'Thermal Systems Engineering'), ('WEMI', 'Welding Engineering'), ('WM', 'Watershed Management'), ('WRD', 'Water Resources Development'), ('WRDMD', 'Water Resources Development and Management')], max_length=10, verbose_name='Branch')),
                ('link', models.URLField(blank=True, default=None, null=True, verbose_name='External Link')),
                ('description', models.TextField(default=None)),
                ('thumbnail', models.ImageField(default=None, upload_to='img/KnowYourAlum', verbose_name='Thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('contact_no', models.CharField(max_length=15)),
                ('batch_of', models.PositiveIntegerField(default=None)),
                ('branch', models.CharField(default=None, max_length=40)),
                ('role', models.CharField(max_length=20)),
                ('link', models.URLField(verbose_name='Link to Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Mou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='University Name')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('letter', models.FileField(default=None, upload_to='mou/')),
                ('link', models.URLField(verbose_name='University Website Link')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, verbose_name='News Title')),
                ('description', models.TextField(default=None)),
                ('url', models.URLField(blank=True, default=None, null=True, verbose_name='News Link')),
                ('thumbnail', models.ImageField(default=None, upload_to='img/news', verbose_name='Image')),
                ('pub_date', models.DateTimeField(default=None, verbose_name='Published on')),
                ('expiry', models.DateTimeField(default=None, verbose_name='Expiry date')),
                ('short_desc', models.CharField(blank=True, default=None, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='NewsLetter Title')),
                ('content', models.TextField(verbose_name='NewsLetter Content')),
                ('external_link', models.URLField()),
                ('pub_date', models.DateTimeField(verbose_name='Published on')),
                ('image', models.ImageField(default=None, upload_to='img/newsletter/', verbose_name='NewsLetter Image')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('visibility', models.BooleanField(default=True)),
                ('external_url', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.IntegerField(default=0)),
                ('content', models.TextField(default='')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Parent', to='website.Node')),
            ],
        ),
        migrations.CreateModel(
            name='ShareYourStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Story Title')),
                ('description', models.TextField(default=None)),
                ('link', models.URLField(blank=True, default=None, null=True, verbose_name='Article Link')),
                ('thumbnail', models.ImageField(default=None, upload_to='img/ShareYourStory', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Team name')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Video Title')),
                ('mainPage', models.BooleanField(default=False)),
                ('link', models.URLField(default=None)),
                ('description', models.CharField(blank=True, max_length=50, verbose_name='Video Description')),
            ],
        ),
        migrations.CreateModel(
            name='VideoRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title of the Video repository')),
                ('link', models.URLField(blank=True, default=None, verbose_name='Youtube playlist link')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='VideoRepository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='website.VideoRepository'),
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='website.Team'),
        ),
        migrations.AddField(
            model_name='course',
            name='mou',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='website.Mou'),
        ),
    ]
