from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_XML
from wishlist.views import show_wishlist_JSON
from wishlist.views import show_json_by_id
from wishlist.views import show_xml_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_XML, name='show_wishlist_XML'),
    path('json/', show_wishlist_JSON, name='show_wishlist_JSON'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]