{%- if cookiecutter.license == "MIT" -%}
# Possible license content here

{%- elif cookiecutter.license == "BSD-3" -%}
# More possible license content here

{% endif %}


Distributed under the terms of the `{{cookiecutter.license}}`_ license,


{%- if cookiecutter.run_as_docker -%}
# In case of True add your content here

{%- else -%}
# In case of False add your content here

{% endif %}
