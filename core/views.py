from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
  template_name = 'index.html'


class DadosJSONView(BaseLineChartView):
  def get_labels(self):
    """
    Retorna as labels para o eixo x
    """
    labels = [
      "Janeiro",
      "Fevereiro",
      "Março",
      "Abril",
      "Maio",
      "Junho",
      "Julho",
      "Agosto",
      "Setembro",
      "Outubro",
      "Novembro",
      "Dezembro"
    ]

    return labels
  
  def get_providers(self):
    """
    Retorna os nomes dos datasets
    """
    datasets = [
      "Curso 1",
      "Curso 2",
      "Curso 3",
      "Curso 4", 
      "Curso 5",
      "Curso 6"
    ]

    return datasets
  
  def get_data(self):
    """
    Retorna os datasets para plotar no gráfico
    """
    dados = []
    for l in range(6):
      for c in range(12):
        dado = [
          randint(1, 200), #jan
          randint(1, 200), #fev
          randint(1, 200), #mar
          randint(1, 200), #abr
          randint(1, 200), #mai
          randint(1, 200), #jun
          randint(1, 200), #jul
          randint(1, 200), #ago
          randint(1, 200), #set
          randint(1, 200), #out
          randint(1, 200), #nov
          randint(1, 200)  #dez
        ]
      dados.append(dado)
    return dados


