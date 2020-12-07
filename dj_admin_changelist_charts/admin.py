# -*- coding: utf-8 -*-
import json

from django.contrib.admin.views.main import ChangeList
from django.db import transaction, connection, OperationalError
from django.db.models import Count
from django.contrib import admin


class ChangeListMixin(ChangeList):


    def get_results(self, request):
        super(ChangeListMixin, self).get_results(request)

        def _change_none_to_str(value):
            if value is None:
                return self.model_admin.chart_null_value_text
            if value is '':
                return self.model_admin.chart_empty_value_text
            return value

        with transaction.atomic(), connection.cursor() as cursor:
            if self.model_admin.chart_sql_execution_time_limit_msec:
                cursor.execute('SET LOCAL statement_timeout TO %s;' % self.model_admin.chart_sql_execution_time_limit_msec)

            try:
                attr = self.model_admin.chart_group_by_attr

                res = [
                    {'name': _change_none_to_str(x[attr]), 'y': x['count']} for x in
                          self.queryset.all().order_by(attr).values(attr).annotate(count=Count('*'))
                ]


                limit = self.model_admin.chart_number_of_groups_limit
                if limit:
                    res = sorted(res, key=lambda x: x['count'], reverse=True)
                    res = res[:limit]

                    self.chart_warning = 'Amount of groups is too big: %s . Only top %s groups displayed in the chart.'

                self.piechardata = json.dumps(res)
            except OperationalError:  # Skip in case timeout error
                pass


class AdminWIthChartsMixin(admin.ModelAdmin):
    def get_changelist_instance(self, request):
        return super().get_changelist_instance(request)

    chart_group_by_attr = None
    chart_number_of_groups_limit = None
    chart_sql_execution_time_limit_msec = 0 # Enable it for postgres. Sqlite doesn't support `SET LOCAL statement_timeout TO`
    chart_null_value_text = 'Value is not specified'
    chart_empty_value_text = 'Value is empty string'


    def get_changelist(self, request, **kwargs):
        assert self.chart_group_by_attr is not None, 'chart_group_by should be set to model admin instance'

        cls =  super().get_changelist(request, **kwargs)

        return type(
            cls.__name__ + '_WithCharts',
            (ChangeListMixin, cls),
            {}
        )


