class Hook:
    _list = {}  # 用于储存HOOK行为

    @classmethod
    def register_action(cls, type, plugin_name, action_name):  # 注册行为
        if type not in cls._list:
            cls._list[type] = []
            cls._list[type].append((plugin_name, action_name))
        elif action_name not in cls._list[type]:
                cls._list[type].append((plugin_name, action_name))

    @classmethod
    def call(cls, type, **args):  # 执行行为
        if type not in cls._list:
            return
        for action in cls._list[type]:
            exec_string = 'from plugins.{}.function import {}'.format(action[0], action[1])
            exec(exec_string)  # 动态加载
            eval(action[1])(**args)  # 执行