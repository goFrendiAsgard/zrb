from typing import List
from zrb import Input, DockerComposeTask, runner
from zrb.builtin._group import project_group
from .common import (
    RESOURCE_DIR,
    local_input, image_input, image_env
)

compose_inputs: List[Input] = [
    local_input,
    image_input,
]
compose_env_prefix = 'CONTAINER_ENV_PREFIX'

build_snake_app_name_image = DockerComposeTask(
    icon='🏭',
    name='build-kebab-app-name-image',
    description='Build human readable app name image',
    group=project_group,
    inputs=compose_inputs,
    envs=[image_env],
    skip_execution='{{not input.local_snake_app_name}}',
    cwd=RESOURCE_DIR,
    compose_cmd='build',
    compose_flags=[
        '--no-cache'
    ],
    compose_env_prefix=compose_env_prefix,
)
runner.register(build_snake_app_name_image)

push_snake_app_name_image = DockerComposeTask(
    icon='📰',
    name='push-kebab-app-name-image',
    description='Push human readable app name image',
    group=project_group,
    inputs=compose_inputs,
    envs=[image_env],
    upstreams=[build_snake_app_name_image],
    cwd=RESOURCE_DIR,
    compose_cmd='push',
    compose_env_prefix=compose_env_prefix,
)
runner.register(push_snake_app_name_image)
