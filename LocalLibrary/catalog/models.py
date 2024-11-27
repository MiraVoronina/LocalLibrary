
from django.db import models

from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book") #может иметь несколько жанров, а жанр может иметь много книг

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)


from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date


class MyModelName(models.Model):
    """Типичный класс модели, производный от класса Model."""

    # Поля
    my_field_name = models.CharField(max_length=20, help_text='Введите описание поля')

    # Метаданные
    class Meta:
        ordering = ['-my_field_name']

    # Методы
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к определенному экземпляру MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """Строка для представления объекта MyModelName."""
        return self.my_field_name


# Создание новой записи с использованием конструктора модели.
a_record = MyModelName(my_field_name="Instance #1")

# Сохранение объекта в базе данных.
a_record.save()


# Доступ к значениям полей модели
print(a_record.id)  # Должен вернуть 1 для первой записи.
print(a_record.my_field_name)

# Изменение записи
# Доступ к значениям полей модели с использованием атрибутов Python.
print(a_record.id)  # Должен вернуть 1 для первой записи.
print(a_record.my_field_name)  # Должен напечатать 'Instance #1'

# Изменение записи, изменяя поля, затем вызывая save().
a_record.my_field_name = "New Instance Name"
a_record.save()


class Genre(models.Model):
    """Модель, представляющая жанр книги."""
    name = models.CharField(max_length=200, help_text="Введите жанр книги (например, Научная фантастика, Французская поэзия и т.д.)")
    name = models.CharField(max_length=200,


    def __str__(self):
        """Строка для представления объекта модели."""
        return self.name


class Book(models.Model):
    """Модель, представляющая книгу (но не конкретный экземпляр книги)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 символов <a href="https://www.isbn-international.org/content/what-isbn">номер ISBN</a>')
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр для этой книги")
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги")
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 символов <a href="https://www.isbn-international.org/content/what-isbn">номер ISBN</a>'
    )
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр для этой книги")
    copies = models.PositiveIntegerField(default=1)  # Количество экземпляров
    is_borrowed = models.BooleanField(default=False)  # Статус выдачи книги
    language = models.CharField(max_length=30, default='English')
    publication_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_mark_returned", "Can mark book as returned"),
            ("can_view_borrowed_books", "Can view borrowed books"),
        ]

    def __str__(self):
        """Строка для представления объекта модели."""
        return self.title
    def get_absolute_url(self):
        """Возвращает URL для доступа к конкретному экземпляру книги."""
        return reverse('book_detail', args=[str(self.id)])


class BookInstance(models.Model):
    """Модель, представляющая конкретный экземпляр книги (т.е. который можно взять в библиотеке)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный ID для этой книги во всей библиотеке")

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        """Проверяет, просрочена ли книга."""
        return self.due_back and date.today() > self.due_back


    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('b', 'Borrowed'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Доступность книги')


    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):

        return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

        """Строка для представления объекта модели."""
        return '%s (%s)' % (self.id, self.book.title)


class Author(models.Model):
    """Модель, представляющая автора."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Умер', null=True, blank=True)
    date_of_death = models.DateField('death', null=True, blank=True)


    def get_absolute_url(self):
        """Возвращает URL для доступа к конкретному экземпляру автора."""
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        """Строка для представления объекта модели."""
        return '%s, %s' % (self.last_name, self.first_name)

