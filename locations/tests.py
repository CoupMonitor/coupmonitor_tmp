from django.test import TestCase
from .models import Location

# Create your tests here.

class LocationTestCass(TestCase):
    def setUp(self):
        Location.objects.language("en").create(name='Nasr City', govornorate='Cairo', lat=null, lon=null )
        Location.objects.language("ar").create(name="مدينة نصر", governorate='القاهرة', lat=null, lon = null)

        Location.objects.language("en").create(name='menyet el-nasr', governorate='Dakahlia', lat=1.213, lon=3.123)
        Location.objects.language("ar").create(name='منية النصر', governorate='الدقهلية', lat=1.213, lon=3,123)


    def test_location_multilingual(self):
        pass

    def test_location_null_latlon(self):
        pass


