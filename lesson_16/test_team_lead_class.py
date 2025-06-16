import pytest
from lesson_16.homework_16_1 import TeamLead


class TestTeamLeadAttr:

    lead = TeamLead("Yevhenii", 20000, "IT", "Python", 5)

    @classmethod
    def test_team_lead_has_attr_from_employee(cls):

        assert hasattr(cls.lead, "name")
        assert hasattr(cls.lead, "salary")

    @classmethod
    def test_team_lead_has_attr_from_manager(cls):

        assert hasattr(cls.lead, "department")

    @classmethod
    def test_team_lead_has_attr_from_developer(cls):

        assert hasattr(cls.lead, "programming_language")

    @classmethod
    def test_team_lead_has__own_attr(cls):

        assert hasattr(cls.lead, "team_size")

