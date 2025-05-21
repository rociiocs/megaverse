from unittest import TestCase
from unittest.mock import Mock

from domain.models.astral_object import AstralObject
from infrastructure.astral_object_adapter import AstralObjectAdapter
from infrastructure.factories.astral_object_factory import AstralObjectFactory


class TestAstralObjectAdapter(TestCase):

    def setUp(self):
        self.adapter = AstralObjectAdapter()
        self.adapter.astral_objects_factory = Mock(spec=AstralObjectFactory)

    def test_get_list_astral_objects_ignores_space(self):
        megaverse_map = [
            ["SPACE", "RED_SOLOON"],
            ["POLYANET", "SPACE"],
            ["POLYANET", "RIGHT_COMETH"]
        ]

        fake_astral_object = Mock(spec=AstralObject)
        self.adapter.astral_objects_factory.create.return_value = fake_astral_object

        result = self.adapter.get_list_astral_objects(megaverse_map)

        self.assertEqual(len(result), 4)
        self.adapter.astral_objects_factory.create.assert_any_call("soloon", "red", 0, 1)
        self.adapter.astral_objects_factory.create.assert_any_call("polyanet", None, 1, 0)
        self.adapter.astral_objects_factory.create.assert_any_call("cometh", "right", 2, 1)

    def test_get_object_type_and_property_value_with_color(self):
        result = self.adapter._AstralObjectAdapter__get_object_type_and_property_value("blue_SOLOON")
        self.assertEqual(result, ("soloon", "blue"))

    def test_get_object_type_and_property_value_without_property(self):
        result = self.adapter._AstralObjectAdapter__get_object_type_and_property_value("POLYANET")
        self.assertEqual(result, ("polyanet", None))

    def test_get_object_type_and_property_value_invalid_format(self):
        with self.assertRaises(ValueError):
            self.adapter._AstralObjectAdapter__get_object_type_and_property_value(None)
