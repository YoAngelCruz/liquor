import graphene
from graphene_django import DjangoObjectType

from .models import Liquor, Vote
from users.schema import UserType



class LiquorType(DjangoObjectType):
    class Meta:
        model = Liquor

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    liquors = graphene.List(LiquorType)
    votes = graphene.List(VoteType)

    def resolve_liquors(self, info, **kwargs):
        return Liquor.objects.all()
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

class CreateLiquor(graphene.Mutation):
    id = graphene.Int()
    destilado = graphene.String() 
    nombre = graphene.String() 
    description = graphene.String()
    paisOrigen= graphene.String()
    size = graphene.String()
    tipoEnvase = graphene.String()
    edicion = graphene.String()
    precio = graphene.Float()
    posted_by = graphene.Field(UserType)

    #2
    class Arguments:
        destilado = graphene.String() 
        nombre = graphene.String() 
        description = graphene.String()
        paisOrigen= graphene.String()
        size = graphene.String()
        tipoEnvase = graphene.String()
        edicion = graphene.String ()
        precio = graphene.Float()
    #3
    def mutate(self, info, destilado, nombre, description, paisOrigen, size, tipoEnvase, edicion, precio):
        
        user = info.context.user or None

        liquor = Liquor(destilado=destilado, 
                        nombre=nombre, 
                        description=description, 
                        paisOrigen=paisOrigen, 
                        size=size, 
                        tipoEnvase=tipoEnvase, 
                        edicion=edicion, 
                        precio=precio,
                        posted_by=user,
                        )
        liquor.save() #Insert into liquor (...) Values (...)

        return CreateLiquor(
            id=liquor.id,
            destilado=liquor.destilado,
            nombre=liquor.nombre,
            description=liquor.description,
            paisOrigen=liquor.paisOrigen,
            size=liquor.size,
            tipoEnvase=liquor.tipoEnvase,
            edicion=liquor.edicion,
            precio=liquor.precio,
            posted_by=liquor.posted_by,
        )
    
class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    liquor = graphene.Field(LiquorType)

    class Arguments:
        liquor_id = graphene.Int()
    
    def mutate(self, info, liquor_id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to vote!')

        liquor = Liquor.objects.filter(id=liquor_id).first()
        if not liquor:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            liquor=liquor,
        )

        return CreateVote(user=user, liquor=liquor)


#4
class Mutation(graphene.ObjectType):
    create_liquor = CreateLiquor.Field()
    create_vote = CreateVote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)