import graphene
from contribution_plan.models import ContributionPlanBundle, ContributionPlan, ContributionPlanBundleDetails
from core import ExtendedConnection, prefix_filterset
from graphene_django import DjangoObjectType
from product.schema import ProductGQLType
from calculation.gql.gql_types import CalculationRulesGQLType

class ContributionPlanGQLType(DjangoObjectType):

    class Meta:
        model = ContributionPlan
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "version": ["exact"],
            "code": ["exact", "istartswith", "icontains", "iexact"],
            "name": ["exact", "istartswith", "icontains", "iexact"],
            **prefix_filterset("benefit_plan__", ProductGQLType._meta.filter_fields),
            **prefix_filterset("calculation__", CalculationRulesGQLType._meta.filter_fields),
            "periodicity": ["exact", "lt", "lte", "gt", "gte"],
            "date_created": ["exact", "lt", "lte", "gt", "gte"],
            "date_updated": ["exact", "lt", "lte", "gt", "gte"],
            "user_created": ["exact"],
            "user_updated": ["exact"],
            "is_deleted": ["exact"]
        }

        connection_class = ExtendedConnection

    @classmethod
    def get_queryset(cls, queryset, info):
        return ContributionPlan.get_queryset(queryset, info)


class ContributionPlanBundleGQLType(DjangoObjectType):

    class Meta:
        model = ContributionPlanBundle
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "version": ["exact"],
            "code": ["exact", "istartswith", "icontains", "iexact"],
            "name": ["exact", "istartswith", "icontains", "iexact"],
            "periodicity": ["exact", "lt", "lte", "gt", "gte"],
            "date_created": ["exact", "lt", "lte", "gt", "gte"],
            "date_updated": ["exact", "lt", "lte", "gt", "gte"],
            "user_created": ["exact"],
            "user_updated": ["exact"],
            "is_deleted": ["exact"]
        }

        connection_class = ExtendedConnection

    @classmethod
    def get_queryset(cls, queryset, info):
        return ContributionPlanBundle.get_queryset(queryset, info)


class ContributionPlanBundleDetailsGQLType(DjangoObjectType):

    class Meta:
        model = ContributionPlanBundleDetails
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "version": ["exact"],
            **prefix_filterset("contribution_plan_bundle__",
                               ContributionPlanBundleGQLType._meta.filter_fields),
            **prefix_filterset("contribution_plan__",
                               ContributionPlanGQLType._meta.filter_fields),
            "date_created": ["exact", "lt", "lte", "gt", "gte"],
            "date_updated": ["exact", "lt", "lte", "gt", "gte"],
            "user_created": ["exact"],
            "user_updated": ["exact"],
            "is_deleted": ["exact"]
        }

        connection_class = ExtendedConnection

    @classmethod
    def get_queryset(cls, queryset, info):
        return ContributionPlanBundleDetails.get_queryset(queryset, info)

