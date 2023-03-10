from typing import Any, List, Mapping


def fetch_external_env(data: Any) -> Mapping[str, str]:
    global_env_dict = {}
    if 'services' not in data:
        return global_env_dict
    for service in data['services']:
        if 'environment' not in data['services'][service]:
            continue
        environments = data['services'][service]['environment']
        if isinstance(environments, list):
            for environment in environments:
                parts: List[str] = environment.split('=')
                if len(parts) > 0:
                    env_str = parts[1]
                    env_dict = parse_external_env_string(env_str)
                    global_env_dict.update(env_dict)
        if isinstance(environments, dict):
            for _, env_str in environments.items():
                env_dict = parse_external_env_string(env_str)
                global_env_dict.update(env_dict)
    return global_env_dict


def parse_external_env_string(env_str: str) -> Mapping[str, str]:
    env_dict = {}
    stack = []
    key = ''
    value = ''
    index = 0
    while index < len(env_str):
        char = env_str[index]
        if char == '{':
            stack.append(index)
        elif char == '}':
            start = stack.pop()
            if not stack:
                segment = env_str[start+1:index]
                if ':-' in segment:
                    key, value = segment.split(':-', 1)
                    if value.startswith('${') and value.endswith('}'):
                        sub_dict = parse_external_env_string(value)
                        env_dict.update(sub_dict)
                else:
                    key = segment
                    value = ''
                if '${' in value:
                    value = ''
                env_dict[key] = value
                key = ''
                value = ''
        index += 1
    return env_dict
