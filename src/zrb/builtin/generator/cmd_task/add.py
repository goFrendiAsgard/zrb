from typing import Any
from ..._group import project_add_group
from ....task.task import Task
from ....task.resource_maker import ResourceMaker
from ....runner import runner
from .._common import (
    project_dir_input, task_name_input, validate_project_dir,
    validate_new_task_name, register_task, get_default_task_replacements,
    get_default_task_replacement_middlewares, new_task_scaffold_lock
)

import os

# Common definitions

current_dir = os.path.dirname(__file__)


def _validate(*args: Any, **kwargs: Any):
    project_dir = kwargs.get('project_dir')
    validate_project_dir(project_dir)
    task_name = kwargs.get(project_dir, 'task_name')
    validate_new_task_name(project_dir, task_name)


def _create_task(*args: Any, **kwargs: Any):
    project_dir = kwargs.get('project_dir')
    validate_project_dir(project_dir)
    task_name = kwargs.get('task_name')
    return register_task(project_dir, task_name)


# Task definitions

validate = Task(
    name='task-validate-create',
    inputs=[project_dir_input, task_name_input],
    run=_validate
)

copy_resource = ResourceMaker(
    name='copy-resource',
    inputs=[project_dir_input, task_name_input],
    upstreams=[validate],
    replacements=get_default_task_replacements(),
    replacement_middlewares=get_default_task_replacement_middlewares(),
    template_path=os.path.join(current_dir, 'task_template'),
    destination_path='{{ input.project_dir }}',
    scaffold_locks=[new_task_scaffold_lock]
)

add_cmd_task = Task(
    name='cmd-task',
    group=project_add_group,
    inputs=[project_dir_input, task_name_input],
    run=_create_task,
    upstreams=[copy_resource]
)
runner.register(add_cmd_task)