from rest_framework import serializers
from .models import TravelProject, ProjectPlace
from .services.artic import fetch_place_from_api


class TravelProjectSerializer(serializers.ModelSerializer):
    places = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    # returned list of external_ids
    place_external_ids = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TravelProject
        fields = ('id', 'name', 'description', 'start_date', 'places', 'place_external_ids')

    
    def get_place_external_ids(self, obj):
        return list(obj.places.values_list('external_id', flat=True))


#   Create travel project with places fetched from external API
    def create(self, validated_data):
        external_ids = validated_data.pop('places', [])

        project = TravelProject.objects.create(**validated_data)

        for external_id in external_ids:
            place = ProjectPlace.objects.filter(external_id=external_id).first()
            if not place:
                print(f'Get {external_id} from api')
                response = fetch_place_from_api(external_id)

                if not response:
                    raise serializers.ValidationError(f'Place {external_id} not found in external API')

                place = ProjectPlace.objects.create(
                    external_id = external_id,
                    title = response['data']['title']
                )

            project.places.add(place)

        return project


class ProjectPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPlace
        fields = '__all__'