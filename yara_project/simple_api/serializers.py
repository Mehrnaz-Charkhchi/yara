from rest_framework import serializers

from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer, serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = Purchase
        fields = ['created', 'datetime', 'purchase', 'purchase_id', 'user_id', 'name', 'phone', 'email', 'address']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.created = validated_data.get('created', instance.created)
        return instance
