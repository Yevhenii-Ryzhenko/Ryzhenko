import pytest
from lesson_15.homework_15 import Rhombus

class TestRhombus:
    @pytest.mark.rhombus
    def test_side_negative_0(self):
        with pytest.raises(AttributeError):
            Rhombus (0, 110)

    @pytest.mark.rhombus
    def test_side_negative_minus(self):
        with pytest.raises(AttributeError):
            Rhombus (-10, 110)

    @pytest.mark.rhombus
    def test_angle_a_negative_0(self):
        with pytest.raises(AttributeError):
            Rhombus (10, 0)

    @pytest.mark.rhombus
    def test_angle_a_negative_minus(self):
        with pytest.raises(AttributeError):
            Rhombus (10, -10)

    @pytest.mark.rhombus
    def test_angle_a_negative_180(self):
        with pytest.raises(AttributeError):
            Rhombus (10, 180)

    @pytest.mark.rhombus
    def test_angle_a_negative_more_180(self):
        with pytest.raises(AttributeError):
            Rhombus (10, 190)

    @pytest.mark.rhombus
    def test_angle_b(self):
        romb_1 = Rhombus(10, 100)
        assert romb_1.angle_b == 80

    @pytest.mark.rhombus
    def test_angle_b_after_update_angle_a(self):
        romb_2 = Rhombus(10, 100)
        romb_2.angle_a = 120
        assert romb_2.angle_b == 60

    @pytest.mark.rhombus
    def test_rhombus(self):
        romb_3 = Rhombus(10, 80)
        assert romb_3.side_a == 10
        assert romb_3.angle_a == 80
        assert romb_3.angle_b == 100

