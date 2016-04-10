from Disaster.models import TodoList
from Disaster.serializers import TodoListSerializer
from swampdragon_tokenauth.mixins import TokenAuthMixin
from swampdragon.route_handler import ModelRouter
from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter

class TodoListRouter(TokenAuthMixin, ModelRouter):
    route_name = 'toask-item'
    serializer_class = TodoListSerializer
    model = TodoList
    permission_classes = [LoginRequired()]

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(user=self.connection.user)
