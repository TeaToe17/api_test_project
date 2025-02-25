from rest_framework import serializers
from rest_framework.reverse import reverse


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field="pk",
        read_only=True
        )
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)





    # other_products = serializers.SerializerMethodField(read_only=True)
    # def get_other_products(self,obj):
    #     # print(dir(obj))
    #     user = obj
    #     my_products_qs = user.products_set.all()[:5]
    #     print(my_products_qs)
    #     return UserProductInlineSerializer(my_products_qs,many=True,context=self.context).data