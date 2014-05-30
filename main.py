from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import\
    NumericProperty,\
    ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # 'move' method will move the ball one step.
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):

    # This property must be set in the .kv file
    ball = ObjectProperty(None)

    # Initial configuration of the ball
    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    # This method is invoked every frame by Clock.schedule_interval()
    def update(self, dt):
        self.ball.move()

        #bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        #bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()

        # Invoke game.update() every 1/60 seconds (60 Hz)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()

