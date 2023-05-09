from django.forms import ModelForm
from app.models import Jogos

# Create the form class
class JogosForm(ModelForm):
    class Meta:
        model = Jogos
        fields = ['jogo', 'plataforma', 'desenvolvedor']