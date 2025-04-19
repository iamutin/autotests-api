from faker import Faker


def get_random_email():
    fake = Faker()
    return fake.email()
