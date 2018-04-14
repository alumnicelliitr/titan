from website.models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms

class DistinguishForm(ModelForm):
	class Meta:
		model = DistinguishedAlumni
		exclude = ()
		labels = {
	    "nominee_name": _("Name"),
	"nominee_email":_("Email Address"),
	"nominee_contact":_("Contact No.:"),
	"nominee_degree": _("Degree obtained from University of Roorkee/IIT Roorkee"),
	"nominee_yearpass": _("Year of Graduation"),
	"nominee_quals": _("Other Educational Qualifications, if any"),
	"nominee_address": _("Address"),
	"nominee_designation":_("Designation and Affiliation"),
	"nominee_category":_("Category of Nomination"),
	"nominee_webpage":_("Personal Webpage, if available"),
	"nominee_linkedin":_("LinkedIn Profile Url, if available"),
	"nominee_description":_("Description of achievements in the category of nomination"),
	"nominee_awards":_("Details of Awards Received (Please mention the awarding entity, year and the work leading to the award)"),
	"nominee_photo":_("Recent Photograph (Preferred File Types : jpg,png)"),
	"nominee_resume":_("Resume of the nominee (Preferred File Types : pdf,docx)"),
	"nominator_name": _("Name"),
	"nominator_email":_("Email Address"),
	"nominator_contact":_("Contact No.:"),
	"nominator_designation":_("Designation and Affiliation"),
	"nominator_address":_("Address"),
	"nominator_affiliation":_("Your current or past associations with University of Roorkee/IIT Roorkee"),
	"nominator_moreinfo":_("I can be contacted for more information about the nominee"),
		}