    from django.db import models


class Categories(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    icon = models.CharField(verbose_name='Код иконки', max_length=200)
    slug_category = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Materials(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Colors(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    color = models.CharField(verbose_name='Код цвета (например #FFFFFF)', max_length=7)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Sizes(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Products(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    slug_product = models.SlugField(verbose_name='URL', unique=True)
    category = models.ForeignKey(Categories, verbose_name='Категория', related_name='category',
                                 on_delete=models.PROTECT)
    price = models.DecimalField(verbose_name='Основная цена', max_digits=10, decimal_places=2)
    price_discount = models.DecimalField(verbose_name='Цена со скидкой', max_digits=10, decimal_places=2, null=True,
                                         blank=True)
    discount = models.DecimalField(verbose_name='Скидка', max_digits=2, decimal_places=0, null=True, blank=True)
    img1 = models.ImageField(verbose_name='Основное изображение (640х480)', upload_to='static/images/products/', null=True,
                             blank=True)
    img2 = models.ImageField(verbose_name='Второе изображение (640х480)', upload_to='static/images/products/', null=True,
                             blank=True)
    img3 = models.ImageField(verbose_name='Третье изображение (640х480)', upload_to='static/images/products/', null=True,
                             blank=True)
    img4 = models.ImageField(verbose_name='Четвертое изображение (640х480)', upload_to='static/images/products/', null=True,
                             blank=True)
    img5 = models.ImageField(verbose_name='Пятое изображение (640х480)', upload_to='static/images/products/', null=True,
                             blank=True)
    brand = models.CharField(verbose_name='Бренд', max_length=200)
    materials = models.ManyToManyField(Materials, verbose_name='Материалы', related_name='materials')
    colors = models.ManyToManyField(Colors, verbose_name='Цвета', related_name='colors')
    sizes = models.ManyToManyField(Sizes, verbose_name='Размеры', related_name='sizes')
    availability = models.BooleanField(verbose_name='Наличие')
    new = models.BooleanField(verbose_name='Новинка')
    date = models.DateTimeField(auto_now_add=True)
    popularity = models.BooleanField(verbose_name='Популярный товар', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Portfolio(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    url = models.CharField(verbose_name='Ссылка', max_length=200)
    img = models.ImageField(verbose_name='Изображение для портфолио', upload_to='static/images/portfolio/', null=True,
                             blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class Subscribe(models.Model):
    mail = models.CharField(verbose_name='Почта', max_length=200)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Заявка на подписку'
        verbose_name_plural = 'Заявки на подписку'


class Team(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    img = models.ImageField(verbose_name='Фото участника команды', upload_to='static/images/team/', null=True,)
    status = models.CharField(verbose_name='Статус', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', max_length=200, blank=True)
    instagram = models.CharField(verbose_name='Ссылки на instagram', max_length=200, blank=True)
    mail = models.CharField(verbose_name='Почта участника', max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'


class Review(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    img = models.ImageField(verbose_name='Фото человека с отзыва', upload_to='static/images/team/')
    description = models.TextField(verbose_name='Отзыв', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
