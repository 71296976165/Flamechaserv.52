transform offScreenBottomLeft:
    xpos 0.0 xanchor 1.0 ypos 2.0 yanchor 1.0

define leftSide = MoveTransition(
                    delay = 0.3,
                    enter = offScreenBottomLeft,
                    leave = offScreenBottomLeft,
                    old = False,
                    layers = ['master'],
                    time_warp = ease,
                    enter_time_warp = None,
                    leave_time_warp = None)

transform offScreenBottomRight:
    xpos 2.0 xanchor 0.5 ypos 2.0 yanchor 1.0

define rightSide = MoveTransition(
                    delay = 0.3,
                    enter = offScreenBottomRight,
                    leave = offScreenBottomRight,
                    old = False,
                    layers = ['master'],
                    time_warp = ease,
                    enter_time_warp = None,
                    leave_time_warp = None)
