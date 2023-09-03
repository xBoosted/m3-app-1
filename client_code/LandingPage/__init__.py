from ._anvil_designer import LandingPageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class LandingPage(LandingPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    #anvil.users.login_with_form()
    #self.customer_list_panel.items = anvil.server.call('get_customers')
    #Add when ready

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('EmployeeData')
