import random
from rest_framework import generics
from rest_framework import filters
from django_countries import countries
from django.db.models import Q
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Item, OrderItem, Order
from .serializers import *
from .models import *
from authentication.models import *
from django.utils.crypto import get_random_string
from django.http import JsonResponse
import json
import stripe
from home.models import *
from django.core import serializers
from django.template.loader import get_template
from io import BytesIO
# from xhtml2pdf import pisa
from django.http import HttpResponse
from slugify import slugify

import datetime
from datetime import datetime, timedelta


# class AdminOrderDetailView(ListAPIView):
#     # permission_classes = (IsAuthenticated, )
#     serializer_class = UserOrderDetailSerializer

#     def post_queryset(self, request, *args, **kwargs):
#         return OderProduct.objects.filter( status='Completed')

class AdminDashBoardView(APIView):
    # serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        total_products = Item.objects.all()
        total_products = Item.objects.all()

        last_month = datetime.today() - timedelta(days=30)


        in_stock_products = Item.objects.filter(
            stock_status="In Stock").order_by('-id')
        pre_order_products = Item.objects.filter(
            stock_status="Pre-Orders Products").order_by('-id')

        up_coming_products = Item.objects.filter(
            stock_status="Up Coming Products").order_by('-id')        
        out_of_stock_products = Item.objects.filter(
            stock_status="Out of Stock").order_by('-id')


        in_stock_products = len(in_stock_products)
        pre_order_products = len(pre_order_products)
        up_coming_products = len(up_coming_products)
        out_of_stock_products = len(out_of_stock_products)

        last_month = datetime.today() - timedelta(days=30)


        total_sell = OderProduct.objects.filter(created_at__gte=last_month )
        total_return = OderProduct.objects.filter(created_at__gte=last_month ,status='Return')
        total_cencelled = OderProduct.objects.filter(created_at__gte=last_month ,status='Cencelled')




        total_sell_prices =[]
        for i in total_sell:
            total_sell_prices.append(i.price *i.quantity)
        total_sell_prices = sum(total_sell_prices)


        total_return_prices =[]
        for i in total_return :
            total_return_prices.append(i.price *i.quantity)
        total_return_prices = sum(total_return_prices)

        total_cencelled_prices =[]
        for i in total_cencelled :
            total_cencelled_prices.append(i.price *i.quantity)
        total_cencelled_prices = sum(total_cencelled_prices)








        responseData = {
            'status': 'success',
            "in_stock_products": in_stock_products,
            "pre_order_products": pre_order_products,
            "up_coming_products": up_coming_products,
            "total_sell_prices": total_sell_prices,
            "out_of_stock_products": out_of_stock_products,
            "total_cencelled_prices": total_cencelled_prices,
            "total_return_prices": total_return_prices,

        }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)

class AdminInstockProductsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    queryset = Item.objects.filter(stock_status = "In Stock").order_by('-id')



class AdminOutOfSockProductsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    queryset = Item.objects.filter(stock_status = "Out of Stock").order_by('-id')




class AdminPreOrderProductsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    queryset = Item.objects.filter(stock_status = "Pre-Orders Products").order_by('-id')



class AdminUpComingProductsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    queryset = Item.objects.filter(stock_status = "Up Coming Products").order_by('-id')



class AdminSingleOrderDetailUpdateView(APIView):
    # serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        orderId = request.data['orderId']
        returns_status = request.data['returns_status']
        returns_reason_sms = request.data['returns_reason_sms']
        cancelled_status = request.data['cancelled_status']
        cancelled_reason_sms = request.data['cancelled_reason_sms']
        status = request.data['status']
        other_status = request.data['other_status']

        oder_product_update =OderProduct.objects.filter(id = orderId)
        oder_product_update.update(
              returns_status =returns_status,
              returns_reason_sms=returns_reason_sms,
              cancelled_status=cancelled_status,
              cancelled_reason_sms=cancelled_reason_sms,
              status=status,
              other_status=other_status,
        )



        oder_product = OderProduct.objects.filter(id = orderId).values(
            'id',
            'order',
            'user',
            'item',
            'item__image',
            'name',
            'orderid',
            'color',
            'size',
            'quantity',
            'price',
            "amount",
            'order_code',
            'status',
            'created_at',
            'shiping_status',
            'other_status',
            'returns_status',
            'cancelled_status',
            'returns_reason_sms',
            'cancelled_reason_sms',
            'user_returns_status',
            'user_cancelled_status'


        )
        oder_product = list(oder_product)

 
        responseData = {'status': 'success',"oder_product":oder_product }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)



class AdminSingleOrderDetailView(APIView):
    # serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        orderId = request.data['orderId']



        oder_product = OderProduct.objects.filter(id = orderId).values(
            'id',
            'order',
            'user',
            'item',
            'item__image',
            'name',
            'orderid',
            'color',
            'size',
            'quantity',
            'price',
            "amount",
            'order_code',
            'status',
            'created_at',
            'shiping_status',
            'other_status',
            'returns_status',
            'cancelled_status',
            'returns_reason_sms',
            'cancelled_reason_sms',
            'user_returns_status',
            'user_cancelled_status'


        )
        data = Order.objects.filter().values(
            'being_delivered',
            'billing_address_id',
            'cancelled_status',
            'coupon_id',
            'id',
            'order_code',
            'ordered',
            'ordered_date',
            'received',
            'ref_code',
            'refund_granted',
            'returns_status',
            'shiping_status',
            'shipping_address_id',
            'start_date',
            'status',
            'user_id',
            # 'item_id',
            'user__email',


        )
        data = list(data)
        oder_product = list(oder_product)
 
        responseData = {'status': 'success', 'data': data ,"oder_product":oder_product }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)










class AdminOrderDetailView(APIView):
    # serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        orderId = request.data['orderId']



        oder_product = OderProduct.objects.filter(order_id = orderId).values(
            'id',
            'order',
            'user',
            'item',
            'item__image',
            'name',
            'orderid',
            'color',
            'size',
            'quantity',
            'price',
            "amount",
            'order_code',
            'status',
            'created_at',
            'shiping_status',
            'other_status',
            'returns_status',
            'cancelled_status',
            'returns_reason_sms',
            'cancelled_reason_sms',
            'user_returns_status',
            'user_cancelled_status'


        ).order_by('-id')
        data = Order.objects.filter().values(
            'being_delivered',
            'billing_address_id',
            'cancelled_status',
            'coupon_id',
            'id',
            'order_code',
            'ordered',
            'ordered_date',
            'received',
            'ref_code',
            'refund_granted',
            'returns_status',
            'shiping_status',
            'shipping_address_id',
            'start_date',
            'status',
            'user_id',
            # 'item_id',
            'user__email',


        ).order_by('-id')
        data = list(data)
        oder_product = list(oder_product)
 
        responseData = {'status': 'success', 'data': data ,"oder_product":oder_product }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)





class AdminAllOrderView(APIView):
    # serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = Order.objects.filter().values(
            'being_delivered',
            'billing_address_id',
            'cancelled_status',
            'coupon_id',
            'id',
            'order_code',
            'ordered',
            'ordered_date',
            'received',
            'ref_code',
            'refund_granted',
            'returns_status',
            'shiping_status',
            'shipping_address_id',
            'start_date',
            'status',
            'user_id',
            # 'item_id',
            'user__email',


        ).order_by('-id')
        data = list(data)
 
        responseData = {'status': 'success', 'data': data , }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)




class AdminAllReturnsOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter( status='Return').order_by('-id')





class AdminAllCompletesOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter( status='Completed').order_by('-id')





class AdminAllCencelledOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter(status='Cencelled').order_by('-id')

class AdminAllNewOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter(status='New').order_by('-id')






class UploadImagesAndVideosView(APIView):
    def post(self, request, *args, **kwargs):
        # caption = request.data.get('caption', None)
        images = request.data.getlist('image', None)

        # type = request.data.getlist('type', None)
        # print(request.data['_parts'][0],'.....')
        print(request.data, '.....')
        print(request.data['image'],'.....')
        # dd= json.loads(request.data['image'])
        # print (dd,',,,,,,,,,,,,,,,,,,ddd')
        data = []

        if images:
            for image in images:
                image_url = AllProductImages.objects.create(image=image)
                print(image_url.image)
                data.append(str(image_url.image))

        # # data = list(data
        responseData = {'status': 'success', 'data': data}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)

class UploadProductMainImagesAndVideosView(APIView):
    def post(self, request, *args, **kwargs):
        # caption = request.data.get('caption', None)
        images = request.data.getlist('image', None)

        # type = request.data.getlist('type', None)
        # print(request.data['_parts'][0],'.....')
        print(request.data, '.....')
        print(request.data['image'],'.....')
        # dd= json.loads(request.data['image'])
        # print (dd,',,,,,,,,,,,,,,,,,,ddd')
        data = []

        if images:
            for image in images:
                image_url = AllProductMainImages.objects.create(image=image)
                print(image_url.image)
                data.append(str(image_url.image))

        # # data = list(data
        responseData = {'status': 'success', 'data': data}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)











class UplodedProductUpdates(ListAPIView):

    def post(self, request, *args, **kwargs):
        productName = request.data['productName']
        status = request.data['status']
        category = request.data['category']
        variant = request.data['variant']
        minamount = request.data['minamount']
        note = request.data['note']
        shippingTime = request.data['shippingTime']
        price = request.data['price']
        discountPrice = request.data['discountPrice']
        quantity = request.data['quantity']
        shortDescription = request.data['shortDescription']
        detail = request.data['detail']
        imageDetail = request.data['imageDetail']
        productStatus = request.data['productStatus']
        images = request.data['images']
        image = request.data['image']
        productId = request.data['productId']
        sellPrice = request.data['sellPrice']
        constPrice = request.data['constPrice']
        stockStatus = request.data['stockStatus']
        # slug = request.data['slug']
        # print (slug,'slugslugslug')
        searching_product = Item.objects.filter(id=productId)

        create_item = searching_product.update(
            # category=category,
            title=productName,
            description=shortDescription,
            # image=image[0]["images"],
            price=price,
            discount_price=discountPrice,
            amount=quantity,
            minamount=minamount,
            variant=variant,
            detail=detail,
            image_detail=imageDetail,
            slug=slugify(productName),
            product_status=productStatus,
            note=note,
            shipping_time=shippingTime,
            status=status,
            stock_status=stockStatus,
            cost_price=constPrice,
            sell_price=sellPrice,
            
            )
            
        # if searching_product:
        #     if category:
        #         for i in category:
        #             create_item.category.add(i)


        # for i in images:
        #     ProductImages.objects.create(product_id =create_item.id,image=i["images"])





        # print (detail)

        responseData = {'status': 'success', }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)



class ProductUploadView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserOrderSerializer
    def post(self, request, *args, **kwargs):
        productName = request.data['productName']
        status = request.data['status']
        category = request.data['category']
        variant = request.data['variant']
        minamount = request.data['minamount']
        note = request.data['note']
        shippingTime = request.data['shippingTime']
        price = request.data['price']
        discountPrice = request.data['discountPrice']
        quantity = request.data['quantity']
        shortDescription = request.data['shortDescription']
        detail = request.data['detail']
        imageDetail = request.data['imageDetail']
        productStatus = request.data['productStatus']
        images = request.data['images']
        image = request.data['image']
        stockStatus = request.data['stockStatus']
        constPrice = request.data['constPrice']
        sellPrice = request.data['sellPrice']
        # slug = request.data['slug']
        # print (slug,'slugslugslug')

        create_item = Item.objects.create(
            # category=category,
            title=productName,
            description=shortDescription,
            image=image[0]["images"],
            price=price,
            discount_price=discountPrice,
            amount=quantity,
            minamount=minamount,
            variant=variant,
            detail=detail,
            image_detail=imageDetail,
            slug=slugify(productName),
            product_status=productStatus,
            note=note,
            shipping_time=shippingTime,
            status=status,
            stock_status=stockStatus,
            cost_price=constPrice,
            sell_price=sellPrice,
            
            )
            
        if create_item:
            for i in category:
                create_item.category.add(i)


        for i in images:
            ProductImages.objects.create(product_id =create_item.id,image=i["images"])


        responseData = {'status': 'success', }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)









class AccountsView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AccountseSerializer
    queryset = Accounts.objects.all()

class YourOrdersView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = YourOrdersSerializer
    queryset = YourOrders.objects.all()




class LoginSecurityView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSecuritySerializer
    queryset = LoginSecurity.objects.all()




class YourPaymentsView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = YourPaymentsSerializer
    queryset = YourPayments.objects.all()




class YourProfileView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = YourProfileSerializer
    queryset = YourProfile.objects.all()




class OrbitplugGuidelineView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = OrbitplugGuidelineSerializer
    queryset = OrbitplugGuideline.objects.all()




class YourCanTryForSellView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = YourCanTryForSellSerializer
    queryset = YourCanTryForSell.objects.all()

















class AllCategoryListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class RelatedProductsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    # queryset = PhoneHomePageProductListSlider10.objects.all()

    def get(self, request, pk,  *args, **kwargs):
        data = Item.objects.filter(category=pk[0])
        data = list(data.values())

        if len(data) == 1:
            data = random.sample(data, 1)

        elif len(data) == 2:
            data = random.sample(data, 2)
            

        elif len(data) == 3:
            data = random.sample(data, 3)
            

        elif len(data) == 4:
            data = random.sample(data, 4)
            
        elif len(data) == 5:
            data = random.sample(data, 5)
        elif len(data) == 6:
            data = random.sample(data, 3)
        elif len(data) == 7:
            data = random.sample(data, 7)
        elif len(data) == 8:
            data = random.sample(data, 8)
        elif len(data) == 9:
            data = random.sample(data, 9)
        elif len(data) == 10:
            data = random.sample(data, 10)
        elif len(data) >= 11:
            data = random.sample(data, 11)




# ....................................................................

        if len(pk) > 1:
            print(pk[1])


            data2 = Item.objects.filter(category=pk[2])
            data2 = list(data2.values())
            # print (data2)

            if len(data2) >= 1:
                data2 = random.sample(data, 1)

            elif len(data2) >= 2:
                data2 = random.sample(data, 2)
            elif len(data2) >= 3:
                data2 = random.sample(data, 3)

            elif len(data2) >= 4:
                data2 = random.sample(data, 4)

            elif len(data2) >= 5:
                data2 = random.sample(data, 5)
            elif len(data2) >= 6:
                data2 = random.sample(data, 6)
            elif len(data2) >= 7:
                data2 = random.sample(data, 7)
            elif len(data2) >= 8:
                data2 = random.sample(data, 8)
            elif len(data2) >= 9:
                data2 = random.sample(data, 9)
            elif len(data2) >= 10:
                data2 = random.sample(data, 10)
            elif len(data2) >= 11:
                data2 = random.sample(data, 11)
        else:
            data2 = ""







        responseData = {'status': 'success', 'data': data, "data2": data2}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)




class ItemDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()



class CategoryItemsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    # queryset = PhoneHomePageProductListSlider10.objects.all()
    def get(self, request,pk,  *args, **kwargs):
        data = Item.objects.filter(category=pk)
        data = list(data.values())
        responseData = {'status': 'success', 'data': data}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)



# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

#     if not pdf.err:
#         return result.getvalue()

#     return None


def admin_order_pdf(request, pk):
    if request.user.is_superuser:
        order = get_object_or_404(Order, pk=pk)
        order_product = OderProduct.objects.filter(id= pk)


        pdf = render_to_pdf('order_pdf.html', {
                            'order': order,
                             "order_product": order_product
                             
                             
                             })

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            content = "attachment; filename=%s.pdf" % pk
            response['Content-Disposition'] = content

            return response

    return HttpResponse("Not found")





class BullingAddressListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = BullingAddressSerializer

    def get_queryset(self):
        return BullingAddress.objects.filter(user=self.request.user)


class ShippingAddressListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):

        print (self.request.user,'.......................okay')
        
        return ShippingAddress.objects.filter(user=self.request.user)


class ShippingAddressUpdateView(UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ShippingAddressSerializer
    queryset = ShippingAddress.objects.all()






class UserIDView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'userID': request.user.id}, status=HTTP_200_OK)


class ItemListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ItemSerializer
    queryset = Item.objects.all().order_by('-id')




# ............................... Search.........................


class SearchListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'slug']






class UserProfileListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class AllOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter(user=self.request.user.id)
class AllReturnsOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter(user=self.request.user.id, status='Return').order_by('-id')

class AllCompletesOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter(user=self.request.user.id,  status='Completed').order_by('-id')


class AllCencelledOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter(user=self.request.user.id,  status='Cencelled').order_by('-id')


class AllNewOrderProductsListView(ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = UserOrderDetailSerializer

    def get_queryset(self):
        return OderProduct.objects.filter(user=self.request.user.id,  status='New').order_by('-id')






class UserProfileUpdateView(UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all().order_by('-id')

class OrderCancelledandReturnsView(UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = OrderCancelledandReturnsSerializer
    queryset = OderProduct.objects.all().order_by('-id')


class OrderCancelledandReturnsDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserOrderDetailSerializer
    queryset = OderProduct.objects.all().order_by('-id')





class UserOrderDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserOrderSerializer
    queryset = Order.objects.all().order_by('-id')


class OrderTrackDetailView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserOrderSerializer
    def post(self, request, *args, **kwargs):
        orderid = request.data['orderid']
        data = Order.objects.filter(user=request.user.id, order_code=orderid)
        if data:
            data = list(data.values())
            mess = ""
        else:
            mess = ('Please try again')
            data = ""
        responseData = {'status': 'success', 'data': data , "mess":mess}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)









class OrderListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderQuantityUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        slug = request.data.get('slug', None)
        if slug is None:
            return Response({"message": "Invalid data"}, status=HTTP_400_BAD_REQUEST)
        item = get_object_or_404(Item, slug=slug)
        order_qs = Order.objects.filter(
            user=request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(item__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                else:
                    order.items.remove(order_item)
                return Response(status=HTTP_200_OK)
            else:
                return Response({"message": "This item was not in your cart"}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "You do not have an active order"}, status=HTTP_400_BAD_REQUEST)


class OrderItemDeleteView(DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = OrderItem.objects.all()


class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        slug = request.data.get('slug', None)

        variations = request.data.get('variations', [])

       

        if slug is None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)
        item = get_object_or_404(Item, slug=slug)
        variation_find_id = Item.objects.filter(slug=slug)
        # item = get_object_or_404(Item, slug=slug)


        minimum_variation_count = Variants.objects.filter(item=item).count()
        print (minimum_variation_count)
        print (len(variations))
        if len(variations) == -1:
            return Response({"message": "Please specify the required variation types"}, status=HTTP_400_BAD_REQUEST)

        order_item_qs = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
        )
        for v in variations:
            order_item_qs = order_item_qs.filter(
                Q(item_variations__exact=v)
            )

        if order_item_qs.exists():
            order_item = order_item_qs.first()
            order_item.quantity += 1
            order_item.save()
        else:
            order_item = OrderItem.objects.create(
                item=item,
                user=request.user,
                ordered=False
            )
            order_item.item_variations.add(*variations)
            order_item.save()

        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if not order.items.filter(item__id=order_item.id).exists():
                order.items.add(order_item)
                return Response(status=HTTP_200_OK)

        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            return Response(status=HTTP_200_OK)




class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return order
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")
            # return Response({"message": "You do not have an active order"}, status=HTTP_400_BAD_REQUEST)








# class OrderDetailView(RetrieveAPIView):
# class OrderDetailView(APIView):
#     serializer_class = OrderSerializer
#     permission_classes = (IsAuthenticated,)

#     # def get_object(self):
#     #     try:
#     #         order = Order.objects.get(user=self.request.user, ordered=False)
#     #         return order
#     #     except ObjectDoesNotExist:
#     #         # raise Http404("You do not have an active order")
#     #         return Response({"message": "You do not have an active order"}, status=HTTP_400_BAD_REQUEST)


  
#     def post(self, request, *args, **kwargs):

#         data = OrderItem.objects.filter(user=request.user).values(
#             'quantity',
#              'item_id',
#              'item__title',
#              'item__price',
#              'item__discount_price',
#              'item__image',
#              'user_id',

            
#             )
#         print (data,'...............data')

#         # for i in data :
#             # print(i.quantity)
#             # print(i.item__title)


#         # print (data,'.........s')

# # <QuerySet [{'id': 143, 'user_id': 3, 'ordered': False, 'item_id': 6, 'quantity': 4}]> .........s
#         data = list(data)

#         responseData = {'status': 'success', 'data':data ,}

#         return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class PaymentView(APIView):

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        userprofile = Profile.objects.get(user=self.request.user)
        token = request.data.get('stripeToken')

        ordercode = get_random_string(5).upper()  # random cod
        order.ordered = True
        # order.payment = 1
        # order.billing_address = "billing_address"
        order.order_code = ordercode
        # order.shipping_address = "shipping_address"
        # order.ref_code = create_ref_code()
        order.save()
        order_product = OrderItem.objects.filter(user_id=self.request.user.id)
        current_user = request.user


        for product in order_product:
            
            variation = product.item_variations.distinct()
            if variation:
                for rs in variation:
                    detail = OderProduct()
                    detail.order_id = order.id
                    detail.name = rs.title
                    detail.item_id = rs.item.id
                    detail.user_id = current_user.id
                    detail.quantity = rs.quantity
                    detail.price = rs.price
                    detail.variant_id = rs.id
                    detail.color = rs.color
                    detail.size = rs.size
                    detail.order_code = ordercode
                    detail.amount = (rs.quantity * rs.price)
                    detail.save()
            else:
                detail = OderProduct()
                detail.order_id = order.id
                detail.name = product.item.title
                detail.item_id = product.item.id
                detail.user_id = current_user.id
                detail.quantity = product.quantity
                detail.price = product.item.price
                detail.order_code = ordercode
                detail.amount = (product.quantity * product.item.price)
                detail.save()
        data = ShippingAddress.objects.filter(user=self.request.user)

       
        for i in data:
            detail = OrderShippingAddress()
            detail.order_id = order.id
            detail.user_id = current_user.id
            detail.fast_name = i.shopping_fast_name
            detail.last_name = i.shopping_last_name
            detail.phone = i.shopping_phone
            detail.address = i.shopping_address
            detail.district = i.shopping_district
            detail.division = i.shopping_division
            detail.zip_code = i.shopping_zip_code
            detail.save()


        user_data = request.data
        if user_data:
            payment_detail = Payment()
            transactionId = user_data['transactionId']
            taka = user_data['taka']
            payment_detail.user_id = current_user.id
            payment_detail.order_id = order.id
            payment_detail.transactionID = transactionId
            payment_detail.taka = taka
            payment_detail.save()

       


        OrderItem.objects.filter(user_id=current_user.id).delete()
       

        return Response(status=HTTP_200_OK)

   
        return Response({"message": "Invalid data received"}, status=HTTP_400_BAD_REQUEST)


class AddCouponView(APIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get('code', None)
        if code is None:
            return Response({"message": "Invalid data received"}, status=HTTP_400_BAD_REQUEST)
        order = Order.objects.get(
            user=self.request.user, ordered=False)
        coupon = get_object_or_404(Coupon, code=code)
        order.coupon = coupon
        order.save()
        return Response(status=HTTP_200_OK)


class CountryListView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(countries, status=HTTP_200_OK)


class AddressListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AddressSerializer

    def get_queryset(self):
        address_type = self.request.query_params.get('address_type', None)
        qs = Address.objects.all()
        if address_type is None:
            return qs
        return qs.filter(user=self.request.user, address_type=address_type)


class AddressCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AddressUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AddressDeleteView(DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Address.objects.all()


class PaymentListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)



