# -*- coding: utf-8 -*-
import json

from django.contrib.admin.views.main import ChangeList
from django.db.models import Count
from django.contrib import admin


class ChangeListMixin(ChangeList):

    chart_group_by = None

    def get_results(self, request):
        super(ChangeListMixin, self).get_results(request)

        def change_none_to_str(value):
            if value is None:
                return 'Value is not specified'
            return value

        self.piechardata = json.dumps([

            {'name': change_none_to_str(x[self.chart_group_by]), 'y': x['count']}
            for x in self.queryset.all().order_by(self.chart_group_by).values(
                self.chart_group_by
            ).annotate(count=Count('*'))
        ]
        )


class AdminWIthChartsMixin(admin.ModelAdmin):
    def get_changelist_instance(self, request):
        return super().get_changelist_instance(request)

    chart_group_by = None

    def get_changelist(self, request, **kwargs):
        assert self.chart_group_by is not None, 'chart_group_by should be set to model admin instance'

        cls =  super().get_changelist(request, **kwargs)

        return type(
            cls.__name__ + '_WithCharts',
            (ChangeListMixin, cls),
            {
                'chart_group_by': self.chart_group_by,
            }
        )


