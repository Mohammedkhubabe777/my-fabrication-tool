import uuid
from datetime import datetime


class FabricationJobCard:
    """Digital Job Card system for managing metal fabrication orders."""

    MATERIAL_RATES_PER_KG = {
        "MS_ANGLE_5MM": 62.0,
        "MS_SHEET_2MM": 68.0,
        "ISMB_CHANNEL_100MM": 75.0,
    }

    LABOR_HOURLY_RATE = 250.0

    def __init__(self, client_name: str, item_type: str, material_key: str, weight_kg: float, labor_hours: float):
        if material_key not in self.MATERIAL_RATES_PER_KG:
            raise ValueError(f"Invalid material key: {material_key}")
        
        self.job_id = f"SV-{uuid.uuid4().hex[:6].upper()}"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client_name = client_name
        self.item_type = item_type
        self.material_key = material_key
        self.weight_kg = weight_kg
        self.labor_hours = labor_hours
        self.status = "Queued"

    def calculate_estimate(self) -> float:
        material_cost = self.weight_kg * self.MATERIAL_RATES_PER_KG[self.material_key]
        labor_cost = self.labor_hours * self.LABOR_HOURLY_RATE
        return round(material_cost + labor_cost, 2)

    def update_status(self, new_status: str):
        valid_statuses = ["Queued", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Status must be one of {valid_statuses}")
        self.status = new_status

    def generate_whatsapp_quote(self) -> str:
        total = self.calculate_estimate()
        return (
            f"🛠️ *Sri Venkateshwara Fabrication Quote*\n"
            f"Job Ref: {self.job_id}\n"
            f"Client: {self.client_name}\n"
            f"Item: {self.item_type}\n"
            f"Estimated Total: ₹{total:,.2f}\n"
            f"Status: {self.status}"
        )


if __name__ == "__main__":
    job = FabricationJobCard(
        client_name="Rajesh Contractor",
        item_type="Tractor Trailer Tow Hook",
        material_key="MS_ANGLE_5MM",
        weight_kg=35.0,
        labor_hours=4.0
    )
    print(job.generate_whatsapp_quote())
