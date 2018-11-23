from hook import Hook

def comment(commenter, content):
    args = {
        'commenter': commenter,
        'host': 'myself'
    }
    Hook.call('COMMENT_BEFORE', **args)
    print(content) 
    Hook.call('COMMENT_AFTER', **args)

# 注册两个钩子
Hook.register_action('COMMENT_AFTER','test_plugin', 'send_to_commenter')
Hook.register_action('COMMENT_AFTER','test_plugin', 'send_to_host')

# 模拟运行 comment 行为
comment('someone@domain.com', 'Hello, Guys')