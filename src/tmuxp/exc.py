"""Exceptions for tmuxp.

tmuxp.exc
~~~~~~~~~

"""
import typing as t

from ._compat import implements_to_string


class TmuxpException(Exception):

    """Base Exception for Tmuxp Errors."""


class WorkspaceError(TmuxpException):

    """Error parsing tmuxp workspace data."""


class EmptyWorkspaceException(WorkspaceError):

    """Workspace file is empty."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        return super().__init__("Session configuration is empty.", *args, **kwargs)


class TmuxpPluginException(TmuxpException):

    """Base Exception for Tmuxp Errors."""


class BeforeLoadScriptNotExists(OSError):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.strerror = "before_script file '%s' doesn't exist." % self.strerror


@implements_to_string
class BeforeLoadScriptError(Exception):

    """Exception replacing :py:class:`subprocess.CalledProcessError` for
    :meth:`tmuxp.util.run_before_script`.
    """

    def __init__(
        self, returncode: int, cmd: str, output: t.Optional[str] = None
    ) -> None:
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.message = (
            f"before_script failed with returncode {self.returncode}.\n"
            f"command: {self.cmd}\n"
            "Error output:\n"
            f"{self.output}"
        )

    def __str__(self):
        return self.message
