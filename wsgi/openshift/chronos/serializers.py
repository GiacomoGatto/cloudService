from rest_framework import serializers
from models import Targets, Missions, Details, Planets, PayloadBusTypes, PayloadBusComps, SciData


class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = ('id', 'name', 'slug', 'body_type', 'image_url', 'characteristics', 'curiosities', 'sim_related', 'use_in_sim')


class MissionsSerializer(serializers.ModelSerializer):
    target = serializers.RelatedField(many=False)
    class Meta:
        model = Missions
        fields = ('id', 'target', 'era', 'name', 'codename', 'hashed', 'image_url', 'link_url', 'launch_dates', 'twitter', 'fb_page', 'nasa', 'esa', 'jaxa')


class DetailsSerializer(serializers.ModelSerializer):
    mission = serializers.RelatedField(many=False)
    class Meta:
        model = Details
        fields = ('id', 'mission', 'detail_type', 'header', 'body', 'date', 'image_link')


class PlanetsSerializer(serializers.ModelSerializer):
    #target = serializers.RelatedField(many=False)
    class Meta:
        model = Planets
        fields = ('target', 'discover', 'rings', 'light', 'mass', 'diameter', 'density', 'gravity', 'l_day', 'l_year', 'eccent', 'distance', 'perihelion', 'aphelion', 'inclination', 'active', 'atmosphere')


class PayloadBusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayloadBusTypes
        fields = ('id', 'name', 'category', 'description', 'link')


class PayloadBusCompsSerializer(serializers.ModelSerializer):
    pbtype = serializers.RelatedField(many=True)
    class Meta:
        model = PayloadBusComps
        fields = ('id', 'pbtype', 'name', 'description', 'slug', 'link', 'category')


class SciDataSerializer(serializers.ModelSerializer):
    component = PayloadBusCompsSerializer(many=True)
    mission = MissionsSerializer(many=False)

    class Meta:
        model = SciData
        fields = ('id', 'data_scope', 'data_type', 'header', 'component', 'mission', 'body', 'comment', 'related_to')

SciDataSerializer.base_fields['related_to'] = SciDataSerializer()

