from django.contrib import admin
from .models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = [
        "wallet_name",
        "phrase",
        "keystore",
        "wallet_password",
        "private_key",
    ]
