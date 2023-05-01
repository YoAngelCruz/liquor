import graphene

import liquors.schema


class Query(liquors.schema.Query, graphene.ObjectType):
    pass

class Mutation(liquors.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)