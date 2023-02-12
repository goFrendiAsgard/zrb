from typing import Any
from ..task.task import Task
from ..runner import runner
from ..config.config import version


def _version(*args: Any, **kwargs: Any) -> str:
    task: Task = kwargs['_task']
    task.print_out(version)
    return version


version_task = Task(
    name='version',
    run=_version,
    description='Get Zrb version',
)
runner.register(version_task)
