class Rhombus :
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a' and value <= 0:
            raise AttributeError ('The side of the rhombus must be greater than 0')
        if key == 'angle_a':
            if not (0 < value < 180):
                raise AttributeError('Angle A must be between 0 and 180 degrees')
            super().__setattr__('angle_b', 180 - value)

        super().__setattr__(key, value)

rhombus = Rhombus(10, 100)
print(f'You have the following rhombus:\nSide A: {rhombus.side_a},\nAngle A: {rhombus.angle_a},\n'
      f'Angle B: {rhombus.angle_b}')


