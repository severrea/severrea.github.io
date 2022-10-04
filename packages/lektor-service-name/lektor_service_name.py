# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor_envvars      import LektorEnv

class ServiceNameEnv(LektorEnv):
    def service_name(self, alt):
        default_name_var = self.prefix + 'SERVICE_NAME'
        custom_name_var  = default_name_var + '_' + alt.replace('-', '_').upper()

        return self.env(custom_name_var, self.env(default_name_var, ''))


class ServiceNamePlugin(Plugin):
    name = 'Service Name'
    description = u'A plugin that gets a localized site service name from environment variables.'

    def on_process_template_context(self, context, **extra):
        config                  = self.get_config()
        context['service_name'] = ServiceNameEnv(config).service_name
