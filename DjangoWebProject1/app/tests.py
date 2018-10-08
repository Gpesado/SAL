from django.test import TestCase

# Create your tests here.

from app.models import Usuario

class UsuarioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Usuario.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'Nombre')

    def test_last_name_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'died')

    def test_first_name_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('first_name').max_length
        self.assertEquals(max_length,30)

    def test_last_name_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('last_name').max_length
        self.assertEquals(max_length,30)

    def test_get_absolute_url(self):
        usuario=Usuario.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/app/usuario/1/update')