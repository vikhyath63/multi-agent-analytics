import pytest
from app.analytics import initialize,run_query
def test_scopes_results(tmp_path):
    db=tmp_path/"x.db"; initialize(db); result=run_query("revenue by region","Retail",db)
    assert result["business_unit_scope"]=="Retail" and result["row_count"]==2
def test_rejects_unknown_intent(tmp_path):
    db=tmp_path/"x.db"; initialize(db)
    with pytest.raises(ValueError): run_query("delete all data",None,db)
