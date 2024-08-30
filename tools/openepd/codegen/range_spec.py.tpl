{% for module, symbols in imports.items() %}{% if symbols %}
from {{module}} import {% for symbol in symbols%}{{symbol}}{{ ", " if not loop.last else "" }}{% endfor %}{% else %}
import {{module}}{% endif %}{% endfor %}

{% for range_spec in range_specs %}
class {{range_spec.classname}}(BaseOpenEpdHierarchicalSpec):
    """{{range_spec.class.__doc__ | format_multiline_comment}}
    Range version.
    """
    _EXT_VERSION = "{{range_spec.class._EXT_VERSION}}"
{% for field in range_spec.fields %}
    {{field.name}}: {{field.type}} = {{field.field_init}}{% endfor %}


{% endfor %}



__all__ = {% for range_spec in range_specs %}"{{range_spec.classname}}", {%endfor%}
