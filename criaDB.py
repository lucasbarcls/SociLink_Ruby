from projetoRuby import database, app
from projetoRuby.models import Usuario, Foto


with app.app_context():
     database.create_all()