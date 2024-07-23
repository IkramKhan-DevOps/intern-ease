from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from src.accounts.models import User, City, Country, Category
from src.portals.company.models import Company, Job

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake data for testing purposes"

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete all existing data before adding new fake data',
        )

    def handle(self, *args, **options):
        if options['delete']:
            self.delete_all()

        self.add_fake_countries()
        self.add_fake_cities()
        self.add_fake_categories()
        self.add_fake_users()
        self.add_fake_companies()
        self.add_fake_jobs()

    def delete_all(self):
        print("Deleting all data")
        User.objects.filter(is_superuser=False).delete()
        Country.objects.all().delete()
        City.objects.all().delete()
        Company.objects.all().delete()
        Category.objects.all().delete()
        Job.objects.all().delete()
        print("__________________________________________________")

    def add_fake_countries(self):
        print("Adding fake countries")
        countries = [
            {
                "name": "Saudi Arabia",
                "short_name": "SA",
                "phone_code": "+966",
                "language": "Arabic",
                "currency": "SAR",
            }
        ]
        for country_data in countries:
            if not Country.objects.filter(name=country_data['name']).exists():
                Country.objects.create(**country_data)
                print(f"Country: {country_data['name']} created")
            else:
                print(f"Country: {country_data['name']} already exists")
        print("__________________________________________________")

    def add_fake_cities(self):
        print("Adding fake cities")
        cities = [
            "Riyadh", "Jeddah", "Mecca (Makkah)", "Medina (Madinah)", "Dammam",
            "Khobar (Al Khobar)", "Dhahran", "Tabuk", "Abha", "Taif", "Hail",
            "Buraidah", "Najran", "Jizan", "Khamis Mushait", "Jubail", "Yanbu",
            "Al Qassim (Buraidah)", "Al Hofuf (Al-Ahsa)", "Jazan"
        ]
        for city_name in cities:
            if not City.objects.filter(name=city_name).exists():
                City.objects.create(name=city_name)
                print(f"City: {city_name} created")
            else:
                print(f"City: {city_name} already exists")
        print("__________________________________________________")

    def add_fake_categories(self):
        print("Adding fake categories")
        categories = [
            "Software Development",
            "System Administration",
            "Cybersecurity",
            "Data Science and Analytics",
            "IT Support",
            "Quality Assurance (QA) and Testing",
            "Project Management",
            "Database Management",
            "Artificial Intelligence (AI) and Machine Learning (ML)",
            "Cloud Computing",
            "UI/UX Design",
            "Business Analysis",
            "Network Engineering",
            "Technical Writing",
            "Game Development",
            "Computer Hardware",
            "Mobile Development",
            "Embedded Systems",
            "IT Sales and Marketing",
        ]
        for category_name in categories:
            if not Category.objects.filter(name=category_name).exists():
                Category.objects.create(name=category_name)
                print(f"Category: {category_name} created")
            else:
                print(f"Category: {category_name} already exists")
        print("__________________________________________________")

    def add_fake_users(self):
        def fake_company_accounts():
            print("Adding fake company accounts")
            for _ in range(5):
                username = fake.company()
                if not User.objects.filter(username=username).exists():
                    user = User(
                        username=username,
                        email=fake.company_email(),
                        password=fake.password(),
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        is_company=True,
                        phone_number=fake.phone_number(),
                        address=fake.address(),
                        gender=fake.random_element(elements=('m', 'f')),
                        is_completed=True,
                    )
                    user.save()
                    print(f"Company User: {username} created")
                else:
                    print(f"Company User: {username} already exists")

        def fake_customer_accounts():
            print("Adding fake customer accounts")
            for _ in range(5):
                username = fake.name()
                if not User.objects.filter(username=username).exists():
                    user = User(
                        username=username,
                        email=fake.email(),
                        password=fake.password(),
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        is_customer=True,
                        phone_number=fake.phone_number(),
                        address=fake.address(),
                        gender=fake.random_element(elements=('m', 'f')),
                        is_completed=True,
                    )
                    user.save()
                    print(f"Customer User: {username} created")
                else:
                    print(f"Customer User: {username} already exists")

        print("Adding fake users")
        fake_company_accounts()
        fake_customer_accounts()
        print("__________________________________________________")

    def add_fake_companies(self):
        print("Adding fake companies")
        company_users = User.objects.filter(is_company=True)
        for user in company_users:
            if not Company.objects.filter(user=user).exists():
                company = Company(
                    user=user,
                    name=fake.company(),
                    tag_line=fake.catch_phrase(),
                    description=fake.paragraph(nb_sentences=10),
                    business_type=fake.random_element(
                        elements=('non profit', 'government', 'small business', 'medium business', 'enterprise')
                    ),
                    company_registration_no=fake.ean(length=13),
                    company_start_date=timezone.make_aware(fake.date_time_this_decade()),
                    contact_number=fake.phone_number(),
                    contact_email=fake.company_email(),
                    company_address=fake.address(),
                    country=Country.objects.order_by('?').first(),
                )
                company.save()
                print(f"Company: {company.name} created for user: {user.username}")
            else:
                print(f"Company for user: {user.username} already exists")
        print("__________________________________________________")

    def add_fake_jobs(self):
        print("Adding fake jobs")
        for _ in range(10):
            company = Company.objects.order_by('?').first()
            if company:
                if not Job.objects.filter(company=company, title=fake.job()).exists():
                    job = Job(
                        title=fake.job(),
                        category=Category.objects.order_by('?').first(),
                        vacancy=fake.random_digit_not_null(),
                        description=fake.paragraph(nb_sentences=10),
                        detailed_description=fake.paragraph(nb_sentences=10),
                        company=company,
                        city=City.objects.order_by('?').first(),
                        country=Country.objects.order_by('?').first(),
                        start_time=timezone.make_aware(fake.date_time_this_decade()),
                        end_time=timezone.make_aware(fake.date_time_this_decade()),
                    )
                    job.save()
                    print(f"Job: {job.title} created")
                else:
                    print(f"Job: {fake.job()} for company: {company.name} already exists")
        print("__________________________________________________")
