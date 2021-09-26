from django.test import TestCase
from .models import Film, Chart


class FilmModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Film.objects.create(title='Test film')
        Film.objects.create(url='Test url')

    def test_title_content(self):
        film = Film.objects.get(film_id=1)
        expected_object_name = f'{film.title}'
        self.assertEquals(expected_object_name, 'Test film')

    def test_url_content(self):
        film = Film.objects.get(film_id=2)
        expected_object_name = f'{film.url}'
        self.assertEquals(expected_object_name, 'Test url')

class ChartModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Chart.objects.create(title='Test chart')
        Chart.objects.create(description='Test description')

    def test_title_content(self):
        chart = Chart.objects.get(chart_id=1)
        expected_object_name = f'{chart.title}'
        self.assertEquals(expected_object_name, 'Test chart')

    def test_description_content(self):
        chart = Chart.objects.get(chart_id=2)
        expected_object_name = f'{chart.description}'
        self.assertEquals(expected_object_name, 'Test description')