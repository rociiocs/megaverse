from unittest import TestCase
from unittest.mock import patch, Mock

from domain.enums.astral_color_enum import AstralColorEnum
from domain.enums.cometh_direction_enum import DirectionEnum
from infrastructure.factories.astral_object_factory import AstralObjectFactory


class TestAstralObjectFactory(TestCase):
    def setUp(self):
        self.factory = AstralObjectFactory()

    def test_create_polyanet_without_property(self):
        mock_class = Mock()
        with patch.dict(self.factory.astral_object_class_mapper, {"polyanet": mock_class}):
            self.factory.create("polyanet", None, 1, 2)

        mock_class.assert_called_once_with(1, 2)

    def test_create_soloon_with_color(self):
        mock_class = Mock()
        with patch.dict(self.factory.astral_object_class_mapper, {"soloon": mock_class}):
            self.factory.create("soloon", "blue", 0, 0)

        mock_class.assert_called_once_with(0, 0, AstralColorEnum.BLUE)

    def test_create_cometh_with_direction(self):
        mock_class = Mock()
        with patch.dict(self.factory.astral_object_class_mapper, {"cometh": mock_class}):
            self.factory.create("cometh", "right", 0, 0)

        mock_class.assert_called_once_with(0, 0, DirectionEnum.RIGHT)

    def test_create_invalid_type_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.factory.create("invalid_type", None, 0, 0)
        self.assertIn("There is not any astral object", str(context.exception))

    @patch("infrastructure.factories.astral_object_factory.Polyanet", side_effect=TypeError("missing argument"))
    def test_create_raises_type_error(self, _):
        with self.assertRaises(ValueError) as context:
            self.factory.create("polyanet", None)
        self.assertIn("Error creating 'polyanet'", str(context.exception))

    def test_get_astral_object_property_returns_enum(self):
        result = self.factory._AstralObjectFactory__get_astral_object_property("soloon", "red")
        self.assertEqual(result, AstralColorEnum.RED)

    def test_get_astral_object_property_returns_none_if_not_enum(self):
        result = self.factory._AstralObjectFactory__get_astral_object_property("polyanet", "any")
        self.assertIsNone(result)
