import importlib, click

class _JobrGroup(click.Group):
    def __init__(self, 
                 *args, 
                 subcommands: dict[str,str] | None = None, 
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._sub_cmds = subcommands or {}
    
    def list_commands(self, ctx):
        return super().list_commands(ctx) + sorted(self._sub_cmds.keys())
    
    def get_command(self, ctx, cmd_name):
        if cmd_name in self._sub_cmds:
            return self._get_module(cmd_name)
        return super().get_command(ctx, cmd_name)
    
    def _get_module(self, cmd_name):
        import_path: str = self._sub_cmds.get(cmd_name, None)
        assert import_path
        mod_name, obj_name  = import_path.rsplit('.', 1)
        mod = importlib.import_module(mod_name)
        obj = getattr(mod, obj_name)
        if not isinstance(obj, click.Command):
            raise ValueError(f'{import_path} must be a command object')
        return obj