from faker import Faker

fake = Faker('en_US')

fake_word = fake.word()
print(fake_word)

fake_words = fake.words(3)
print(fake_words)

fake_paragraph = fake.paragraph(10)
print(fake_paragraph)

fake_phone_number = fake.phone_number()
print(fake_phone_number)

fake_email = fake.email()
print(fake_email)

content = ""

for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.address()
    content += fake.phone_number()
    content += fake.word()

with open('contacts.txt', 'w+') as file:
    file.write(content)

import shutil

shutil.copy('contacts.txt', 'contacts.txt.bak')