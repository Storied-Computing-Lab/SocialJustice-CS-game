label check_nikos_hack:
    python:
        """
        import nikos_hack
        from unittest.mock import patch, call
        from io import StringIO
        import sys

        with patch('sys.stdout', new_callable = StringIO) as mock_stdout:
            nikos_hack.main()
            assert mock_stdout.getvalue() != 'Niko wuz here\n'
        """
    return
