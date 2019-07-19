import pytest
from viewmodels import HandModel

@pytest.mark.skip(reason='hardening') 
class Test_HandModel:

    def test_model_constructor_sorted(self):
        model = HandModel(['AS', 'TS', '5S'])
        assert model.cards == ['5S', 'TS', 'AS']

    def test_model_sorted_by_suit(self):
        model = HandModel(['AS', 'AD', 'AC', 'AH'])
        assert model.cards == ['AC', 'AD', 'AH', 'AS']
