import graphene
from django.shortcuts import get_object_or_404
from graphene_django import DjangoObjectType
from myapp.models import UserModel, EducationModel

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel

class EducationType(DjangoObjectType):
    class Meta:
        model = EducationModel

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    educations = graphene.List(EducationType)
    education_by_id = graphene.Field(EducationType, id=graphene.Int())

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_educations(self, info):
        return EducationModel.objects.all()

    def resolve_education_by_id(self, info, id):
        return get_object_or_404(EducationModel, pk=id)

class CreateUser(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    last_name = graphene.String()

    class Arguments:
        name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, name, last_name):
        user = UserModel(name=name, last_name=last_name)
        user.save()

        return CreateUser(
            id=user.id,
            name=user.name,
            last_name=user.last_name,
        )

class CreateEducation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    education_type = graphene.String()
    education_length = graphene.String()
    education_pace = graphene.String()
    description = graphene.String()

    class Arguments:
        name = graphene.String()
        education_type = graphene.String()
        education_length = graphene.String()
        education_pace = graphene.String()
        description = graphene.String()

    def mutate(self, info, name, education_type, education_length, education_pace, description):
        education = EducationModel(name=name, education_type=education_type, education_length=education_length, education_pace=education_pace, description=description)
        education.save()

        return CreateEducation(
            id=education.id,
            name=education.name, 
            education_type=education.education_type, 
            education_length=education.education_length, 
            education_pace=education.education_pace, 
            description=education.description
        )

class UpdateEducation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    education_type = graphene.String()
    education_length = graphene.String()
    education_pace = graphene.String()
    description = graphene.String()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        education_type = graphene.String()
        education_length = graphene.String()
        education_pace = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, name, education_type, education_length, education_pace, description):
        education = get_object_or_404(EducationModel, pk=id)
        education.name=name
        education.education_type=education_type
        education.education_length=education_length
        education.education_pace=education_pace
        education.description=description
        education.save()

        return UpdateEducation(
            name=education.name, 
            education_type=education.education_type, 
            education_length=education.education_length, 
            education_pace=education.education_pace, 
            description=education.description
        )

class DeleteEducation(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        education = get_object_or_404(EducationModel, pk=id)
        education.delete()
        return DeleteEducation(id=education.id)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_education = CreateEducation.Field()
    delete_education = DeleteEducation.Field()
    update_education = UpdateEducation.Field()
    
schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)