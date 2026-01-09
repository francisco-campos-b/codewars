"""
8kyu
Create a class Ball.
Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
ball1 = new Ball();
ball2 = new Ball("super");
ball1.ballType //=> "regular"
ball2.ballType //=> "super"
"""


class Ball:
    """Class for ball type"""

    def __init__(self, ball_type: str = "regular") -> None:
        self.ball_type = ball_type

    def get_type(self) -> str:
        """Returns the type of the ball."""
        return self.ball_type

    def show_properties(self):
        """Displays a description of the ball's properties."""
        return f"This is a '{self.ball_type}' ball."
