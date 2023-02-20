from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import *
from authentication.models import *
# variation = Size
from home.models import *
from rest_framework_recursive.fields import RecursiveField







class AccountseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = ['name', 'image', 'description','link','appslink']




class YourOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = YourOrders
        fields = ['name', 'image', 'description','link' ,'appslink']



class LoginSecuritySerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginSecurity
        fields = ['name', 'image', 'description','link','appslink']




class YourPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourPayments
        fields = ['name', 'image','phone','appslink']




class YourProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = YourProfile
        fields = ['name', 'image', 'description','link','appslink']


class OrbitplugGuidelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrbitplugGuideline
        fields = ['name', 'image', 'description','link','appslink']


class YourCanTryForSellSerializer(serializers.ModelSerializer):

    class Meta:
        model = YourCanTryForSell
        fields = ['name', 'image', 'description','link','appslink']




class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'children']



class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class BullingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BullingAddress
        fields = (
            'user',
            'fast_name',
            'last_name',
            'phone',
            'address',
            'district',
            'division',
            'zip_code',
           
        )


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            'shopping_fast_name',
            'shopping_last_name',
            'shopping_phone',
            'shopping_address',
            'shopping_district',
            'shopping_division',
            'shopping_zip_code',
            'id',
            "user_id",

           
        )





class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = (
            'id',
            'code',
            'amount'
        )




class VariationDetailSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = Size
        fields = (
            'id',
            'name',
            'code'
        )

    def get_item(self, obj):
        return ItemSerializer(obj.item).data


class ItemVariationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variants
        fields = (
            'id',
            'title',
            'item',
            'price',
            'size',
            'color',
        )


class OrderItemSerializer(serializers.ModelSerializer):
    item_variations = serializers.SerializerMethodField()
    item = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'item',
            'item_variations',
            'quantity',
            'final_price',
            'get_total_quantity'
        )

    def get_item(self, obj):
        return ItemSerializer(obj.item).data

    def get_item_variations(self, obj):
        return ItemVariationDetailSerializer(obj.item_variations.all(), many=True).data

    def get_final_price(self, obj):
        return obj.get_final_price()


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    coupon = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'order_items',
            'total',
            'coupon',
            'start_date',
            "received",
            'status',
            'order_code',
            'refund_requested',
            'shiping_status',
            'returns_status',
            'cancelled_status',
            'get_total_quantites'
        )

    def get_order_items(self, obj):
        return OrderItemSerializer(obj.items.all(), many=True).data

    def get_total(self, obj):
        return obj.get_total()

    def get_coupon(self, obj):
        if obj.coupon is not None:
            return CouponSerializer(obj.coupon).data
        return None


class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variants
        fields = (
            'id',
            'title',
            'item',
            'image_id',
            'image',
            'color',
            'size'
        )

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Images
#         fields = (
#             'id',
#             'title',
#             'image'
#         )

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = (
            'id',
            'title',
            'image'
        )


class UserOrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OderProduct
        fields = (
            'id',
            'name',
            'email',
            'order',
            'color',
            'item',
            "amount",
            'size',
            'quantity',
            'price',
            'order_code',
            'status',
            'created_at',
            'update_at',
            'imageUrl',
            'user_returns_status',
            'user_cancelled_status',
            'itemId'
 
        )


class OrderCancelledandReturnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OderProduct
        fields = (
         
            'user_returns_status',
            'user_cancelled_status',
            'cancelled_reason_sms',
            'returns_reason_sms',
        )


class UserOrderSerializer(serializers.ModelSerializer):
    orderproduct = UserOrderDetailSerializer(many=True, read_only=True, source='oderproduct_set')

    class Meta:
        model = Order
        fields = (
            'id',
            'orderproduct',
        )





class ItemDetailSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    variations = VariationSerializer( many=True, read_only=True, source='variants_set')
    images = ProductImagesSerializer(many=True, read_only=True, source='productimages_set')

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'category',
            'shipping_time',
            'product_status',
            'description',
            'slug',
            'description',
            'image',
            'variations',
            'images',
            'detail',
            'image_detail',
            "note",
            "minamount",
            "amount",
            "collection_details",
            "status",
            "stock_status",
            "cost_price",
            "sell_price",
        )

    # def get_category(self, obj):
    #     return obj.get_category_display()



    def get_variations(self, obj):
        return ItemVariationSerializer(obj.variation_set.all(), many=True).data


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'id',
            'user_id',
            'email',
            'fast_name',
            'last_name',
            'user_name',
            'address',
            'district',
            # 'image',
            'division',
            'phone',
            'zip_code',

        )





class AddressSerializer(serializers.ModelSerializer):
    country = CountryField()

    class Meta:
        model = Address
        fields = (
            'id',
            'user',
            'street_address',
            'apartment_address',
            'country',
            'zip',
            'address_type',
            'default'
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'taka',
            'transactionID'
        )



class ItemSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    variations = VariationSerializer( many=True, read_only=True, source='variants_set')
    images = ProductImagesSerializer(many=True, read_only=True, source='productimages_set')

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'category',
            'shipping_time',
            'product_status',
            'description',
            'slug',
            'description',
            'image',
            'variations',
            'images',
            'detail',
            'image_detail',
            "note",
            "minamount",
            "amount",
            "collection_details",
            "status",
            "stock_status",
        )

    # def get_category(self, obj):
    #     return obj.get_category_display()



    def get_variations(self, obj):
        return ItemVariationSerializer(obj.variation_set.all(), many=True).data
