"""
ALERT!
This file is used to add fake data to the database.
"""

from django.utils import timezone

from src.accounts.models import User, City, Country, Category
from src.portals.company.models import (
    Company, Job
)

from faker import Faker
fake = Faker()


def add_fake_countries():
    print()
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
        country = Country.objects.create(**country_data)
        print(f"Country: {country.name} created")

    print()
    print("__________________________________________________")
    print()


def add_fake_cities():
    print()
    print("Adding fake cities")
    cities = [
        "Riyadh", "Jeddah", "Mecca (Makkah)", "Medina (Madinah)", "Dammam",
        "Khobar (Al Khobar)", "Dhahran", "Tabuk", "Abha", "Taif", "Hail",
        "Buraidah", "Najran", "Jizan", "Khamis Mushait", "Jubail", "Yanbu",
        "Al Qassim (Buraidah)", "Al Hofuf (Al-Ahsa)", "Jazan"
    ]

    for city_name in cities:
        city = City.objects.create(name=city_name)
        print(f"City: {city.name} created")

    print()
    print("__________________________________________________")
    print()


def add_fake_categories():
    print()
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
        category = Category.objects.create(name=category_name)
        print(f"Category: {category.name} created")

    print()
    print("__________________________________________________")
    print()


def add_fake_users():
    def fake_company_accounts():
        print()
        print("Adding fake company accounts")
        for r in range(5):
            user = User(
                username=fake.company(),
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
            print(f"{r + 1}: Company User: {user.username} created")
        print()

    def fake_customer_accounts():
        print()
        print("Adding fake customer accounts")
        for _ in range(5):
            user = User(
                username=fake.name(),
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
            print(f"Customer User: {user.username} created")
        print()

    print("We are adding fake users 10 each for company and customer...")
    fake_company_accounts()
    fake_customer_accounts()
    print("__________________________________________________")
    print()


def add_fake_companies():
    print()
    print("Adding fake companies")
    company_users = User.objects.filter(is_company=True)
    for user in company_users:
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
    print()
    print("__________________________________________________")
    print()


def add_fake_jobs():
    print()
    print("Adding fake jobs")
    for _ in range(10):
        company = Company.objects.order_by('?').first()
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
    print()
    print("__________________________________________________")
    print()


def delete_all():
    print()
    print("Deleting all data")
    User.objects.filter(is_superuser=False).delete()
    Country.objects.all().delete()
    Company.objects.all().delete()
    Category.objects.all().delete()
    Job.objects.all().delete()
    print("__________________________________________________")
    print()


def main():

    print("__ WELCOME TO FAKE ME __")
    print()

    input_command = input("Do you want to delete all data? (y/n): ")
    command_delete = True if input_command == 'y' else False

    input_command = input("Do you want to add fake data? (y/n): ")
    command_add = True if input_command == 'y' else False

    if command_delete:
        delete_all()

    if command_add:
        add_fake_countries()
        add_fake_cities()
        add_fake_categories()
        add_fake_users()
        add_fake_companies()
        add_fake_jobs()


if __name__ == '__main__':
    main()
