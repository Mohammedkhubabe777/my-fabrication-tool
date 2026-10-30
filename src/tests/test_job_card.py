import pytest
from src.job_card import FabricationJobCard


def test_calculate_estimate():
    job = FabricationJobCard(
        client_name="Test Client",
        item_type="Enclosure Box",
        material_key="MS_SHEET_2MM",
        weight_kg=10.0,
        labor_hours=2.0
    )
    assert job.calculate_estimate() == 1180.0


def test_update_status():
    job = FabricationJobCard(
        client_name="Test Client",
        item_type="Enclosure Box",
        material_key="MS_SHEET_2MM",
        weight_kg=10.0,
        labor_hours=2.0
    )
    job.update_status("In Progress")
    assert job.status == "In Progress"


def test_invalid_material():
    with pytest.raises(ValueError):
        FabricationJobCard(
            client_name="Test Client",
            item_type="Invalid Item",
            material_key="UNKNOWN_STEEL",
            weight_kg=10.0,
            labor_hours=2.0
        )
