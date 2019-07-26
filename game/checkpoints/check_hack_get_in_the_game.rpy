label check_hack_get_in_the_game:
    python:
        import hack_get_in_the_game
        import trace
        solved = False

        tracer = trace.Trace(count=False, trace=True)
        tracer.run('hack_get_in_the_game.main()')

    return
