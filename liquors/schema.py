import graphene
from graphene_django import DjangoObjectType

from .models import Liquor


class LiquorType(DjangoObjectType):
    class Meta:
        model = Liquor


class Query(graphene.ObjectType):
    liquors = graphene.List(LiquorType)

    def resolve_liquors(self, info, **kwargs):
        return Liquor.objects.all()

class CreateLiquor(graphene.Mutation):
    id = graphene.Int()
    destilado = graphene.String() 
    nombre = graphene.String() 
    description = graphene.String()
    paisOrigen= graphene.String()
    size = graphene.String()
    tipoEnvase = graphene.String()
    edicion = graphene.String ()
    precio = graphene.Float()

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
        liquor = Liquor(destilado=destilado, 
                        nombre=nombre, 
                        description=description, 
                        paisOrigen=paisOrigen, 
                        size=size, 
                        tipoEnvase=tipoEnvase, 
                        edicion=edicion, 
                        precio=precio)
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
            precio=liquor.precio
        )


#4
class Mutation(graphene.ObjectType):
    create_liquor = CreateLiquor.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)