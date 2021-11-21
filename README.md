# Tuit
- Django
- PostgreSQL
- Admin Panel

# Admin

- username: admin
- password: 1234

# PostgreSQL

- user: postgres
- password: 1234
- host: localhost

# Kanonicheskiy url 
- HTML da articlega url berish uchun ishlatamiz
- get_absolute_url(self):
  + return reverse('qaysi app: qandey nomdagi url', args=[qaysi parametrlardan foydalanamiz])

# SMTP serveri bilan ishlash

- open the file settings.py and write these:
- EMAIL_HOST = smtp.gmail.com
- EMAIL_HOST_USER = your_gmail
- EMAIL_HOST_PASSWORD = you_password
- EMAIL_PORT = 587
- EMAIL_USE_TLS = True