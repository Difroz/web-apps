from django.db import models, transaction
import csv
import io
from datetime import datetime

from django.db.models import Func, F


class Deal(models.Model):
    customer = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.customer

    @classmethod
    def import_csv(self, csv_file):
        """
        Загружает информацию из csv файла в БД
        :param file: csv
        :return:
        """
        file = csv_file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        data = [line for line in reader]
        base = Deal.objects.all()
        with transaction.atomic():
            for row in data:
                Deal.objects.get_or_create(**row)

    @classmethod
    def data_processing(cls):
        result_list = []
        users = Deal.objects.values('customer').annotate(spend_money=models.Sum('total')).order_by('-spend_money')[:5]
        gems_list = Deal.objects.values('item', 'customer').filter(
            customer__in=users.values_list('customer', flat=True))
        gems = gems_list.values('item').annotate(unique_usr=models.Count('customer', distinct=True)).filter(
            unique_usr__gte=2)

        for i in users:
            user_dict = {}
            user_dict['username'] = i['customer']
            user_dict['spend_money'] = i['spend_money']
            gem = gems_list.values('item').filter(models.Q(item__in=gems.values('item')) & models.Q(customer=i['customer'])).distinct()
            user_dict['gems'] = list(gem.values_list('item', flat=True))
            result_list.append(user_dict)
        print(result_list)
        return result_list






