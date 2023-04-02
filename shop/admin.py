from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *
import admin_thumbnails
from .models import Images

def order_name(obj):
    return '%s %s' % (obj.first_name, obj.last_name)
order_name.short_description = 'Name'


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf', args=[obj.id])))


order_name.short_description = 'PDF'



class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Item,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Item,
                                                'category',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'image_thumbnail']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['category']
    # readonly_fields = ('image_tag',)
    
    inlines = [ProductImageInline, ProductVariantsInline]
    prepopulated_fields = {'slug': ('title',)}


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'color_tag']


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']



@admin_thumbnails.thumbnail('image')
class productImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


class VariantsAdmin(admin.ModelAdmin):


    list_display = ['title', 'item', 'color',
                'size', 'price', 'quantity', 'image_tag']
    search_fields = ['title']
    # inlines = [ItemVariationInLineAdmin]


class OrderProductline(admin.TabularInline):
    model = OderProduct

    fields = (
        # 'user',
        'item',
        # 'price',
        'quantity',
        'status',
        # 'amount',
        'color',
        "size",
        # 'name',
        # 'order_code',
        # 'order',
        'cancelled_reason_sms',
        'returns_reason_sms',
        "other_status"

    )

    readonly_fields = (
                        # 'user', 
                        'item', 
                        # 'price', 
                        'quantity', 
                        # 'amount',
                        'color',
                        "size",
                        # 'name',
                        # 'order_code',
                        # 'order',
                        'cancelled_reason_sms',
                        'returns_reason_sms',
                        'user_returns_status',
                        'user_cancelled_status',
                        # 'orderid',
                        
                        )
    # can_delete = False
    extra = 0
    show_change_link = True


class OrderShippingAddressline(admin.TabularInline):
    model = OrderShippingAddress

    fields = (
        'fast_name',
        'last_name',
        'phone',
        "address",
        'district',
        'division',
        'zip_code',

    )
    readonly_fields = (
                       
                        'fast_name',
                        'last_name',
                        'phone',
                        "address",
                        'district',
                        'division',
                        'zip_code',

                        )

    extra = 0
    show_change_link = True


class Paymentline(admin.TabularInline):
    model = Payment

    fields = (
        'transactionID',
        'taka',
        "user",
        'order',
        
    )
    readonly_fields = (

       'transactionID',
        'taka',
        "user",
        'order',

    )

    extra = 0
    show_change_link = True





def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'coupon',
                    # order_pdf
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',

        'coupon'
    ]

    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]
    inlines = [OrderProductline, OrderShippingAddressline, Paymentline]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']
   

class BullingAddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'email',
        'phone',
        'district',
        'division',
    ]
    list_filter = ['phone', ]
    search_fields = ['phone']


class ShippingAddressdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'email',
        'shopping_phone',
        'shopping_district',
        'shopping_division',
    ]
    list_filter = ['shopping_phone', ]
    search_fields = ['shopping_phone']

    

class OrderShippingAddressdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'email',
        'phone',
        'district',
        'division',
    ]
    list_filter = ['phone', ]
    search_fields = ['phone']






class AccountsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
  
    ]




class LoginSecurityAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
  
    ]



class YourPaymentsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
  
    ]



class YourProfileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
  
    ]



class OrbitplugGuidelineAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
  
    ]



class YourCanTryForSellAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
  
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Variants, VariantsAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(ProductImages)
admin.site.register(AllProductMainImages)
admin.site.register(AllProductImages)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Images)
admin.site.register(Details)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(OderProduct)
admin.site.register(ShippingAddress, ShippingAddressdmin)
admin.site.register(BullingAddress, BullingAddressAdmin)
admin.site.register(Accounts, AccountsAdmin)
admin.site.register(YourOrders, AccountsAdmin)
admin.site.register(LoginSecurity, LoginSecurityAdmin)
admin.site.register(YourPayments, YourPaymentsAdmin)
admin.site.register(YourProfile, YourProfileAdmin)
admin.site.register(OrbitplugGuideline, OrbitplugGuidelineAdmin)
admin.site.register(YourCanTryForSell, YourCanTryForSellAdmin)



