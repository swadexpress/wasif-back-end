from django.urls import path, include
from .views import *


urlpatterns = [

    #     path('UplodedProduct/', UplodedProduct.as_view(), name='UplodedProduct'),
    path('AdminAllCencelledOrderProductsListView/',
         AdminAllCencelledOrderProductsListView.as_view(), name='AdminAllCencelledOrderProductsListView'),

    path('AdminSingleOrderDetailUpdateView/',
         AdminSingleOrderDetailUpdateView.as_view(), name='AdminSingleOrderDetailUpdateView'),


    path('AdminPreOrderProductsListView/',
         AdminPreOrderProductsListView.as_view(), name='AdminPreOrderProductsListView'),


    path('AdminOutOfSockProductsListView/',
         AdminOutOfSockProductsListView.as_view(), name='AdminOutOfSockProductsListView'),


    path('AdminUpComingProductsListView/',
         AdminUpComingProductsListView.as_view(), name='AdminUpComingProductsListView'),



    path('AdminSingleOrderDetailView/',
         AdminSingleOrderDetailView.as_view(), name='AdminSingleOrderDetailView'),

    path('AdminAllReturnsOrderProductsListView/',
         AdminAllReturnsOrderProductsListView.as_view(), name='AdminAllReturnsOrderProductsListView'),


    path('AdminInstockProductsListView/',
         AdminInstockProductsListView.as_view(), name='AdminInstockProductsListView'),


    path('AdminAllOrderView/',
         AdminAllOrderView.as_view(), name='AdminAllOrderView'),






    path('AdminOrderDetailView/',
         AdminOrderDetailView.as_view(), name='AdminOrderDetailView'),

    path('AdminAllCompletesOrderProductsListView/',
         AdminAllCompletesOrderProductsListView.as_view(), name='AdminAllCompletesOrderProductsListView'),




    path('AdminDashBoardView/',
         AdminDashBoardView.as_view(), name='AdminDashBoardView'),


    path('AdminAllNewOrderProductsListView/',
         AdminAllNewOrderProductsListView.as_view(), name='AdminAllNewOrderProductsListView'),





    path('UplodedProductUpdates/', UplodedProductUpdates.as_view(),
         name='UplodedProductUpdates'),
    path('UploadProductMainImagesAndVideosView/', UploadProductMainImagesAndVideosView.as_view(),
         name='UploadProductMainImagesAndVideosView'),



    path('UploadImagesAndVideosView/', UploadImagesAndVideosView.as_view(),
         name='UploadImagesAndVideosView'),

    path('product-upload/', ProductUploadView.as_view(), name='product-upload'),

    path('AccountsView/', AccountsView.as_view(), name='AccountsView'),
    path('YourOrdersView/', YourOrdersView.as_view(), name='YourOrdersView'),
    path('LoginSecurityView/', LoginSecurityView.as_view(),
         name='LoginSecurityView'),
    path('YourPaymentsView/', YourPaymentsView.as_view(), name='YourPaymentsView'),
    path('YourProfileView/', YourProfileView.as_view(), name='YourProfileView'),
    path('OrbitplugGuidelineView/', OrbitplugGuidelineView.as_view(),
         name='OrbitplugGuidelineView'),
    path('YourCanTryForSellView/', YourCanTryForSellView.as_view(),
         name='YourCanTryForSellView'),
    path('user-id/', UserIDView.as_view(), name='user-id'),
    path('relatedproductslistView/<pk>/',
         RelatedProductsListView.as_view(), name='RelatedProductsListView'),
    path('categoryitemslistview/<pk>/',
         CategoryItemsListView.as_view(), name='categoryitemslistview'),
    path('allcategorylistview/', AllCategoryListView.as_view(),
         name='allcategorylistview'),

    
    path('shippingaddressupdateview/<pk>/',
         ShippingAddressUpdateView.as_view(), name='shippingaddressupdateview'),


    path('shippingaddresslistview/', ShippingAddressListView.as_view(),
         name='shippingaddresslistview'),
    path('bullingaddresslistview/', BullingAddressListView.as_view(),
         name='bullingaddresslistview'),

    path('allneworderproductslistview/', AllNewOrderProductsListView.as_view(),
         name='allneworderproductslistview'),
    path('allcencelledorderproductslistview/', AllCencelledOrderProductsListView.as_view(),
         name='allcencelledorderproductslistview'),
    path('allcompletesorderproductslistview/', AllCompletesOrderProductsListView.as_view(),
         name='allcompletesorderproductslistview'),
    path('allreturnsorderproductslistview/', AllReturnsOrderProductsListView.as_view(),
         name='allreturnsorderproductslistview'),
    path('allorderaroductslistView/', AllOrderProductsListView.as_view(),
         name='allorderaroductslistView'),
    path('ordercancelledandreturnsdetail/<pk>/',
         OrderCancelledandReturnsDetailView.as_view(), name='ordercancelledanddeturnsdetail'),
    path('ordercancelledandreturns/<pk>/',
         OrderCancelledandReturnsView.as_view(), name='ordercancelledandreturns'),
    path('ordertrack/', OrderTrackDetailView.as_view(), name='ordertrack'),

    
    path('search/', SearchListView.as_view(), name='search'),



    path('countries/', CountryListView.as_view(), name='country-list'),
    path('addresses/', AddressListView.as_view(), name='address-list'),
    path('addresses/create/', AddressCreateView.as_view(), name='address-create'),
    path('addresses/<pk>/update/',
         AddressUpdateView.as_view(), name='address-update'),
    path('addresses/<pk>/delete/',
         AddressDeleteView.as_view(), name='address-delete'),

         
    path('products/', ItemListView.as_view(), name='product-list'),



    path('products/<pk>/', ItemDetailView.as_view(), name='product-detail'),
    path('orderdetail/<pk>/', UserOrderDetailView.as_view(), name='order-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('order-summary/', OrderDetailView.as_view(), name='order-summary'),
    path('order/', OrderListView.as_view(), name='order'),
    path('checkout/', PaymentView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('order-items/<pk>/delete/',
         OrderItemDeleteView.as_view(), name='order-item-delete'),
    path('order-item/update-quantity/',
         OrderQuantityUpdateView.as_view(), name='order-item-update-quantity'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('userprofile/', UserProfileListView.as_view(), name='user-profile-list'),
    path('userprofileupdate/<pk>/', UserProfileUpdateView.as_view(),
         name='user-profile-list-update'),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]
