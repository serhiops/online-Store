# Generated by Django 4.1.1 on 2022-09-15 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import shop.addintionaly.user_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('number_of_phone', models.CharField(blank=True, max_length=15, verbose_name='number of phone')),
                ('email_verify', models.BooleanField(default=False, verbose_name='is verify email')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', shop.addintionaly.user_manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('description', models.CharField(max_length=128, verbose_name='description')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('image', models.ImageField(upload_to='images/categories/%Y/%m/%d', verbose_name='image')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=50)),
                ('post_office', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('payment', models.CharField(choices=[('MC', 'Mastercard'), ('PP', 'Paypal'), ('COD', 'Cash on delivery'), ('CC', 'Credit card'), ('DBT', 'Direct bank transfer')], default='DBT', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_user', to=settings.AUTH_USER_MODEL, verbose_name='buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('XUA', 'ADB Unit of Account'), ('AFN', 'Afghan Afghani'), ('AFA', 'Afghan Afghani (1927–2002)'), ('ALL', 'Albanian Lek'), ('ALK', 'Albanian Lek (1946–1965)'), ('DZD', 'Algerian Dinar'), ('ADP', 'Andorran Peseta'), ('AOA', 'Angolan Kwanza'), ('AOK', 'Angolan Kwanza (1977–1991)'), ('AON', 'Angolan New Kwanza (1990–2000)'), ('AOR', 'Angolan Readjusted Kwanza (1995–1999)'), ('ARA', 'Argentine Austral'), ('ARS', 'Argentine Peso'), ('ARM', 'Argentine Peso (1881–1970)'), ('ARP', 'Argentine Peso (1983–1985)'), ('ARL', 'Argentine Peso Ley (1970–1983)'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Florin'), ('AUD', 'Australian Dollar'), ('ATS', 'Austrian Schilling'), ('AZN', 'Azerbaijani Manat'), ('AZM', 'Azerbaijani Manat (1993–2006)'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('BDT', 'Bangladeshi Taka'), ('BBD', 'Barbadian Dollar'), ('BYN', 'Belarusian Ruble'), ('BYB', 'Belarusian Ruble (1994–1999)'), ('BYR', 'Belarusian Ruble (2000–2016)'), ('BEF', 'Belgian Franc'), ('BEC', 'Belgian Franc (convertible)'), ('BEL', 'Belgian Franc (financial)'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudan Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BOB', 'Bolivian Boliviano'), ('BOL', 'Bolivian Boliviano (1863–1963)'), ('BOV', 'Bolivian Mvdol'), ('BOP', 'Bolivian Peso'), ('BAM', 'Bosnia-Herzegovina Convertible Mark'), ('BAD', 'Bosnia-Herzegovina Dinar (1992–1994)'), ('BAN', 'Bosnia-Herzegovina New Dinar (1994–1997)'), ('BWP', 'Botswanan Pula'), ('BRC', 'Brazilian Cruzado (1986–1989)'), ('BRZ', 'Brazilian Cruzeiro (1942–1967)'), ('BRE', 'Brazilian Cruzeiro (1990–1993)'), ('BRR', 'Brazilian Cruzeiro (1993–1994)'), ('BRN', 'Brazilian New Cruzado (1989–1990)'), ('BRB', 'Brazilian New Cruzeiro (1967–1986)'), ('BRL', 'Brazilian Real'), ('GBP', 'British Pound'), ('BND', 'Brunei Dollar'), ('BGL', 'Bulgarian Hard Lev'), ('BGN', 'Bulgarian Lev'), ('BGO', 'Bulgarian Lev (1879–1952)'), ('BGM', 'Bulgarian Socialist Lev'), ('BUK', 'Burmese Kyat'), ('BIF', 'Burundian Franc'), ('XPF', 'CFP Franc'), ('KHR', 'Cambodian Riel'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verdean Escudo'), ('KYD', 'Cayman Islands Dollar'), ('XAF', 'Central African CFA Franc'), ('CLE', 'Chilean Escudo'), ('CLP', 'Chilean Peso'), ('CLF', 'Chilean Unit of Account (UF)'), ('CNX', 'Chinese People’s Bank Dollar'), ('CNY', 'Chinese Yuan'), ('CNH', 'Chinese Yuan (offshore)'), ('COP', 'Colombian Peso'), ('COU', 'Colombian Real Value Unit'), ('KMF', 'Comorian Franc'), ('CDF', 'Congolese Franc'), ('CRC', 'Costa Rican Colón'), ('HRD', 'Croatian Dinar'), ('HRK', 'Croatian Kuna'), ('CUC', 'Cuban Convertible Peso'), ('CUP', 'Cuban Peso'), ('CYP', 'Cypriot Pound'), ('CZK', 'Czech Koruna'), ('CSK', 'Czechoslovak Hard Koruna'), ('DKK', 'Danish Krone'), ('DJF', 'Djiboutian Franc'), ('DOP', 'Dominican Peso'), ('NLG', 'Dutch Guilder'), ('XCD', 'East Caribbean Dollar'), ('DDM', 'East German Mark'), ('ECS', 'Ecuadorian Sucre'), ('ECV', 'Ecuadorian Unit of Constant Value'), ('EGP', 'Egyptian Pound'), ('GQE', 'Equatorial Guinean Ekwele'), ('ERN', 'Eritrean Nakfa'), ('EEK', 'Estonian Kroon'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBA', 'European Composite Unit'), ('XEU', 'European Currency Unit'), ('XBB', 'European Monetary Unit'), ('XBC', 'European Unit of Account (XBC)'), ('XBD', 'European Unit of Account (XBD)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fijian Dollar'), ('FIM', 'Finnish Markka'), ('FRF', 'French Franc'), ('XFO', 'French Gold Franc'), ('XFU', 'French UIC-Franc'), ('GMD', 'Gambian Dalasi'), ('GEK', 'Georgian Kupon Larit'), ('GEL', 'Georgian Lari'), ('DEM', 'German Mark'), ('GHS', 'Ghanaian Cedi'), ('GHC', 'Ghanaian Cedi (1979–2007)'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('GRD', 'Greek Drachma'), ('GTQ', 'Guatemalan Quetzal'), ('GWP', 'Guinea-Bissau Peso'), ('GNF', 'Guinean Franc'), ('GNS', 'Guinean Syli'), ('GYD', 'Guyanaese Dollar'), ('HTG', 'Haitian Gourde'), ('HNL', 'Honduran Lempira'), ('HKD', 'Hong Kong Dollar'), ('HUF', 'Hungarian Forint'), ('IMP', 'IMP'), ('ISK', 'Icelandic Króna'), ('ISJ', 'Icelandic Króna (1918–1981)'), ('INR', 'Indian Rupee'), ('IDR', 'Indonesian Rupiah'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IEP', 'Irish Pound'), ('ILS', 'Israeli New Shekel'), ('ILP', 'Israeli Pound'), ('ILR', 'Israeli Shekel (1980–1985)'), ('ITL', 'Italian Lira'), ('JMD', 'Jamaican Dollar'), ('JPY', 'Japanese Yen'), ('JOD', 'Jordanian Dinar'), ('KZT', 'Kazakhstani Tenge'), ('KES', 'Kenyan Shilling'), ('KWD', 'Kuwaiti Dinar'), ('KGS', 'Kyrgystani Som'), ('LAK', 'Laotian Kip'), ('LVL', 'Latvian Lats'), ('LVR', 'Latvian Ruble'), ('LBP', 'Lebanese Pound'), ('LSL', 'Lesotho Loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('LTL', 'Lithuanian Litas'), ('LTT', 'Lithuanian Talonas'), ('LUL', 'Luxembourg Financial Franc'), ('LUC', 'Luxembourgian Convertible Franc'), ('LUF', 'Luxembourgian Franc'), ('MOP', 'Macanese Pataca'), ('MKD', 'Macedonian Denar'), ('MKN', 'Macedonian Denar (1992–1993)'), ('MGA', 'Malagasy Ariary'), ('MGF', 'Malagasy Franc'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('MVR', 'Maldivian Rufiyaa'), ('MVP', 'Maldivian Rupee (1947–1981)'), ('MLF', 'Malian Franc'), ('MTL', 'Maltese Lira'), ('MTP', 'Maltese Pound'), ('MRU', 'Mauritanian Ouguiya'), ('MRO', 'Mauritanian Ouguiya (1973–2017)'), ('MUR', 'Mauritian Rupee'), ('MXV', 'Mexican Investment Unit'), ('MXN', 'Mexican Peso'), ('MXP', 'Mexican Silver Peso (1861–1992)'), ('MDC', 'Moldovan Cupon'), ('MDL', 'Moldovan Leu'), ('MCF', 'Monegasque Franc'), ('MNT', 'Mongolian Tugrik'), ('MAD', 'Moroccan Dirham'), ('MAF', 'Moroccan Franc'), ('MZE', 'Mozambican Escudo'), ('MZN', 'Mozambican Metical'), ('MZM', 'Mozambican Metical (1980–2006)'), ('MMK', 'Myanmar Kyat'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillean Guilder'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('NIO', 'Nicaraguan Córdoba'), ('NIC', 'Nicaraguan Córdoba (1988–1991)'), ('NGN', 'Nigerian Naira'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('OMR', 'Omani Rial'), ('PKR', 'Pakistani Rupee'), ('XPD', 'Palladium'), ('PAB', 'Panamanian Balboa'), ('PGK', 'Papua New Guinean Kina'), ('PYG', 'Paraguayan Guarani'), ('PEI', 'Peruvian Inti'), ('PEN', 'Peruvian Sol'), ('PES', 'Peruvian Sol (1863–1965)'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('PLN', 'Polish Zloty'), ('PLZ', 'Polish Zloty (1950–1995)'), ('PTE', 'Portuguese Escudo'), ('GWE', 'Portuguese Guinea Escudo'), ('QAR', 'Qatari Rial'), ('XRE', 'RINET Funds'), ('RHD', 'Rhodesian Dollar'), ('RON', 'Romanian Leu'), ('ROL', 'Romanian Leu (1952–2006)'), ('RUB', 'Russian Ruble'), ('RUR', 'Russian Ruble (1991–1998)'), ('RWF', 'Rwandan Franc'), ('SVC', 'Salvadoran Colón'), ('WST', 'Samoan Tala'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('CSD', 'Serbian Dinar (2002–2006)'), ('SCR', 'Seychellois Rupee'), ('SLL', 'Sierra Leonean Leone'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SKK', 'Slovak Koruna'), ('SIT', 'Slovenian Tolar'), ('SBD', 'Solomon Islands Dollar'), ('SOS', 'Somali Shilling'), ('ZAR', 'South African Rand'), ('ZAL', 'South African Rand (financial)'), ('KRH', 'South Korean Hwan (1953–1962)'), ('KRW', 'South Korean Won'), ('KRO', 'South Korean Won (1945–1953)'), ('SSP', 'South Sudanese Pound'), ('SUR', 'Soviet Rouble'), ('ESP', 'Spanish Peseta'), ('ESA', 'Spanish Peseta (A account)'), ('ESB', 'Spanish Peseta (convertible account)'), ('XDR', 'Special Drawing Rights'), ('LKR', 'Sri Lankan Rupee'), ('SHP', 'St. Helena Pound'), ('XSU', 'Sucre'), ('SDD', 'Sudanese Dinar (1992–2007)'), ('SDG', 'Sudanese Pound'), ('SDP', 'Sudanese Pound (1957–1998)'), ('SRD', 'Surinamese Dollar'), ('SRG', 'Surinamese Guilder'), ('SZL', 'Swazi Lilangeni'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('STN', 'São Tomé & Príncipe Dobra'), ('STD', 'São Tomé & Príncipe Dobra (1977–2017)'), ('TVD', 'TVD'), ('TJR', 'Tajikistani Ruble'), ('TJS', 'Tajikistani Somoni'), ('TZS', 'Tanzanian Shilling'), ('XTS', 'Testing Currency Code'), ('THB', 'Thai Baht'), ('XXX', 'The codes assigned for transactions where no currency is involved'), ('TPE', 'Timorese Escudo'), ('TOP', 'Tongan Paʻanga'), ('TTD', 'Trinidad & Tobago Dollar'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TRL', 'Turkish Lira (1922–2005)'), ('TMT', 'Turkmenistani Manat'), ('TMM', 'Turkmenistani Manat (1993–2009)'), ('USD', 'US Dollar'), ('USN', 'US Dollar (Next day)'), ('USS', 'US Dollar (Same day)'), ('UGX', 'Ugandan Shilling'), ('UGS', 'Ugandan Shilling (1966–1987)'), ('UAH', 'Ukrainian Hryvnia'), ('UAK', 'Ukrainian Karbovanets'), ('AED', 'United Arab Emirates Dirham'), ('UYW', 'Uruguayan Nominal Wage Index Unit'), ('UYU', 'Uruguayan Peso'), ('UYP', 'Uruguayan Peso (1975–1993)'), ('UYI', 'Uruguayan Peso (Indexed Units)'), ('UZS', 'Uzbekistani Som'), ('VUV', 'Vanuatu Vatu'), ('VES', 'Venezuelan Bolívar'), ('VEB', 'Venezuelan Bolívar (1871–2008)'), ('VEF', 'Venezuelan Bolívar (2008–2018)'), ('VND', 'Vietnamese Dong'), ('VNN', 'Vietnamese Dong (1978–1985)'), ('CHE', 'WIR Euro'), ('CHW', 'WIR Franc'), ('XOF', 'West African CFA Franc'), ('YDD', 'Yemeni Dinar'), ('YER', 'Yemeni Rial'), ('YUN', 'Yugoslavian Convertible Dinar (1990–1992)'), ('YUD', 'Yugoslavian Hard Dinar (1966–1990)'), ('YUM', 'Yugoslavian New Dinar (1994–2002)'), ('YUR', 'Yugoslavian Reformed Dinar (1992–1993)'), ('ZWN', 'ZWN'), ('ZRN', 'Zairean New Zaire (1993–1998)'), ('ZRZ', 'Zairean Zaire (1971–1993)'), ('ZMW', 'Zambian Kwacha'), ('ZMK', 'Zambian Kwacha (1968–2012)'), ('ZWD', 'Zimbabwean Dollar (1980–2008)'), ('ZWR', 'Zimbabwean Dollar (2008)'), ('ZWL', 'Zimbabwean Dollar (2009)')], default='UAH', editable=False, max_length=3)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='UAH', max_digits=14, verbose_name='price')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='sale')),
                ('in_stock', models.BooleanField(default=True, verbose_name='in stock')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_category', to='shop.category', verbose_name='category')),
                ('views', models.ManyToManyField(blank=True, related_name='post_views', to='shop.ip')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TempOrdering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='qty')),
                ('current_price_currency', djmoney.models.fields.CurrencyField(choices=[('XUA', 'ADB Unit of Account'), ('AFN', 'Afghan Afghani'), ('AFA', 'Afghan Afghani (1927–2002)'), ('ALL', 'Albanian Lek'), ('ALK', 'Albanian Lek (1946–1965)'), ('DZD', 'Algerian Dinar'), ('ADP', 'Andorran Peseta'), ('AOA', 'Angolan Kwanza'), ('AOK', 'Angolan Kwanza (1977–1991)'), ('AON', 'Angolan New Kwanza (1990–2000)'), ('AOR', 'Angolan Readjusted Kwanza (1995–1999)'), ('ARA', 'Argentine Austral'), ('ARS', 'Argentine Peso'), ('ARM', 'Argentine Peso (1881–1970)'), ('ARP', 'Argentine Peso (1983–1985)'), ('ARL', 'Argentine Peso Ley (1970–1983)'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Florin'), ('AUD', 'Australian Dollar'), ('ATS', 'Austrian Schilling'), ('AZN', 'Azerbaijani Manat'), ('AZM', 'Azerbaijani Manat (1993–2006)'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('BDT', 'Bangladeshi Taka'), ('BBD', 'Barbadian Dollar'), ('BYN', 'Belarusian Ruble'), ('BYB', 'Belarusian Ruble (1994–1999)'), ('BYR', 'Belarusian Ruble (2000–2016)'), ('BEF', 'Belgian Franc'), ('BEC', 'Belgian Franc (convertible)'), ('BEL', 'Belgian Franc (financial)'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudan Dollar'), ('BTN', 'Bhutanese Ngultrum'), ('BOB', 'Bolivian Boliviano'), ('BOL', 'Bolivian Boliviano (1863–1963)'), ('BOV', 'Bolivian Mvdol'), ('BOP', 'Bolivian Peso'), ('BAM', 'Bosnia-Herzegovina Convertible Mark'), ('BAD', 'Bosnia-Herzegovina Dinar (1992–1994)'), ('BAN', 'Bosnia-Herzegovina New Dinar (1994–1997)'), ('BWP', 'Botswanan Pula'), ('BRC', 'Brazilian Cruzado (1986–1989)'), ('BRZ', 'Brazilian Cruzeiro (1942–1967)'), ('BRE', 'Brazilian Cruzeiro (1990–1993)'), ('BRR', 'Brazilian Cruzeiro (1993–1994)'), ('BRN', 'Brazilian New Cruzado (1989–1990)'), ('BRB', 'Brazilian New Cruzeiro (1967–1986)'), ('BRL', 'Brazilian Real'), ('GBP', 'British Pound'), ('BND', 'Brunei Dollar'), ('BGL', 'Bulgarian Hard Lev'), ('BGN', 'Bulgarian Lev'), ('BGO', 'Bulgarian Lev (1879–1952)'), ('BGM', 'Bulgarian Socialist Lev'), ('BUK', 'Burmese Kyat'), ('BIF', 'Burundian Franc'), ('XPF', 'CFP Franc'), ('KHR', 'Cambodian Riel'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verdean Escudo'), ('KYD', 'Cayman Islands Dollar'), ('XAF', 'Central African CFA Franc'), ('CLE', 'Chilean Escudo'), ('CLP', 'Chilean Peso'), ('CLF', 'Chilean Unit of Account (UF)'), ('CNX', 'Chinese People’s Bank Dollar'), ('CNY', 'Chinese Yuan'), ('CNH', 'Chinese Yuan (offshore)'), ('COP', 'Colombian Peso'), ('COU', 'Colombian Real Value Unit'), ('KMF', 'Comorian Franc'), ('CDF', 'Congolese Franc'), ('CRC', 'Costa Rican Colón'), ('HRD', 'Croatian Dinar'), ('HRK', 'Croatian Kuna'), ('CUC', 'Cuban Convertible Peso'), ('CUP', 'Cuban Peso'), ('CYP', 'Cypriot Pound'), ('CZK', 'Czech Koruna'), ('CSK', 'Czechoslovak Hard Koruna'), ('DKK', 'Danish Krone'), ('DJF', 'Djiboutian Franc'), ('DOP', 'Dominican Peso'), ('NLG', 'Dutch Guilder'), ('XCD', 'East Caribbean Dollar'), ('DDM', 'East German Mark'), ('ECS', 'Ecuadorian Sucre'), ('ECV', 'Ecuadorian Unit of Constant Value'), ('EGP', 'Egyptian Pound'), ('GQE', 'Equatorial Guinean Ekwele'), ('ERN', 'Eritrean Nakfa'), ('EEK', 'Estonian Kroon'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBA', 'European Composite Unit'), ('XEU', 'European Currency Unit'), ('XBB', 'European Monetary Unit'), ('XBC', 'European Unit of Account (XBC)'), ('XBD', 'European Unit of Account (XBD)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fijian Dollar'), ('FIM', 'Finnish Markka'), ('FRF', 'French Franc'), ('XFO', 'French Gold Franc'), ('XFU', 'French UIC-Franc'), ('GMD', 'Gambian Dalasi'), ('GEK', 'Georgian Kupon Larit'), ('GEL', 'Georgian Lari'), ('DEM', 'German Mark'), ('GHS', 'Ghanaian Cedi'), ('GHC', 'Ghanaian Cedi (1979–2007)'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('GRD', 'Greek Drachma'), ('GTQ', 'Guatemalan Quetzal'), ('GWP', 'Guinea-Bissau Peso'), ('GNF', 'Guinean Franc'), ('GNS', 'Guinean Syli'), ('GYD', 'Guyanaese Dollar'), ('HTG', 'Haitian Gourde'), ('HNL', 'Honduran Lempira'), ('HKD', 'Hong Kong Dollar'), ('HUF', 'Hungarian Forint'), ('IMP', 'IMP'), ('ISK', 'Icelandic Króna'), ('ISJ', 'Icelandic Króna (1918–1981)'), ('INR', 'Indian Rupee'), ('IDR', 'Indonesian Rupiah'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IEP', 'Irish Pound'), ('ILS', 'Israeli New Shekel'), ('ILP', 'Israeli Pound'), ('ILR', 'Israeli Shekel (1980–1985)'), ('ITL', 'Italian Lira'), ('JMD', 'Jamaican Dollar'), ('JPY', 'Japanese Yen'), ('JOD', 'Jordanian Dinar'), ('KZT', 'Kazakhstani Tenge'), ('KES', 'Kenyan Shilling'), ('KWD', 'Kuwaiti Dinar'), ('KGS', 'Kyrgystani Som'), ('LAK', 'Laotian Kip'), ('LVL', 'Latvian Lats'), ('LVR', 'Latvian Ruble'), ('LBP', 'Lebanese Pound'), ('LSL', 'Lesotho Loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('LTL', 'Lithuanian Litas'), ('LTT', 'Lithuanian Talonas'), ('LUL', 'Luxembourg Financial Franc'), ('LUC', 'Luxembourgian Convertible Franc'), ('LUF', 'Luxembourgian Franc'), ('MOP', 'Macanese Pataca'), ('MKD', 'Macedonian Denar'), ('MKN', 'Macedonian Denar (1992–1993)'), ('MGA', 'Malagasy Ariary'), ('MGF', 'Malagasy Franc'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('MVR', 'Maldivian Rufiyaa'), ('MVP', 'Maldivian Rupee (1947–1981)'), ('MLF', 'Malian Franc'), ('MTL', 'Maltese Lira'), ('MTP', 'Maltese Pound'), ('MRU', 'Mauritanian Ouguiya'), ('MRO', 'Mauritanian Ouguiya (1973–2017)'), ('MUR', 'Mauritian Rupee'), ('MXV', 'Mexican Investment Unit'), ('MXN', 'Mexican Peso'), ('MXP', 'Mexican Silver Peso (1861–1992)'), ('MDC', 'Moldovan Cupon'), ('MDL', 'Moldovan Leu'), ('MCF', 'Monegasque Franc'), ('MNT', 'Mongolian Tugrik'), ('MAD', 'Moroccan Dirham'), ('MAF', 'Moroccan Franc'), ('MZE', 'Mozambican Escudo'), ('MZN', 'Mozambican Metical'), ('MZM', 'Mozambican Metical (1980–2006)'), ('MMK', 'Myanmar Kyat'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillean Guilder'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('NIO', 'Nicaraguan Córdoba'), ('NIC', 'Nicaraguan Córdoba (1988–1991)'), ('NGN', 'Nigerian Naira'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('OMR', 'Omani Rial'), ('PKR', 'Pakistani Rupee'), ('XPD', 'Palladium'), ('PAB', 'Panamanian Balboa'), ('PGK', 'Papua New Guinean Kina'), ('PYG', 'Paraguayan Guarani'), ('PEI', 'Peruvian Inti'), ('PEN', 'Peruvian Sol'), ('PES', 'Peruvian Sol (1863–1965)'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('PLN', 'Polish Zloty'), ('PLZ', 'Polish Zloty (1950–1995)'), ('PTE', 'Portuguese Escudo'), ('GWE', 'Portuguese Guinea Escudo'), ('QAR', 'Qatari Rial'), ('XRE', 'RINET Funds'), ('RHD', 'Rhodesian Dollar'), ('RON', 'Romanian Leu'), ('ROL', 'Romanian Leu (1952–2006)'), ('RUB', 'Russian Ruble'), ('RUR', 'Russian Ruble (1991–1998)'), ('RWF', 'Rwandan Franc'), ('SVC', 'Salvadoran Colón'), ('WST', 'Samoan Tala'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('CSD', 'Serbian Dinar (2002–2006)'), ('SCR', 'Seychellois Rupee'), ('SLL', 'Sierra Leonean Leone'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SKK', 'Slovak Koruna'), ('SIT', 'Slovenian Tolar'), ('SBD', 'Solomon Islands Dollar'), ('SOS', 'Somali Shilling'), ('ZAR', 'South African Rand'), ('ZAL', 'South African Rand (financial)'), ('KRH', 'South Korean Hwan (1953–1962)'), ('KRW', 'South Korean Won'), ('KRO', 'South Korean Won (1945–1953)'), ('SSP', 'South Sudanese Pound'), ('SUR', 'Soviet Rouble'), ('ESP', 'Spanish Peseta'), ('ESA', 'Spanish Peseta (A account)'), ('ESB', 'Spanish Peseta (convertible account)'), ('XDR', 'Special Drawing Rights'), ('LKR', 'Sri Lankan Rupee'), ('SHP', 'St. Helena Pound'), ('XSU', 'Sucre'), ('SDD', 'Sudanese Dinar (1992–2007)'), ('SDG', 'Sudanese Pound'), ('SDP', 'Sudanese Pound (1957–1998)'), ('SRD', 'Surinamese Dollar'), ('SRG', 'Surinamese Guilder'), ('SZL', 'Swazi Lilangeni'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('STN', 'São Tomé & Príncipe Dobra'), ('STD', 'São Tomé & Príncipe Dobra (1977–2017)'), ('TVD', 'TVD'), ('TJR', 'Tajikistani Ruble'), ('TJS', 'Tajikistani Somoni'), ('TZS', 'Tanzanian Shilling'), ('XTS', 'Testing Currency Code'), ('THB', 'Thai Baht'), ('XXX', 'The codes assigned for transactions where no currency is involved'), ('TPE', 'Timorese Escudo'), ('TOP', 'Tongan Paʻanga'), ('TTD', 'Trinidad & Tobago Dollar'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TRL', 'Turkish Lira (1922–2005)'), ('TMT', 'Turkmenistani Manat'), ('TMM', 'Turkmenistani Manat (1993–2009)'), ('USD', 'US Dollar'), ('USN', 'US Dollar (Next day)'), ('USS', 'US Dollar (Same day)'), ('UGX', 'Ugandan Shilling'), ('UGS', 'Ugandan Shilling (1966–1987)'), ('UAH', 'Ukrainian Hryvnia'), ('UAK', 'Ukrainian Karbovanets'), ('AED', 'United Arab Emirates Dirham'), ('UYW', 'Uruguayan Nominal Wage Index Unit'), ('UYU', 'Uruguayan Peso'), ('UYP', 'Uruguayan Peso (1975–1993)'), ('UYI', 'Uruguayan Peso (Indexed Units)'), ('UZS', 'Uzbekistani Som'), ('VUV', 'Vanuatu Vatu'), ('VES', 'Venezuelan Bolívar'), ('VEB', 'Venezuelan Bolívar (1871–2008)'), ('VEF', 'Venezuelan Bolívar (2008–2018)'), ('VND', 'Vietnamese Dong'), ('VNN', 'Vietnamese Dong (1978–1985)'), ('CHE', 'WIR Euro'), ('CHW', 'WIR Franc'), ('XOF', 'West African CFA Franc'), ('YDD', 'Yemeni Dinar'), ('YER', 'Yemeni Rial'), ('YUN', 'Yugoslavian Convertible Dinar (1990–1992)'), ('YUD', 'Yugoslavian Hard Dinar (1966–1990)'), ('YUM', 'Yugoslavian New Dinar (1994–2002)'), ('YUR', 'Yugoslavian Reformed Dinar (1992–1993)'), ('ZWN', 'ZWN'), ('ZRN', 'Zairean New Zaire (1993–1998)'), ('ZRZ', 'Zairean Zaire (1971–1993)'), ('ZMW', 'Zambian Kwacha'), ('ZMK', 'Zambian Kwacha (1968–2012)'), ('ZWD', 'Zimbabwean Dollar (1980–2008)'), ('ZWR', 'Zimbabwean Dollar (2008)'), ('ZWL', 'Zimbabwean Dollar (2009)')], default='UAH', editable=False, max_length=3)),
                ('current_price', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='UAH', max_digits=14, verbose_name='price')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('main_ordering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tempOrderingList', to='shop.ordering')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_pr', to='shop.product', verbose_name='product')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024, verbose_name='text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_author', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_prd', to='shop.product', verbose_name='product')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/products/%Y/%m/%d', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='added')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='qty')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cartListProduct', to='shop.product', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cartListUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-added',),
            },
        ),
    ]
