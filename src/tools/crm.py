import logging

class CRMTool:
    def log_lead(self, name: str, phone: str, notes: str):
        # In a real app, this would save to a database or Salesforce
        logging.info(f"New Lead: {name} - {phone}. Notes: {notes}")
        return "Lead information successfully saved to CRM."