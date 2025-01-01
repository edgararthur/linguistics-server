from admin_tools.dashboard import modules, Dashboard

class CustomDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(modules.ModelList(
            title='User Management',
            models=['auth.*'],
        ))
        self.children.append(modules.ModelList(
            title='Management',
            models=['appname.*'],
        ))
