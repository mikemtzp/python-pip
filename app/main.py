import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda x: x['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type country => ')

  result = utils.get_population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values, country['Country/Territory'])


if __name__ == '__main__':
  run()