class DriveBase:

    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def init(self):
        self.left_motor.init()
        self.right_motor.init()
    
    def set_power(self, power, r=None):
        """
        Set the motor powers. Single argument sets both.
        """
        self.set_left(power)
        self.set_right(power if r is None else r)

    def set_left(self, power):
        self.left_motor.set_power(power)

    def set_right(self, power):
        self.right_motor.set_power(power)
