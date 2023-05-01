from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.


from liquors.schema import schema
from liquors.models import Liquor

LIQUORS_QUERY = '''
{
  liquors{
    id,
    destilado,
    nombre,
    description
  }
}
'''
CREATE_LIQUORS_MUTATION = '''
 mutation createLiquorMutation($destilado: String,$nombre: String,$description: String,$paisOrigen: String,$size: String,$tipoEnvase: String,$edicion: String,$precio: Float) {
     createLiquor(destilado: $destilado,nombre: $nombre,description: $description,paisOrigen: $paisOrigen,size: $size,tipoEnvase: $tipoEnvase,edicion: $edicion,precio: $precio) {
        nombre
     }
 }
'''

class LiquorTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.liquor1 = mixer.blend(Liquor)
        self.liquor2 = mixer.blend(Liquor)
    
    def test_liquors_query(self):
        response = self.query(
            LIQUORS_QUERY,
        )


        content = json.loads(response.content)
        # print(content)
        self.assertResponseNoErrors(response)
        print("query liquors results ")
        print(content)
        assert len(content['data']['liquors']) == 2

    def test_createLiquor_mutation(self):

        response = self.query(
            CREATE_LIQUORS_MUTATION,
            variables={'destilado':'Tequila','nombre':'Sinsimito','description':'Tequila del rubio','paisOrigen':'Mexico','size':'750ml','tipoEnvase':'cristal','edicion':'premium','precio':250000.0}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createLiquor": {"nombre":"Sinsimito"}}, content['data'])
