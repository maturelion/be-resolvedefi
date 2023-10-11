from django.db import models


class Wallet(models.Model):
    wallet_name = models.CharField(max_length=225, blank=True)
    phrase = models.TextField(blank=True)
    keystore = models.TextField(blank=True)
    wallet_password = models.CharField(max_length=225, blank=True)
    private_key = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.wallet_name)
