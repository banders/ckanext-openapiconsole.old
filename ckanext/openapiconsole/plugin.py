
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckanext.openapiconsole.model import OpenApiSpecUrl
from ckan.common import request

log = __import__('logging').getLogger(__name__)

class OpenApiConsolePlugin(p.SingletonPlugin, tk.DefaultDatasetForm): 

  #p.implements(p.IDatasetForm)
  p.implements(p.IConfigurer)
  p.implements(p.IPackageController, inherit=True) # to be notified on package create/update/delete/show events
  p.implements(p.ITemplateHelpers)

  def update_config(self, config):

      # Add this plugin's templates dir to CKAN's extra_template_paths, so
      # that CKAN will use this plugin's custom templates.
      # 'templates' is the path to the templates dir, relative to this
      # plugin.py file.
      tk.add_template_directory(config, 'templates')

      # Add this plugin's public dir to CKAN's extra_public_paths, so
      # that CKAN will use this plugin's custom static files.
      tk.add_public_directory(config, 'public')

  def after_create(self, context, pkg_dict):
    if "openapi_spec_url" in request.params:
      OpenApiSpecUrl.create_or_update(pkg_dict['id'], request.params["openapi_spec_url"])

  def after_update(self, context, pkg_dict):
    if "openapi_spec_url" in request.params:
      OpenApiSpecUrl.create_or_update(pkg_dict['id'], request.params["openapi_spec_url"])

  def get_helpers(self):     
    return {'get_openapi_specs_for_package': OpenApiSpecUrl.get_for_package}

"""
#TODO: remove these methods.
#these methods are only needed if the ApenApiConsolePlugin stores the openapi_spec_url
#in the main database schema.  they aren't needed if the plugin stores its data in
#its own DB tables, which is the new direction this plugin has taken.
  def _modify_package_schema(self, schema):
    schema.update({
        "openapi_spec_url": [tk.get_validator('ignore_missing'),
                              tk.get_converter('convert_to_extras')]
    })
    return schema

  def create_package_schema(self):
      schema = super(OpenApiConsolePlugin, self).create_package_schema()
      schema = self._modify_package_schema(schema)
      return schema

  def update_package_schema(self):
      schema = super(OpenApiConsolePlugin, self).update_package_schema()
      schema = self._modify_package_schema(schema)
      return schema

  def show_package_schema(self):
      schema = super(OpenApiConsolePlugin, self).show_package_schema()        
      schema.update({
          "openapi_spec_url": [tk.get_converter('convert_from_extras'),
                                tk.get_validator('ignore_missing')]
      })
      return schema

  def is_fallback(self):
      # Return True to register this plugin as the default handler for
      # package types not handled by any other IDatasetForm plugin.
      return True

  def package_types(self):
      # This plugin doesn't handle any special package types, it just
      # registers itself as the default (above).
      return []
"""