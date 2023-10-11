from rest_framework.serializers import ModelSerializer
from .models import Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            "id",
            "wallet_name",
            "phrase",
            "keystore",
            "wallet_password",
            "private_key",
        ]
