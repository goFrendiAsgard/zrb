from zrb.builtin._group import project_group
from zrb import Task, runner

remove_project_containers = Task(
    name='remove-containers',
    group=project_group,
    upstreams=[],
    description='Remove project containers'
)
runner.register(remove_project_containers)
