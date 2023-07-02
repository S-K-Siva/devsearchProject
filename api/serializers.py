from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Projects.models import Project,Tags,Review
from users.models import Profile,Message,Skill
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__"

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"
    

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message 
        fields = "__all__"

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class ProfileSerializer(ModelSerializer):
    skills = serializers.SerializerMethodField()
    class Meta:
        model = Profile 
        fields = "__all__"

    def get_skills(self,obj):
        skills = obj.skill_set.all()
        serializer = SkillSerializer(skills,many=True)
        return serializer.data
class ProjectSerializer(ModelSerializer):
    author = UserSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_reviews(self,obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data
