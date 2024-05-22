from  rest_framework import serializers
from rest_framework.reverse import reverse


from .models import Products
from .validators import validate_title_no_hello , unique_product_title
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field="pk",
        read_only=True
        ),
    title = serializers.CharField(read_only=True)

    class Meta:
        model=Products
        fields = [
            "url",
            "title"
        ]

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user",read_only=True)
    # related_products = ProductInlineSerializer(source="user.products_set.all",read_only=True,many=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello,unique_product_title])
    class Meta:
        model = Products
        fields = [
            "owner",
            "pk",
            "url",
            "edit_url",
            # "email",
            "title", 
            "content",
            "price",
            "sale_price",
            # "my_discount",
            "my_user_data",
            # "related_products",
            "public",
        ]
        
    def get_my_user_data(self,obj):
        # print(f"this{self.context.get('request').user}")
        return {
            "username": obj.user.username
        }

    # def validate_title(self,value):
    #     qs = Products.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product title")
    #     return value

    # def create(self,validated_data):
    #     email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     print(email,obj)
    #     return obj

    def get_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)

    def get_edit_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)

    # def get_my_discount(self,obj):
    #     try:
    #         return obj.get_discount()
    #     except:
    #         return None