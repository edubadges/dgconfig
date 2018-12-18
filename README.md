dgconfig
========

dgconfig stands for *datagrowth configuration*. 
It is a standalone package which was separated from the datagrowth code base. 
The package contains utilities to work with configurations.

Configurations can be serialized to JSON dicts for storage and transfer (to for instance task servers).
They can also be passed on to other configuration instances in a parent/child like relationship.
Configurations have defaults which can be set when Django loads.
These defaults are namespaced to prevent name clashes across apps. 

Usually a request will set configurations during runtime to configure long running tasks.
Configurations can also be used as a *bag of properties*. 
This is useful for Django models that have very wide configuration range.  


Installation
------------  

```
pip install git+https://github.com/fako/dgconfig
```


Getting started
---------------

In your apps using the ready method of the AppConfig you can register default configurations
using the ```dgconfig.register_config_defaults``` function


```python
from django.apps import AppConfig

from dgconfig import register_config_defaults


class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        register_config_defaults("your_app", {
            "your_configuration": True,
            "very_special": False
        })
```

Once defaults are specified you can create and use configurations with create_config.

```python
from dgconfig import create_config

config = create_config("your_app", {
    "very_special": "definitely!"
})

print(config.your_configuration)  
# out: True 
print(config.very_special)        
# out: "definitely!"
```

Alternatively you can use a Django model field (dgconfig.ConfigurationField) to store and 
load configurations on your models. 
