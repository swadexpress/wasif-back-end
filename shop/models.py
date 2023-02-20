from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from authentication.models import User
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail







class Details(models.Model):
    detail = RichTextUploadingField(blank=True, null=True)







CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True,
                            related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        # post.  use __unicode__ in place of
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])



class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class Item(models.Model):
    # title = models.CharField(max_length=100)
    # price = models.FloatField()
    # discount_price = models.FloatField(blank=True, null=True)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    # slug = models.SlugField()
    # description = models.TextField()
    # image = models.ImageField()

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    # many to one relation with Category
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    # keywords = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.CharField(max_length=240, blank=True)
    price = models.FloatField(blank=True, default=0)
    discount_price = models.FloatField(blank=True, null=True)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    amount = models.IntegerField(default=5)
    minamount = models.IntegerField(default=1)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    detail = RichTextUploadingField()
    image_detail = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    shipping_time = models.CharField(max_length=100, default='Shipping Times 5-7 days :)')
    stock_status = models.CharField(max_length=100, default='In Stock')
    cost_price = models.CharField(max_length=100, default='0')
    sell_price = models.CharField(max_length=100, default='0')


    product_status = models.CharField(max_length=100, default='This product available, Happy shopping :)')
    note = models.CharField(max_length=100, default='This product available, Happy shopping :)')
    status = models.CharField(max_length=10, choices=STATUS)
    collection_details = models.CharField(max_length=200,blank=True, null=True,default='')
    create_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.title

    ## method to create a fake table field in read only modez

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def category_name(self):
        return self.category.title
    def category_id(self):
        return self.category.id



    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(
            product=self, status='True').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(
            product=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart", kwargs={
            'slug': self.slug
        })

    # def details (self):
    #     return (self.detail | safe)


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


class ProductImages(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=240, blank=True)

class Images(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

class AllProductImages(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
from django_resized import ResizedImageField

class AllProductMainImages(models.Model):
    # image = models.ImageField(blank=True, upload_to='images/')
    image = ResizedImageField(size=[150, 150], upload_to='images/', blank=True, null=True)



    # def __str__(self):
    #     return self.product


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True,
                             null=True, default="None")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.title

    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""

    def get_total_variant_item_price(self):
        return self.quantity * self.price


class OrderItem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_variations = models.ManyToManyField(Variants)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True  )

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price
    # total_quantity = 0
    def get_total_quantity(self):
        return self.quantity 

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def price(self):
        return self.item_variations.price.all()


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    SHAPING_STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    RETURNS_STATUS = (
        ('Apply', 'Apply'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    CANCELLED_STATUS = (
        ('Apply', 'Apply'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    items = models.ManyToManyField(OrderItem)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    # payment = models.ForeignKey(
    #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    order_code = models.CharField(max_length=20, default="None")
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    shiping_status = models.CharField(
        max_length=20, choices=SHAPING_STATUS, default='New')
    returns_status = models.CharField(
        max_length=20, choices=RETURNS_STATUS, default='Apply')
    cancelled_status = models.CharField(
        max_length=20, choices=CANCELLED_STATUS, default='Apply')

    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

    def get_total_quantites(self):
        total_quantites = 0
        for order_item in self.items.all():
            total_quantites += order_item.get_total_quantity()

        return total_quantites



class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = 'Addresses'


# class Payment(models.Model):
#     stripe_charge_id = models.CharField(max_length=50)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.SET_NULL, blank=True, null=True)
#     amount = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


class OderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Return', 'Return'),
        ('Cencelled', 'Cencelled'),
        ('Delivered', 'Delivered'),
    )
    SHAPING_STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Cencelled', 'Cencelled'),
    )
    RETURNS_STATUS = (
        ('Apply', 'Apply'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Cencelled', 'Cencelled'),
    )
    CANCELLED_STATUS = (
        ('Apply', 'Apply'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Cencelled', 'Cencelled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="None")
    orderid = models.CharField(max_length=200, default="None")
    color = models.CharField(max_length=200, default="None")
    size = models.CharField(max_length=200, default="None")
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    order_code = models.CharField(max_length=20, default="None")
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    shiping_status = models.CharField(
        max_length=20, choices=SHAPING_STATUS, default='New')
    other_status = models.CharField(
        max_length=20, choices=STATUS, default='New')
    returns_status = models.CharField(
        max_length=20, choices=RETURNS_STATUS, default='Apply')
    cancelled_status = models.CharField(
        max_length=20, choices=CANCELLED_STATUS, default='Apply')
    returns_reason_sms = models.CharField(max_length=200, default='None')
    cancelled_reason_sms = models.CharField(max_length=200, default='None')

    user_returns_status = models.CharField(max_length=20, default="Apply")
    user_cancelled_status = models.CharField(max_length=20, default="Apply")

    def __str__(self):
        return self.item.title

    def imageUrl(self):
        if self.item.image is not None:
            return self.item.image
        else:
            return ""


    def email(self):
       return self.user.email
            
    def itemId(self):
       return self.item.id


class BullingAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fast_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=200)
    district = models.CharField(blank=True, max_length=200)
    division = models.CharField(blank=True, max_length=200)
    zip_code = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.email

    def email(self):
        return self.user.email

    def user_name(self):
        return self.fast_name + " " + self.last_name


class ShippingAddress(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # order = models.OneToOneField(Order, on_delete=models.CASCADE)
    shopping_fast_name = models.CharField(blank=True, max_length=50)
    shopping_last_name = models.CharField(blank=True, max_length=50)
    shopping_phone = models.CharField(blank=True, max_length=20)
    shopping_address = models.CharField(blank=True, max_length=200)
    shopping_district = models.CharField(blank=True, max_length=200)
    shopping_division = models.CharField(blank=True, max_length=200)
    shopping_zip_code = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.user.email

    def email(self):
        return self.user.email

    def user_name(self):
        return self.shopping_fast_name + " " + self.shopping_last_name


class OrderShippingAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    fast_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=11)
    address = models.CharField(blank=True, max_length=300)
    district = models.CharField(blank=True, max_length=100)
    division = models.CharField(blank=True, max_length=100)
    zip_code = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.email

    def email(self):
        return self.user.email

    def user_name(self):
        return self.fast_name + " " + self.last_name


class Payment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transactionID = models.CharField(blank=True, max_length=50)
    taka = models.CharField(blank=True, max_length=4)


    def __str__(self):
        return self.user.email

    def email(self):
        return self.user.email




class Accounts(models.Model):

    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', null=False)
    link = models.CharField(max_length=200, default="")
    appslink = models.CharField(max_length=200, default="")

    description = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name






class YourOrders(models.Model):

    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', null=False)
    link = models.CharField(max_length=200, default="")
    appslink = models.CharField(max_length=200, default="")

    description = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name




class LoginSecurity(models.Model):

    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', null=False)
    link = models.CharField(max_length=200, default="")
    appslink = models.CharField(max_length=200, default="")

    description = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name




class YourPayments(models.Model):

    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', null=False)
    link = models.CharField(max_length=200, default="")
    appslink = models.CharField(max_length=200, default="")
    phone = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name


class YourProfile(models.Model):

    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', null=False)
    link = models.CharField(max_length=200, default="")
    appslink = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=500, default="")
    def __str__(self):
        return self.name



class OrbitplugGuideline(models.Model):

    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', null=False)
    link = models.CharField(max_length=200, default="")
    appslink = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name




class YourCanTryForSell(models.Model):

    name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', null=False)
    link = models.CharField(max_length=200, default="")
    appslink = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name





